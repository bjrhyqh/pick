#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import sys

import moveit_commander
from geometry_msgs.msg import PoseStamped, Pose
from moveit_commander import MoveGroupCommander,PlanningSceneInterface
from moveit_msgs.msg import PlanningScene, ObjectColor
from moveit_msgs.msg import Grasp, GripperTranslation, MoveItErrorCodes
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from tf.transformations import quaternion_from_euler
from copy import deepcopy

import argparse
import math
import actionlib
#from moveit_python import PlanningSceneInterface

from std_msgs.msg import String


GROUP_NAME_ARM = 'manipulator'
GROUP_NAME_GRIPPER = 'endeffector'

GRIPPER_FRAME = 'ee_link'

#GRIPPER_OPEN = [-3.05224325814e-07,7.81728974886e-08,1.22023372739e-07,2.90163406191e-07,7.8392321079e-08,1.21948984244e-07,1.4411528948e-07,3.20080372873e-07]
#GRIPPER_CLOSED = [2.35887606532e-05,1.57009445431,0.196806690076,3.15720422064e-05,1.56986026264,0.0775878033416,0.69992368317,0.800053345822]
#GRIPPER_NEUTRAL = [-3.05224325814e-07,7.81728974886e-08,1.22023372739e-07,2.90163406191e-07,7.8392321079e-08,1.21948984244e-07,1.4411528948e-07,3.20080372873e-07]

#GRIPPER_JOINT_NAMES = ['bh_j11_joint','bh_j12_joint','bh_j13_joint','bh_j21_joint','bh_j22_joint','bh_j23_joint','bh_j32_joint','bh_j33_joint']
GRIPPER_OPEN=[1.98267356799e-05]
GRIPPER_CLOSED=[0.6]
GRIPPER_NEUTRAL=[1.98267356799e-05]
GRIPPER_JOINT_NAMES=['finger_joint']
GRIPPER_EFFORT = [1.0]

REFERENCE_FRAME = 'base_link'
rx= -0.5
ry= -0.6
rz= 0.5

class MoveItDemo:
    def __init__(self):
        # Initialize the move_group API
        moveit_commander.roscpp_initialize(sys.argv)

        rospy.init_node('moveit_demo')

        # Use the planning scene object to add or remove objects
        scene = PlanningSceneInterface()

        # Create a scene publisher to push changes to the scene
        self.scene_pub = rospy.Publisher('planning_scene', PlanningScene, queue_size=5)

        # Create a publisher for displaying gripper poses
        self.gripper_pose_pub = rospy.Publisher('gripper_pose', PoseStamped, queue_size=5)

        # Create a dictionary to hold object colors
        self.colors = dict()

        # Initialize the move group for the right arm
        my_arm = MoveGroupCommander(GROUP_NAME_ARM)

        # Initialize the move group for the right gripper
        my_gripper = MoveGroupCommander(GROUP_NAME_GRIPPER)

        # Get the name of the end-effector link
        end_effector_link = my_arm.get_end_effector_link()

        # Allow some leeway in position (meters) and orientation (radians)
        my_arm.set_goal_position_tolerance(0.05)
        my_arm.set_goal_orientation_tolerance(0.1)

        # Allow replanning to increase the odds of a solution
        my_arm.allow_replanning(True)

        # Set the right arm reference frame
        my_arm.set_pose_reference_frame(REFERENCE_FRAME)

        # Allow 5 seconds per planning attempt
        my_arm.set_planning_time(15)

        # Set a limit on the number of pick attempts before bailing
        max_pick_attempts = 5

        # Set a limit on the number of place attempts
        max_place_attempts = 3

        # Give the scene a chance to catch up
        rospy.sleep(2)

        #remove objects from a previous session

        # Start the arm in the "resting" pose stored in the SRDF file
        #right_arm.set_named_target('resting')
        #right_arm.go()
#        joint_positions = [-0.0253998950875,-0.709038560046,0.927768320774,1.40608266002,-1.56855335407,0.0245406559189]
#        my_arm.set_joint_value_target(joint_positions)
#        my_arm.go()
#        rospy.sleep(1)

        # Open the gripper to the neutral position
        my_gripper.set_joint_value_target(GRIPPER_NEUTRAL)
        my_gripper.go()

        rospy.sleep(1)

        #find_objects
#        rospy.Subscriber("",String,callback);
        table_id='table'
        target_id='target'
        table_size=[0.6,0.32,0.4]
        target_size=[0.18,0.18,0.2]
        table_ground=0

        # Add a table top and two boxes to the scene
        table_pose = PoseStamped()
        table_pose.header.frame_id = REFERENCE_FRAME
        table_pose.pose.position.x = 0.2-rx
        table_pose.pose.position.y = 0.0-ry
        table_pose.pose.position.z = table_ground + table_size[2] / 2.0 -rz
        table_pose.pose.orientation.w = 1.0
        scene.add_box(table_id, table_pose, table_size) #so does box


        # Set the target pose in between the boxes and on the table,the target is defined by photos shot by camera
        target_pose = PoseStamped()
        target_pose.header.frame_id = REFERENCE_FRAME
        target_pose.pose.position.x = 0.2-rx
        target_pose.pose.position.y = 0.0-ry
        target_pose.pose.position.z = table_ground + table_size[2] + target_size[2] / 2.0 -rz
        target_pose.pose.orientation.w = 1.0

        # Add the target object to the scene
        scene.add_box(target_id, target_pose, target_size)

        # Set the support surface name to the table object
        my_arm.set_support_surface_name(table_id)

#        # Specify a pose to place the target after being picked up
#        place_pose = PoseStamped()
#        place_pose.header.frame_id = REFERENCE_FRAME
#        place_pose.pose.position.x = 0.18
#        place_pose.pose.position.y = -0.18
#        place_pose.pose.position.z = table_ground + table_size[2] + target_size[2] / 2.0
#        place_pose.pose.orientation.w = 1.0

        # Initialize the grasp pose to the target pose
        grasp_pose = target_pose

        # Shift the grasp pose by half the width of the target to center it!!!!!there are other ways to shift
        grasp_pose.pose.position.x += target_size[0] / 2.0
        grasp_pose.pose.position.y -= target_size[1] / 2.0
        grasp_pose.pose.position.z += target_size[2] / 2.0

        # Generate a list of grasps
        grasps = self.make_grasps(grasp_pose, [target_id])

#        # Publish the grasp poses so they can be viewed in RViz
#        for grasp in grasps:
#            self.gripper_pose_pub.publish(grasp.grasp_pose)
#            rospy.sleep(0.2)

        # Track success/failure and number of attempts for pick operation
        result = None
        n_attempts = 0

        # Repeat until we succeed or run out of attempts
        while result != MoveItErrorCodes.SUCCESS and n_attempts < max_pick_attempts:
                n_attempts += 1
                rospy.loginfo("Pick attempt: " +  str(n_attempts))
                result = my_arm.pick(target_id, grasps)
                rospy.loginfo(result)
                rospy.sleep(0.2)

#        # If the pick was successful, attempt the place operation
#        if result == MoveItErrorCodes.SUCCESS:
#                result = None
#                n_attempts = 0

#                # Generate valid place poses
#                places = self.make_places(place_pose)

#                 # Repeat until we succeed or run out of attempts
#                while result != MoveItErrorCodes.SUCCESS and n_attempts < max_place_attempts:
#                    n_attempts += 1
#                    rospy.loginfo("Place attempt: " +  str(n_attempts))
#                        for place in places:
#                            result = my_arm.place(target_id, place)
#                            if result == MoveItErrorCodes.SUCCESS:
#                                break
#                        rospy.sleep(0.2)

#                if result != MoveItErrorCodes.SUCCESS:
#                    rospy.loginfo("Place operation failed after " + str(n_attempts) + " attempts.")
#        else:
#                rospy.loginfo("Pick operation failed after " + str(n_attempts) + " attempts.")




#        # Open the gripper to the neutral position
#        my_gripper.set_joint_value_target(GRIPPER_NEUTRAL)
#        my_gripper.go()

#        rospy.sleep(2)

#        # Return the arm to the "resting" pose stored in the SRDF file
#        my_arm.set_named_target('resting')
#        my_arm.go()

#        rospy.sleep(2)

        if args.once:
            # Shut down MoveIt cleanly
            moveit_commander.roscpp_shutdown()

            # Exit the script
            moveit_commander.os._exit(0)




    # Get the gripper posture as a JointTrajectory
    def make_gripper_posture(self, joint_positions):
            # Initialize the joint trajectory for the gripper joints
            t = JointTrajectory()

            # Set the joint names to the gripper joint names
            t.joint_names = GRIPPER_JOINT_NAMES

            # Initialize a joint trajectory point to represent the goal
            tp = JointTrajectoryPoint()

            # Assign the trajectory joint positions to the input positions
            tp.positions = joint_positions

            # Set the gripper effort
            tp.effort = GRIPPER_EFFORT

            tp.time_from_start = rospy.Duration(1.0)

            # Append the goal point to the trajectory points
            t.points.append(tp)

            # Return the joint trajectory
            return t



    # Generate a gripper translation in the direction given by vector
    def make_gripper_translation(self, min_dist, desired, vector):
        # Initialize the gripper translation object
        g = GripperTranslation()

        # Set the direction vector components to the input
        g.direction.vector.x = vector[0]
        g.direction.vector.y = vector[1]
        g.direction.vector.z = vector[2]

        # The vector is relative to the gripper frame
        g.direction.header.frame_id = GRIPPER_FRAME

        # Assign the min and desired distances from the input
        g.min_distance = min_dist
        g.desired_distance = desired

        return g



    # Generate a list of possible grasps
    def make_grasps(self, initial_pose_stamped, allowed_touch_objects):
            # Initialize the grasp object
            g = Grasp()

            # Set the pre-grasp and grasp postures appropriately
            g.pre_grasp_posture = self.make_gripper_posture(GRIPPER_OPEN)
            g.grasp_posture = self.make_gripper_posture(GRIPPER_CLOSED)

            # Set the approach and retreat parameters as desired
            g.pre_grasp_approach = self.make_gripper_translation(0.05, 0.15, [1.0, 0.0, 0.0])
            g.post_grasp_retreat = self.make_gripper_translation(0.05, 0.15, [-1.0, 0.0, 0.0])

            # Set the first grasp pose to the input pose
            g.grasp_pose = initial_pose_stamped
            rospy.loginfo(g.grasp_pose)

            # Pitch angles to try
            pitch_vals = [0, 0.1, -0.1, 0.2, -0.2, 0.3, -0.3]

            # Yaw angles to try
            yaw_vals = [0]

            # A list to hold the grasps
            grasps = []

            # Generate a grasp for each pitch and yaw angle
            for y in yaw_vals:
                for p in pitch_vals:
                    # Create a quaternion from the Euler angles
                    q = quaternion_from_euler(0, p, y)

                    # Set the grasp pose orientation accordingly
                    g.grasp_pose.pose.orientation.x = q[0]
                    g.grasp_pose.pose.orientation.y = q[1]
                    g.grasp_pose.pose.orientation.z = q[2]
                    g.grasp_pose.pose.orientation.w = q[3]

                    # Set and id for this grasp (simply needs to be unique)
                    g.id = str(len(grasps))

                    # Set the allowed touch objects to the input list
                    g.allowed_touch_objects = allowed_touch_objects

                    # Don't restrict contact force
                    g.max_contact_force = 0

                    # Degrade grasp quality for increasing pitch angles
                    g.grasp_quality = 1.0 - abs(p)

                    rospy.loginfo(g)

                    # Append the grasp to the list
                    grasps.append(deepcopy(g))

            # Return the list
            return grasps




#        # Generate a list of possible place poses
#        def make_places(self, init_pose):
#                    # Initialize the place location as a PoseStamped message
#                    place = PoseStamped()

#                    # Start with the input place pose
#                    place = init_pose

#                    # A list of x shifts (meters) to try
#                    x_vals = [0, 0.005, 0.01, 0.015, -0.005, -0.01, -0.015]

#                    # A list of y shifts (meters) to try
#                    y_vals = [0, 0.005, 0.01, 0.015, -0.005, -0.01, -0.015]

#                    pitch_vals = [0]

#                    # A list of yaw angles to try
#                    yaw_vals = [0]

#                    # A list to hold the places
#                    places = []

#                    # Generate a place pose for each angle and translation
#                    for y in yaw_vals:
#                        for p in pitch_vals:
#                            for y in y_vals:
#                                for x in x_vals:
#                                    place.pose.position.x = init_pose.pose.position.x + x
#                                    place.pose.position.y = init_pose.pose.position.y + y

#                                    # Create a quaternion from the Euler angles
#                                    q = quaternion_from_euler(0, p, y)

#                                    # Set the place pose orientation accordingly
#                                    place.pose.orientation.x = q[0]
#                                    place.pose.orientation.y = q[1]
#                                    place.pose.orientation.z = q[2]
#                                    place.pose.orientation.w = q[3]

#                                    # Append this place pose to the list
#                                    places.append(deepcopy(place))

#                    # Return the list
#            return places


#        def callback(data):
#            target=^


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple demo of pick and place")
    parser.add_argument("--objects", help="Just do object perception", action="store_true")
    parser.add_argument("--all", help="Just do object perception, but insert all objects", action="store_true")
    parser.add_argument("--once", help="Run once.", action="store_true")
    parser.add_argument("--ready", help="Move the arm to the ready position.", action="store_true")
    parser.add_argument("--plan", help="Only do planning, no execution", action="store_true")
    parser.add_argument("--x", help="Recommended x offset, how far out an object should roughly be.", type=float, default=0.5)
    args, unknown = parser.parse_known_args()

    MoveItDemo()

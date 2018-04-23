#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
import random
import actionlib
from moveit_commander import RobotCommander,MoveGroupCommander, PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float64MultiArray,MultiArrayDimension
from control_msgs.msg import GripperCommandAction,FollowJointTrajectoryAction
#joint_names =  ['finger_joint', 'left_inner_knuckle_joint', 'left_inner_finger_joint', 'right_outer_knuckle_joint', 'right_inner_knuckle_joint', 'right_inner_finger_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
#positions =  [0.2928262968941126, -0.2928262968941126, 0.2928262968941126, -0.2928262968941126, -0.2928262968941126, 0.2928262968941126, 0.44286313484323736, -1.1781581860491328, 1.7121511388933512, 1.0374444266562388, 1.5704395720709645, -2.698212672994671]
joint_names =  ['bh_j11_joint', 'bh_j12_joint', 'bh_j13_joint', 'bh_j21_joint', 'bh_j22_joint', 'bh_j23_joint', 'bh_j32_joint', 'bh_j33_joint' , 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']
positions=[-4.8131156305e-07,1.91061237942e-08,1.04382530175e-07,5.67669449225e-07,1.88695592485e-08,1.04431044257e-07,-1.31666154424e-07,-3.32972122763e-07,5.3371648753e-05,1.01259812944e-05,-1.26940372986e-05,-8.65806874053e-05,-3.62772395235e-06,3.25003214563e-06]
#closed=[0.000162433572622,1.12238992706,0.201603807468,-0.000312831535641,1.12238992706,0.201611557441,1.14644963267,0.336005363529]
closed=[0.000162433572622, 1.122, 0.201603807468, -0.000312831535641, 1.122, 0.201611557441, 1, 0]
#def default_grip(arm):


if __name__=='__main__':

    roscpp_initialize(sys.argv)
    rospy.init_node('moveit_py_demo', anonymous=True)

    scene = PlanningSceneInterface()
    robot = RobotCommander()
    arm =  MoveGroupCommander("manipulator")
    eef = MoveGroupCommander("endeffector")
    rospy.sleep(1)
    #Start State Gripper
    group_variable_values = eef.get_current_joint_values()
#    group_variable_values[0] = 0.0
    eef.set_joint_value_target(group_variable_values)
    plan2 = eef.plan()
    arm.execute(plan2)
    # clean the scene
    scene.remove_world_object("pole")
    scene.remove_world_object("table")
    scene.remove_world_object("part")

    client = actionlib.SimpleActionClient('gripper_controller/gripper_action', FollowJointTrajectoryAction)
    if not client.wait_for_server(rospy.Duration(5.0)):
        rospy.logerr('Pick up action client not available!')
        rospy.signal_shutdown('Pick up action client not available!')

    # publish a demo scene
    k = PoseStamped()
    k.header.frame_id = robot.get_planning_frame()
    k.pose.position.x = 0.0
    k.pose.position.y = 0.0
    k.pose.position.z = -0.05
    scene.add_box("table", k, (2,2, 0.0001))
    p = PoseStamped()
    p.header.frame_id = robot.get_planning_frame()
    p.pose.position.x = 0.35
    p.pose.position.y = 0.35
    p.pose.position.z = 0.05
    scene.add_box("part", p, (0.09,0.09,0.2))

    rospy.sleep(1)
#Planning Part 1: Move to correct xy coorinate
    temPose = p
#    temPose.pose.position.z -= 0.00
#    temPose.pose.position.x += 0.135
#    temPose.pose.orientation.y = 1
    temPose.pose.position.z=0.3
    temPose.pose.orientation.y=0.707
    temPose.pose.orientation.w=0.707
    print temPose
    arm.set_pose_target(temPose)
    pl = arm.plan()
    state =arm.execute(pl)
    print state
    rospy.sleep(5)
#    if(state):
#        group_variable_values = eef.get_current_joint_values()
#        group_variable_values[2]=0.247599990879
#        group_variable_values[5]=0.247599990879
#        group_variable_values[7]=0.003999972383
#        eef.set_joint_value_target(group_variable_values)
#        plan2 = eef.plan()
#        eef.execute(plan2)
#        scene.remove_world_object("part")
#        rospy.loginfo(scene)
#        rospy.sleep(5)
#        group_variable_values[1]=1.21800000337
#        group_variable_values[4]=1.21800000337
#        group_variable_values[6]=1.35919998815
#        eef.set_joint_value_target(group_variable_values)
#        plan22 = eef.plan()
#        eef.execute(plan22)
#        eef.go()
#        client.wait_for_server()
#        goal=FollowJointTrajectoryAction().action_goal.goal
#        goal.trajectory=plan22.joint_trajectory
#        rospy.loginfo(goal)
#        rospy.sleep(10)
#        state = client.send_goal_and_wait(goal)
#        rospy.loginfo(state)
#        if state == 0:
#            rospy.logerr('Pick up goal failed!: %s' % client.get_goal_status_text())
#        rospy.sleep(0.05)
        #Planning Part 3: Grip
#        x= eef.attach_object("part","ee_link")
#        if(x):
#        place_pose = PoseStamped()
#        place_pose.header.frame_id = robot.get_planning_frame()
#        place_pose.pose.position.x = 0.324157
#        place_pose.pose.position.y = 0.354343
#        place_pose.pose.position.z = 0.575525
#        place_pose.pose.orientation.x = 0.00014
#        place_pose.pose.orientation.y = 0.884293
#        place_pose.pose.orientation.z = 0.466933

#        arm.set_pose_target(place_pose)
#        pl = arm.plan()
#        state =arm.execute(pl)
#        print state
#            if(state):
#                place_pose = PoseStamped()
#                place_pose.header.frame_id = robot.get_planning_frame()
#                place_pose.pose.position.x = -0.5
#                place_pose.pose.position.y = -0.6
#                place_pose.pose.position.z = 0.35
#                place_pose.pose.orientation.y = 1
#                arm.set_pose_target(place_pose)
#                pl = arm.plan()
#                state =arm.execute(pl)
#                print state
#                if(state):
#                    group_variable_values = eef.get_current_joint_values()
#                    group_variable_values[0] = 0.0
#                    eef.detach_object("part")
#                    place_pose = PoseStamped()
#                    place_pose.header.frame_id = robot.get_planning_frame()
#                    place_pose.pose.position.x = -0.495562
#                    place_pose.pose.position.y = -0.607059
#                    place_pose.pose.position.z = 0.417763
#                    place_pose.pose.orientation.y = 1
#                    arm.set_pose_target(place_pose)
#                    pl = arm.plan()
#                    state =arm.execute(pl)
#                    print state
#    rospy.spin()
#rospy.signal_shutdown("end")

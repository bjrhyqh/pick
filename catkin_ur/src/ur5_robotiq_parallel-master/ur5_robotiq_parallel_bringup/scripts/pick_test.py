#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy
import random
import actionlib
from moveit_commander import RobotCommander,MoveGroupCommander, PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Float64,MultiArrayDimension
from control_msgs.msg import GripperCommandAction,FollowJointTrajectoryAction
from gazebo_ros_link_attacher.srv import Attach, AttachRequest, AttachResponse

if __name__=='__main__':

    roscpp_initialize(sys.argv)
    rospy.init_node('moveit_py_demo', anonymous=True)

    scene = PlanningSceneInterface()
    robot = RobotCommander()
    arm =  MoveGroupCommander("manipulator")
    eef = MoveGroupCommander("gripper")
    rospy.sleep(1)


    # clean the scene
    scene.remove_world_object("pole")
    scene.remove_world_object("table")
    scene.remove_world_object("part")

    client = actionlib.SimpleActionClient('gripper_controller/gripper_action', GripperCommandAction)
    if not client.wait_for_server(rospy.Duration(5.0)):
        rospy.logerr('Pick up action client not available!')
        rospy.signal_shutdown('Pick up action client not available!')

    # publish a demo scene
    k = PoseStamped()
    k.header.frame_id = robot.get_planning_frame()
    k.pose.position.x = 0
    k.pose.position.y = 0
    k.pose.position.z = -0.05-0.025
    scene.add_box("table", k, (2,2, 0.0001))
    p = PoseStamped()
    p.header.frame_id = robot.get_planning_frame()
    p.pose.position.x = -0.6
    p.pose.position.y = 0.7
    p.pose.position.z = 0.1-0.025
    scene.add_box("part", p, (0.04,0.04,0.2))

    rospy.sleep(1)

    temPose = p
    temPose.pose.position.z -= 0.01
    temPose.pose.position.x +=0.125
    temPose.pose.orientation.y = 1
#    temPose.pose.orientation.w = 0.707
    print temPose
    arm.set_pose_target(temPose)
    pl = arm.plan()
    state =arm.execute(pl)
    print state
    rospy.sleep(1)

    if(state):
        cnt=-1
        while cnt<7:
            client.wait_for_server()
            goal=GripperCommandAction().action_goal.goal
            if cnt<0:
                goal.command.position=0.35
            else:
                goal.command.position=0.445-(2**(6-cnt))*0.001
            rospy.loginfo(goal.command.position)
            rospy.sleep(1)
            state = client.send_goal_and_wait(goal)
            cnt=cnt+1
            if state == 0:
                rospy.logerr('Pick up goal failed!: %s' % client.get_goal_status_text())
            rospy.sleep(0.05)

    rospy.loginfo("Creating ServiceProxy to /link_attacher_node/attach")
    attach_srv = rospy.ServiceProxy('/link_attacher_node/attach',
                                    Attach)
    attach_srv.wait_for_service()
    rospy.loginfo("Created ServiceProxy to /link_attacher_node/attach")


    rospy.loginfo("Attaching finger and cube")
    req = AttachRequest()
    req.model_name_1 = "robot"
    req.link_name_1 = "robotiq_85_right_finger_tip_link"
    req.model_name_2 = "coke_can_box_model"
    req.link_name_2 = "coke_can"

    attach_srv.call(req)

    scene.remove_world_object("part")
    rospy.sleep(0.1)
    place_pose = PoseStamped()
    place_pose.header.frame_id = robot.get_planning_frame()
    place_pose.pose.position.x = -0.424157
    place_pose.pose.position.y = 0.604343
    place_pose.pose.position.z = 0.275525
    place_pose.pose.orientation.x = 0
    place_pose.pose.orientation.y = 1
    place_pose.pose.orientation.z = 0
    place_pose.pose.orientation.w= 0

    arm.set_pose_target(place_pose)
    pl = arm.plan()
    state =arm.execute(pl)
    print state

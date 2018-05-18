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

    rospy.init_node('demo_attach_links')
    rospy.loginfo("Creating ServiceProxy to /link_attacher_node/attach")
    attach_srv = rospy.ServiceProxy('/link_attacher_node/attach',
                                    Attach)
    attach_srv.wait_for_service()
    rospy.loginfo("Created ServiceProxy to /link_attacher_node/attach")


    rospy.loginfo("Attaching finger and cube")
    req = AttachRequest()
    req.model_name_1 = "robot"
    req.link_name_1 = "bh_finger_11_link"
    req.model_name_2 = "coke_can_box_model"
    req.link_name_2 = "coke_can"
    attach_srv.call(req)

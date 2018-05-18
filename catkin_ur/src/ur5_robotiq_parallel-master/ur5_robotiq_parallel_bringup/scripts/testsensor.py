#!/usr/bin/env python
# -*- coding: utf-8 -*-
PKG = 'ur5_robotiq_parallel_bringup'
NAME = 'test_bumper'

import math
import roslib,actionlib
#roslib.load_manifest(PKG)

import sys, unittest
import os, os.path, threading, time
import rospy, rostest
from nav_msgs.msg import *
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Wrench
from geometry_msgs.msg import Vector3
from gazebo_msgs.msg import ContactsState
from gazebo_msgs.msg import ContactState

class TestSensor:

    def __init__(self):
        rospy.init_node('bumper_test')
        self.bumper_topic_name = "~bumper_topic_name"
        self.bumper_topic = "/test_bumper"
        self.bumper_state = ContactsState()
        self.sample_count = 0
        rospy.Subscriber(self.bumper_topic, ContactsState, self.bumperStateInput)
#        self.server = actionlib.SimpleActionServer(self.bumper_topic, ContactsState, self.bumperStateInput,auto_start=False)
#        self.server.start()
#        rospy.spin()

    def bumperStateInput(self, contacts_state):
        self.bumper_state = contacts_state
        self.sample_count+=1
        rospy.loginfo(self.bumper_state)
        rospy.loginfo(self.sample_count)
        rospy.sleep(5.0)

if __name__=='__main__':
    try:
        TestSensor()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo('Hasta la Vista...')

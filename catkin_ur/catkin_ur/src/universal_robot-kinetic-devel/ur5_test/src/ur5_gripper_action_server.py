#!/usr/bin/env python
import rospy, actionlib
import thread
from control_msgs.msg import GripperCommandAction,FollowJointTrajectoryAction
from std_msgs.msg import Float64
from trajectory_msgs.msg import JointTrajectory
from math import asin
class ParallelGripperActionController:
 
   def __init__(self):
       rospy.init_node('gripper_controller')
     
       self.r_pub = rospy.Publisher('gripper_controller/command', JointTrajectory,queue_size=1000)
#       self.r_pub = rospy.Publisher('gripper_controller/command', Float64, queue_size=10)        # subscribe to command and then spin
       self.server = actionlib.SimpleActionServer('~gripper_action', FollowJointTrajectoryAction,execute_cb=self.actionCb, auto_start=False)
       self.server.start()
       rospy.spin()

   def actionCb(self, goal):
#        Take an input command of width to open gripper.
#       rospy.loginfo('Gripper controller action goal recieved:%f' % goal.command.position)
       rospy.loginfo('Gripper controller action goal recievedf')
#       command = goal.command.position
       
       # publish msgs
       
#       rmsg = Float64(command)
       rmsg=JointTrajectory()
#       rmsg.joint_names=['bh_j11_joint', 'bh_j12_joint', 'bh_j13_joint', 'bh_j21_joint', 'bh_j22_joint', 'bh_j23_joint', 'bh_j32_joint', 'bh_j33_joint']
       rmsg.joint_names=['finger_joint']
       rmsg.points=goal.trajectory.points
       self.r_pub.publish(rmsg)
       rospy.sleep(5.0)
       self.server.set_succeeded()
       rospy.loginfo('Gripper Controller: Done.')
if __name__=='__main__':
   try:
       ParallelGripperActionController()
   except rospy.ROSInterruptException:
       rospy.loginfo('Hasta la Vista...')

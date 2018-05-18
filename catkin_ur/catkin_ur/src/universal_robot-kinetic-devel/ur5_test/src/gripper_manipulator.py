#!/usr/bin/env python
import sys
import rospy
import random
import math
import copy
import tf
from moveit_commander import RobotCommander,MoveGroupCommander, PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from geometry_msgs.msg import PoseStamped

class UR5_Gripped_Manipulator:

  """
  Class Attributes
  Robot        : Robot Commander Object
  Scene        : Planning Scene Interface Object (current scene)
  Man          : MoveGroupCommander object to control manipulator
  EEF          : MoveGroupCommander object to control endeffector
  Target_poses : Pose list of created target objects
  Picked       : List of part indexes to ensure to picked non-picked ones
  """
  def __init__(self,manip_name="manipulator",eef_name="endeffector") :
      self.robot = RobotCommander()
      self.man = MoveGroupCommander(manip_name)
      self.eef = MoveGroupCommander(eef_name)
      self.target_poses = []
      self.picked = []
  """
  ----------------Function Name: clean_scene----------------
  Definition: Clears the target_poses and picked lists in order to establish a new execution. Necessary for test_simulation method
  """
  def clear_poses(self):
       for i in xrange(len(self.target_poses)):  
            self.target_poses.pop() 
       for i in xrange(len(self.picked)):
            self.picked.pop() 
	
  """
  ----------------Function Name: clean_scene----------------
  Definition   : Clears all non-attached objects from planning scene
  Group        : MoveGroupCommander object to control given group
  """		
  def default_state_gripper(self,grp):
      rospy.loginfo("Openning Gripper")
      joint_vals = grp.get_current_joint_values()
      joint_vals[0] = 0.0
      grp.set_joint_value_target(joint_vals)
      init_plan = grp.plan()
      return grp.execute(init_plan)


  """
  ----------------Function Name: closed_state_gripper----------------
  Definition   : Function that opens gripper and detachs the gripped object
  Obj          : Name of the Object that is needed to detach
  """
  def closed_state_gripper(self,curr_scene, obj):
      rospy.loginfo("Closing Gripper")
      def convert(width):
          return 0.77 - width / 0.15316 * 0.77
      width = curr_scene.get_objects([obj])[obj].primitives[0].dimensions[0]
      width = convert(width)
      now = self.robot.endeffector.get_current_joint_values()[0]
      cnt = 0
      while abs(now - width) > 0.05:
          now = self.robot.endeffector.get_current_joint_values()[0]
          cnt = cnt + 1
          tmp = width - abs(now-width) / 2.0
          self.robot.endeffector.set_joint_value_target('finger_joint', tmp)
          self.robot.endeffector.go()
          rospy.sleep(0.05)
          if cnt == 7:
            break
      rospy.sleep(1.0)   
      ret = self.robot.manipulator.attach_object(obj)
      return ret

  """
  ----------------Function Name:  set_mid_state----------------
  Definition  : Motion planning function for defined mid state for manipulator, can be used for enhancing the performance if needed
  Group       : MoveGroupCommander object to control given group 
  """ 
  def set_mid_state(self,group):
      rospy.loginfo("Going to Mid-State")
      pos = PoseStamped()
      pos.header.frame_id = self.robot.get_planning_frame()
      pos.pose.position.x = 0.45358
      pos.pose.position.y = 0.188518
      pos.pose.position.z = 0.473063
      pos.pose.orientation.x = 0.0004738
      pos.pose.orientation.y = 1
      pos.pose.orientation.z = 0
      pos.pose.orientation.w = 0.000155894
      group.set_pose_target(pos)
      move_plan = group.plan()
      while(not move_plan.joint_trajectory.joint_names):
	        move_plan = group.plan()
      return group.execute(move_plan)

  """     
  ----------------Function Name: add_object----------------
  Name          : Object Name
  Pose	        : Pose of the Object (x,y,z,xo,yo,zo,wo)
  Dimension     : Dimensions of the Obhect (Tuple) (d1,d2,d3),
  Type          : Box(0),Sphere(1)
              d1 is radius for sphere i.e typ==1,
  """
  def add_object(self,name,x,y,z,xo=0.0,yo=0.0,zo=0.0,wo=0.0,d1=0.1,d2=0.1,d3=0.1,curr_scene=None,typ=0):
      pos = PoseStamped()
      pos.header.frame_id = self.robot.get_planning_frame()
      pos.pose.position.x = x
      pos.pose.position.y = y
      pos.pose.position.z = z
      pos.pose.orientation.x = xo
      pos.pose.orientation.y = yo
      pos.pose.orientation.z = zo
      pos.pose.orientation.w = wo
      rospy.loginfo("ADDING OBJECT")	
      if(typ==0):
          curr_scene.add_box(name, pos, (d1,d2,d3))
      elif(typ==1):
	  curr_scene.add_sphere(name,pos,d1)
      else:
	  print("ERROR in Type")
      return pos

  """
  ----------------Function Name: clean_scene----------------
  Definition: Clears all non-attached objects from planning scene
  """	
  def clean_scene(self,curr_scene):
      rospy.loginfo("Clearing the Scene")
      curr_scene.remove_world_object()

  """
  ----------------Function Name:  create_environment----------------
  Definition  : Creates the simulation environment with non-target collision objects, can be edited to create different default environment
  """ 	
  def create_environment(self,curr_scene):	    
       self.add_object(name="wall",x=0.0,y=0.8,z=0.5,d1=0.1,d2=0.35,d3=1,curr_scene = curr_scene,typ=0)
       self.add_object(name="wall_2",x=0.0,y=-0.8,z=0.5,d1=0.1,d2=0.35,d3=1,curr_scene = curr_scene,typ=0)
       self.add_object(name="table",x=0.0,y=0.0,z=-0.05,d1=2,d2=2,d3=0.0001,curr_scene = curr_scene,typ=0)
  """
  ----------------Function Name: check_targets----------------
  Definition  : Creates given number of objects within the distance provided. It prevents collision object overlapping.
         	It returns the pose list of the objects
  Number      : Number of collision objects required to spawn
  Distance    : Required minimum distance between each collision objects
  """
  def check_targets(self,curr_scene,number,distance):
      rospy.loginfo("Creating Boxes!")
      def al(typ,x=0.0):
          if typ == 'x': 
	            return random.uniform(0.35,0.65)
          elif typ =="y":
              rang = math.sqrt(0.7**2 -x**2)
              return random.uniform(-rang,rang)  
      hemme = []
      dims =[]
      cnt = 0
      while len(hemme) !=number :
          if cnt == 200:
              hemme = []
              cnt = 0
          cnt = cnt + 1
          dim = (random.uniform(0.08,0.12),random.uniform(0.08,0.10),random.uniform(0.05,0.2))
          quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0,random.uniform(-math.pi,math.pi))
          box = PoseStamped()
          box.header.frame_id = self.robot.get_planning_frame()
          box.pose.position.z = (-0.04 + (dim[2]/2))
          box.pose.position.x = al('x')
          box.pose.position.y = al('y',box.pose.position.x)
          box.pose.orientation.x = quaternion[0]
          box.pose.orientation.y = quaternion[1]
          box.pose.orientation.z = quaternion[2] 
          box.pose.orientation.w = quaternion[3]
          flag = 1     
          for i in hemme:
              if abs(i.pose.position.x - box.pose.position.x) < distance  or  abs(i.pose.position.y - box.pose.position.y) < distance:
                  flag = 0     
          if flag == 0:
              continue
          hemme.append(box)
	  dims.append(dim)
      cnt = 0
      names = []
      for i in xrange(len(hemme)):
          now = "part" + str(cnt)
          cnt = cnt + 1
          names.append(now)
          self.add_object(name=now,
		   x = hemme[i].pose.position.x,
		   y = hemme[i].pose.position.y,
		   z = hemme[i].pose.position.z,
		   xo = hemme[i].pose.orientation.x,
                   yo = hemme[i].pose.orientation.y,
                   zo = hemme[i].pose.orientation.z,      
                   wo = hemme[i].pose.orientation.w,
		   d1 = dims[i][0],
		   d2 = dims[i][1],
		   d3 = dims[i][2],
		   curr_scene = curr_scene,
		   typ =0)
      print ("End Check!")
      return hemme

  """
  ----------------Function Name:  pick_object----------------
  Definition  : It moves the given group i.e robot to the collision object whose index is given and picks that object.
  Group       : MoveGroupCommander object to control given group 
  Part_index  : Index of the target object to obtain pose
  """
  def pick_object(self,curr_scene,group,part_index):
      rospy.loginfo("Pick Operation starts!")
      gripped_object = curr_scene.get_objects(["part"+str(part_index)])["part"+str(part_index)]
      pos = copy.deepcopy(self.target_poses[part_index])
      temp = tf.transformations.euler_from_quaternion((pos.pose.orientation.x,pos.pose.orientation.y,pos.pose.orientation.z,pos.pose.orientation.w))
      quaternion = tf.transformations.quaternion_from_euler(math.pi, temp[1], temp[2])   
      pos.pose.position.z += 0.17  + (gripped_object.primitives[0].dimensions[2]/2.0)
      pos.pose.orientation.y = 1
      group.set_pose_target(pos)
      move_plan = group.plan()
      i = 0
      while(not move_plan.joint_trajectory.joint_names):
	move_plan = group.plan()
        i+=1
        if(i==500):break
      state = group.execute(move_plan)
      rospy.loginfo("Execute operation for Object is %s"%str(part_index))
      if(state):
          self.closed_state_gripper(curr_scene,"part"+str(part_index))
          rospy.sleep(1.0)
          self.place_object(curr_scene,group,part_index)
          return
      else:
	  return

  """
  ----------------Function Name:  place_object----------------
  Definition  : It places the gripped object to the target location
  Group       : MoveGroupCommander object to control given group 
  Part_index  : Index of the target object to obtain pose

  """    
  def place_object(self,curr_scene,group,part_index):
      pos = PoseStamped()
      def al(typ,x=0.0):
	if typ == 'x':
           return random.uniform(-0.35,-0.6)
	elif typ == 'y':
           rang = math.sqrt(0.75**2 -x**2)
	   x= random.uniform(-rang,rang)
	   while abs(x) < 0.15 :
	       x= random.uniform(-rang,rang)
	   return x
      pos = PoseStamped()
      pos.header.frame_id = robot.get_planning_frame()
      pos.pose.position.x = al("x")
      pos.pose.position.y = al("y",pos.pose.position.x)
      #This line makes placing possible by setting a valid z position for gripped object
      pos.pose.position.z = -0.04+ 0.17 + ((curr_scene.get_attached_objects(["part"+str(part_index)])["part"+str(part_index)]).object.primitives[0].dimensions[2])
      pos.pose.orientation.y =1.0
      group.set_pose_target(pos)
      move_plan = group.plan()
      while(not move_plan.joint_trajectory.joint_names):
		move_plan = group.plan()
      state = group.execute(move_plan)
      if(state):    
          detached= group.detach_object("part"+str(part_index))
	  rospy.sleep(1.5)
          if(detached):
              curr_scene.remove_world_object("part"+str(part_index))
              rospy.sleep(1.5)
              self.default_state_gripper(self.eef)
              self.picked.append(part_index)	
	  else:
              self.default_state_gripper(robot.endeffector)
              group.detach_object("part"+str(part_index))
              rospy.sleep(2)


  """
  ----------------Function Name: execute_simulation----------------
  Definition  : Creates the specified environment , generates motion plans and  does the pick and place operation based on these plans. To visualize RViz is needed.
		Planner ID can be changed based on MoveIT's supported OMPL.
  """                         
  def execute_simulation(self,curr_scene=None,num_of_objects = 3):
      is_success = False
      #Reset State of the Gripper 
      self.default_state_gripper(self.eef) 
      ####
      #Reset the position of the Arm
      # Will be implemented if needed
      ####    
      #Clean the scene
      self.clean_scene(curr_scene = curr_scene) 
      #Create environment
      self.create_environment(curr_scene = curr_scene)
      #Create targets
      self.target_poses = self.check_targets(curr_scene,num_of_objects,0.10)
      rospy.sleep(5)
      #Planner setup 	    
      self.man.set_planner_id("RRTConnectkConfigDefault")
      self.man.set_num_planning_attempts(20)
      self.man.allow_replanning(True)
      #Pick and place every object
      for i in xrange(len(self.target_poses)):
          if i not in self.picked:
              self.pick_object(curr_scene = curr_scene,group=self.man, part_index = i)
      rospy.loginfo("END OF PICK AND PLACE")
      if (len(self.picked) == len(self.target_poses)):
          is_success=True
      self.clear_poses()
      return is_success



  """
  ----------------Function Name: execute_simulation----------------
  Definition     : Executes the simulation num_attempts times. Stores the success rate 
                   and writes into the specified document
  Num_Attempts   : Limiting number for executing simulation. (Default Value: 10)
  File_Name      : File name (with path if needed) to write test results            
  """          
  def test_simulation(self,curr_scene = None,num_attempts = 10,num_of_objects = 3,file_name="ur5_pick_place_test.txt"):
      success_rate = 0
      file = open(file_name,"a+")
      file.write("Start Test \n")
      for case in xrange(1,num_attempts+1):
          state = self.execute_simulation(curr_scene = curr_scene,num_of_objects=num_of_objects)
          if(state):
              success_rate += 1
              rospy.loginfo("Success Rate: " + str(success_rate)+"/"+str(case))
              file.write("Test Case %s is successfull"%str(case))
          else:
              rospy.loginfo("Success Rate: " + str(success_rate)+"/"+str(case))
              file.write("Test Case %s is failedl"%str(case))
      file.write("Success: %" +str(((success_rate/(case-1)*100.0))))
      file.write("----END OF TEST----" )
      file.close()
      return  


if __name__ == "__main__":
    roscpp_initialize(sys.argv)
    rospy.init_node('moveit_py_demo', anonymous=True)
    scene = PlanningSceneInterface()
    control = UR5_Gripped_Manipulator()
    control.test_simulation(curr_scene = scene,num_of_objects=1)
    roscpp_shutdown()
    exit(0)

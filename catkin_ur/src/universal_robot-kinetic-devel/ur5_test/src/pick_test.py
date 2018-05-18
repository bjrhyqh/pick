#!/usr/bin/env python
import sys
import rospy
import random
import tf
import math
import copy
from moveit_commander import RobotCommander,MoveGroupCommander, PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from geometry_msgs.msg import PoseStamped

"""
GLobal lists for target objects.
Target_poses : Pose list of created target objects
Picked       : List of part indexes to ensure to picked non-picked ones
"""
target_poses = []
picked = []
"""
----------------Function Name:  set_mid_state----------------
Definition  : Motion planning function for defined mid state
Robot       : Robot Commander Object
Scene       : Planning Scene Interface Object (current scene)
""" 
def set_mid_state(group,robot):
    rospy.loginfo("Going to Mid-State")
    pos = PoseStamped()
    pos.header.frame_id = robot.get_planning_frame()
    pos.pose.position.x = 0.298122
    pos.pose.position.y = 0.043817
    pos.pose.position.z = 0.802048
    pos.pose.orientation.x = -0.000418977
    pos.pose.orientation.y = 1
    pos.pose.orientation.z = 0.000481335
    pos.pose.orientation.w = 0
    group.set_pose_target(pos)
    init_plan = group.plan()
    return group.execute(init_plan)
"""
----------------Function Name: check_targets----------------
Definition  : Creates given number of objects within the distance provided. It prevents collision object overlapping.
	      It returns the pose list of the objects
Scene       : Planning Scene Interface Object (current scene)
Robot       : Robot Commander Object
Number      : Number of collision objects required to spawn
Distance    : Required minimum distance between each collision objects
"""
def check_targets(robot,scene,number,distance):
    rospy.loginfo("Creating Boxes!")
    def al(typ,x=0.0):
	if typ == 'x':
	    return random.uniform(0.35,0.65)
	elif typ == 'y':
            rang = math.sqrt(0.70**2 -x**2)
            return random.uniform(-rang,rang)
    hemme = []
    dims = []
    cnt = 0
    while len(hemme) !=number :
        if cnt == 200:
            hemme = []
            dims = []
            cnt = 0
        cnt = cnt + 1
        dim = (random.uniform(0.08,0.12),random.uniform(0.08,0.10),random.uniform(0.05,0.2))
        quaternion = tf.transformations.quaternion_from_euler(0.0, 0.0,random.uniform(-math.pi	,math.pi))
        box = PoseStamped()
        box.header.frame_id = robot.get_planning_frame()
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
        print dim
    cnt = 0
    names = []
    print dims
    for i in xrange(len(hemme)):
        now = "part" + str(cnt)
        cnt = cnt + 1
        names.append(now)
        add_object(name=now,
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
		   robot = robot,
		   scene = scene,
		   typ =0)
    print "End Check!"	
    return hemme
	
"""
----------------Function Name: clean_scene----------------
Definition: Clears all non-attached objects from planning scene
Scene: PlanningSceneInterface Object (current scene)
"""	
def clean_scene(scene):
    rospy.loginfo("Clearing the Scene")
    scene.remove_world_object()	
def default_state_gripper(grp):
    rospy.loginfo("Openning Gripper")
    joint_vals = grp.get_current_joint_values()
    joint_vals[0] = 0.0
    grp.set_joint_value_target(joint_vals)
    init_plan = grp.plan()
    return grp.execute(init_plan)
"""
----------------Function Name: closed_state_gripper----------------
Definition   : Function that opens gripper and detachs the gripped object
Robot        : Robot Commander Object
Obj          : Name of the Object that is needed to detach
"""
def closed_state_gripper(robot, obj):
    rospy.loginfo("Closing Gripper")
    def convert(width):
        return 0.77 - width / 0.15316 * 0.77
    width = scene.get_objects([obj])[obj].primitives[0].dimensions[1]
    width = convert(width)
    now = robot.endeffector.get_current_joint_values()[0]
    cnt = 0
    while abs(now - width) > 0.05:
        now = robot.endeffector.get_current_joint_values()[0]
        cnt = cnt + 1
        tmp = width - abs(now-width) / 2.0
        robot.endeffector.set_joint_value_target('finger_joint', tmp)
        robot.endeffector.go()
	rospy.sleep(0.05)
        if cnt == 5:
            break
    rospy.sleep(1.0)   
    ret = robot.manipulator.attach_object(obj)
    return ret

"""
----------------Function Name: create_pose----------------
(x,y,z)       : Position Attributes of Pose Message
(xo,yo,zo,wo) : Orientation Attributes of Pose Message (Default Value: 0)
"""
def create_pose(x,y,z,xo=0.0,yo=0.0,zo=0.0,wo=0.0):
	pos = PoseStamped()
	pos.header.frame_id = robot.get_planning_frame()
        pos.pose.position.x = x
        pos.pose.position.y = y
        pos.pose.position.z = z
	pos.pose.orientation.x = xo
	pos.pose.orientation.y = yo
	pos.pose.orientation.z = zo
	pos.pose.orientation.w = wo
	return pos
"""
----------------Function Name: create_dimensions----------------
(d1,d2,d3)    : Dimensions of the object  (Default Value: 0.1)
"""
def create_dimensions(d1=0.1,d2=0.1,d3=0.1):
	return (d1,d2,d3)
"""     
----------------Function Name: add_object----------------
Name          : Object Name
Pose	      : Pose of the Object (x,y,z,xo,yo,zo,wo)
Dimension     : Dimensions of the Obhect (Tuple) (d1,d2,d3)
Type          : Box(0),Sphere(1)
Robot         : Robot Commander Object
Scene	      : Planning Scene Interface Object(current scene)

	d1 is radius for sphere i.e typ==1,
"""
def add_object(name,x,y,z,robot,scene,xo=0.0,yo=0.0,zo=0.0,wo=0.0,d1=0.1,d2=0.1,d3=0.1,typ=0):
	pos = PoseStamped()
	pos.header.frame_id = robot.get_planning_frame()
        pos.pose.position.x = x
        pos.pose.position.y = y
        pos.pose.position.z = z
	pos.pose.orientation.x = xo
	pos.pose.orientation.y = yo
	pos.pose.orientation.z = zo
	pos.pose.orientation.w = wo	
	if(typ==0):
    		scene.add_box(name, pos, (d1,d2,d3))
	elif(typ==1):
		scene.add_sphere(name,pos,d1)
	else:
		print "ERROR in Type"
	return pos
"""
----------------Function Name:  pick_object----------------
Definition  : It moves the given group i.e robot to the collision object whose index is given and picks that object.
Group       : MoveGroupCommander Object (Motion Planning group)
Part_index  : Index of the target object to obtain pose
Robot       : Robot Commander Object
Scene       : Planning Scene Interface Object (current scene)
"""
def pick_object(group,part_index,robot,scene):    
    rospy.loginfo("Pick Operation starts!")
    gripped_object = scene.get_objects(["part"+str(part_index)])["part"+str(part_index)]
    pos = copy.deepcopy(target_poses[part_index])
    temp = tf.transformations.euler_from_quaternion((pos.pose.orientation.x,pos.pose.orientation.y,pos.pose.orientation.z,pos.pose.orientation.w))
    quaternion = tf.transformations.quaternion_from_euler(math.pi, temp[1], temp[2])   
    pos.pose.position.z += 0.17  + (gripped_object.primitives[0].dimensions[2]/2.0)
    pos.pose.orientation.x = quaternion[0]
    pos.pose.orientation.y = quaternion[1]
    pos.pose.orientation.z = quaternion[2]
    pos.pose.orientation.w = quaternion[3]
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
        closed_state_gripper(robot,"part"+str(part_index))
	rospy.sleep(1.0)
	place_object(group,part_index,robot,scene)
	return
    else:
	
	return
"""
----------------Function Name:  place_object----------------
Definition  : It places the gripped object to the target location
Group       : MoveGroupCommander Object (Motion Planning group)
Part_index  : Index of the target object to obtain pose
Robot       : Robot Commander Object
Scene       : Planning Scene Interface Object (current scene)
"""    
def place_object(group,part_index,robot,scene):
        def al(typ,x=0.0):
	    if typ == 'x':
	        return random.uniform(-0.35,-0.6)
	    elif typ == 'y':
                rang = math.sqrt(0.75**2 -x**2)
	        x= random.uniform(-rang,rang)
            	print x
	        while abs(x) < 0.15 :
		    x= random.uniform(-rang,rang)
	        return x
	pos = PoseStamped()
	pos.header.frame_id = robot.get_planning_frame()
        
        pos.pose.position.x = al("x")
        pos.pose.position.y = al("y",pos.pose.position.x)
        rospy.loginfo(str((pos.pose.position.x,pos.pose.position.y)))
        """
        pos.pose.position.x = -0.565859
        pos.pose.position.y = -0.379874
        """
        #This line makes placing possible by setting a valid z position for gripped object
        pos.pose.position.z = -0.04+ 0.17 + ((scene.get_attached_objects(["part"+str(part_index)])["part"+str(part_index)]).object.primitives[0].dimensions[2])
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
			scene.remove_world_object("part"+str(part_index))
			rospy.sleep(1.5)
 			default_state_gripper(robot.endeffector)
			picked.append(part_index)
			
	else:
		default_state_gripper(robot.endeffector)
	        group.detach_object("part"+str(part_index))
		#rospy.sleep(1.5)
	        #set_mid_state(arm,robot)
	        rospy.sleep(2)
		
"""
----------------Function Name:  create_environment----------------
Definition  : Creates the simulation environment with non-target collision objects
Robot       : Robot Commander Object
Scene       : Planning Scene Interface Object (current scene)
""" 	
def create_environment(scene,robot):	
    
    add_object(name="wall",x=0.0,y=0.8,z=0.5,robot=robot,scene=scene,d1=0.1,d2=0.35,d3=1,typ=0)
    add_object(name="wall_2",x=0.0,y=-0.8,z=0.5,robot=robot,scene=scene,d1=0.1,d2=0.35,d3=1,typ=0)
    add_object(name="table",x=0.0,y=0.0,z=-0.05,robot=robot,scene=scene,d1=2,d2=2,d3=0.0001,typ=0)
    #add_object(name="table2",x=0.0,y=0.0,z=0.8,robot=robot,scene=scene,d1=2,d2=2,d3=0.0001,typ=0)
def clear_poses():
	for i in xrange(len(target_poses)):
		target_poses.pop() 
	for i in xrange(len(picked)):
		picked.pop()   
if __name__=='__main__':
    #Init
    libraries = {1 : "RRTConnect" , 2 : "RRTStar"}
    roscpp_initialize(sys.argv)
    rospy.init_node('moveit_py_demo', anonymous=True)
    scene = PlanningSceneInterface()
    robot = RobotCommander()
    arm =  MoveGroupCommander("manipulator")
    eef = MoveGroupCommander("endeffector")
    rospy.sleep(1)
    success_rate = 0 
    remain_object_per_try = []
    f = open('pick_test_stats.txt', 'w+')
    
    for tr in xrange(1,3):	  
	    #Reset State of the Gripper 
	    default_state_gripper(eef) 
	    ####
	    #Reset the position of the Arm
	    # Will be implemented if needed
            ####    
	    #Clean the scene
	    clean_scene(scene)
	    #Create environment
	    create_environment(scene,robot)
	    #Create target object
	    target_poses = check_targets(robot,scene,3,0.10)
	    f.write("Used Library: " + libraries[2])
      	    rospy.loginfo("TEST NUMBER: " +str(tr))   
	    rospy.sleep(1)
            
	    # Planner setup 	    
	    arm.set_planner_id("RRTConnectkConfigDefault")
	    arm.set_num_planning_attempts(20)
	    arm.allow_replanning(True)
	    #Pick and place every object
	    for i in xrange(len(target_poses)):
		if i not in picked:
			pick_object(group=arm, part_index = i,robot = robot,scene=scene)
			    
	    #For testing
	    if(len(picked) == len(target_poses)):
		success_rate +=1
	    rospy.loginfo("END OF PICK AND PLACE")
	    f.write("After try "+str(tr) + str(success_rate)+"/"+str(tr))
	    rospy.loginfo("Success Rate: " + str(success_rate)+"/"+str(tr))
            
           	
	    clear_poses()
            rospy.sleep(5.0)
f.write("Success= " +str(success_rate))
f.write("----END OF TEST----" )
f.close()
roscpp_shutdown()

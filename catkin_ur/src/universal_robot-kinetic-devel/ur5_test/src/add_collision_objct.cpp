#include <ros/ros.h>
#include <iostream>
#include <geometry_msgs/Pose.h>
// MoveIt! headers
#include <moveit/move_group_interface/move_group.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>

#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>

#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>

int main(int argc, char **argv){

    ros::init(argc, argv, "moveit_example_node");
    ros::NodeHandle node_handle;  
    ros::AsyncSpinner spinner(1);
    spinner.start();

    // here we define two main objects used in this node
    // we talk to the arm with MoveGroup object, in this particular
    // example, the group name must be "manipulator", because this is 
    // the way UR10 robotic arm defined in its configuration file.
    // we will need PlanningSceneInterface object to handle collision checking,
    // we will add collision objects to this scene and hope that MoveIt! controller
    // will find a path as specified.
    moveit::planning_interface::MoveGroup group("manipulator");
    moveit::planning_interface::PlanningSceneInterface planning_scene_interface;

    sleep(3.0);

    // we will put all of our collision objects in this vector.
    std::vector<moveit_msgs::CollisionObject> collision_objects;

    /*
     *  Now, we begin to create our collision objects.
     *
     *  First, we create the one fore bins, we think of the bins as a
     *  single part, and we use a simple box to model this volume.
     *
     */

    moveit_msgs::CollisionObject collision_object;

    // The id of the object is used to identify it and the reference
    // frame for this collision object.
    collision_object.id = "bin_box";
    collision_object.header.frame_id = group.getPlanningFrame();

    // Define a box to add to the world.
    shape_msgs::SolidPrimitive primitive;
    primitive.type = primitive.BOX;
    primitive.dimensions.resize(3);
    primitive.dimensions[0] = 2.0;
    primitive.dimensions[1] = 3.3;
    primitive.dimensions[2] = 0.1;

    // A pose for the box (specified relative to frame_id)
    geometry_msgs::Pose box_pose;
    box_pose.orientation.w = 1.0;
    box_pose.position.x =  -0.55;
    box_pose.position.y = -0.25;
    box_pose.position.z =  -0.1;

    // it seems like we add our box to our collision object...
    collision_object.primitives.push_back(primitive);
    collision_object.primitive_poses.push_back(box_pose);
    collision_object.operation = collision_object.ADD;

    // We add our collision object to our vector
    collision_objects.push_back(collision_object);

    /*
     *
     *  Secondly, we create the one for the top of workcell, we think of the top of the
     *  workcell as a single structure, and we use a simple box to model this volume.
     *
     */

    moveit_msgs::CollisionObject collision_object_2;

    // The id of the object is used to identify it and the reference
    // frame for this collision object.
    collision_object_2.id = "top_workcell_box";
    collision_object_2.header.frame_id = group.getPlanningFrame();

    // Define a box to add to the world.
    shape_msgs::SolidPrimitive primitive_2;
    primitive_2.type = primitive_2.BOX;
    primitive_2.dimensions.resize(3);
    primitive_2.dimensions[0] = 1.2;
    primitive_2.dimensions[1] = 3.3;
    primitive_2.dimensions[2] = 0.1;

    // A pose for the box (specified relative to frame_id).
    geometry_msgs::Pose box_pose_2;
    box_pose_2.orientation.w = 1.0;
    box_pose_2.position.x =  -0.7;
    box_pose_2.position.y = -0.25;
    box_pose_2.position.z = 1.2;

    // it seems like we add our box to our collision object...
    collision_object_2.primitives.push_back(primitive_2);
    collision_object_2.primitive_poses.push_back(box_pose_2);
    collision_object_2.operation = collision_object_2.ADD;

    // We add our collision object to our vector
    collision_objects.push_back(collision_object_2);

    /*
     *
     *  Thirdly, we create the one for the right side of the workcell, we think of the right
     *  side of the workcell as a single structure, and we use a simple box to model this volume.
     *
     */

    moveit_msgs::CollisionObject collision_object_3;

    // The id of the object is used to identify it and the reference
    // frame for this collision object.
    collision_object_3.id = "right_workcell_box";
    collision_object_3.header.frame_id = group.getPlanningFrame();

    // Define a box to add to the world.
    shape_msgs::SolidPrimitive primitive_3;
    primitive_3.type = primitive_3.BOX;
    primitive_3.dimensions.resize(3);
    primitive_3.dimensions[0] = 1.2;
    primitive_3.dimensions[1] = 1.5;
    primitive_3.dimensions[2] = 0.1;

    // A pose for the box (specified relative to frame_id).
    geometry_msgs::Pose box_pose_3;

    box_pose_3.orientation.x = 0.5;
    box_pose_3.orientation.y = -0.5;
    box_pose_3.orientation.z = -0.5;
    box_pose_3.orientation.w = -0.5;

    box_pose_3.position.x =  -0.70;
    box_pose_3.position.y = 1.50;
    box_pose_3.position.z = 0.60;

    // it seems like we add our box to our collision object...
    collision_object_3.primitives.push_back(primitive_3);
    collision_object_3.primitive_poses.push_back(box_pose_3);
    collision_object_3.operation = collision_object_3.ADD;

    // We add our collision object to our vector
    collision_objects.push_back(collision_object_3);

    /*
     *
     *  Similarly, we create the one for the left side of the workcell, we think of the left
     *  side of the workcell as a single structure, and we use a simple box to model this volume.
     *
     */

    moveit_msgs::CollisionObject collision_object_4;

    // The id of the object is used to identify it and the reference
    // frame for this collision object.
    collision_object_4.id = "left_workcell_box";
    collision_object_4.header.frame_id = group.getPlanningFrame();

    // Define a box to add to the world.
    shape_msgs::SolidPrimitive primitive_4;
    primitive_4.type = primitive_4.BOX;
    primitive_4.dimensions.resize(3);
    primitive_4.dimensions[0] = 1.2;
    primitive_4.dimensions[1] = 1.5;
    primitive_4.dimensions[2] = 0.1;

    // A pose for the box (specified relative to frame_id).
    geometry_msgs::Pose box_pose_4;

    box_pose_4.orientation.x = 0.5;
    box_pose_4.orientation.y = -0.5;
    box_pose_4.orientation.z = -0.5;
    box_pose_4.orientation.w = -0.5;

    box_pose_4.position.x =  -0.70;
    box_pose_4.position.y = -2.00;
    box_pose_4.position.z = 0.60;

    // it seems like we add our box to our collision object...
    collision_object_4.primitives.push_back(primitive_4);
    collision_object_4.primitive_poses.push_back(box_pose_4);
    collision_object_4.operation = collision_object_4.ADD;

    // We add our collision object to our vector
    collision_objects.push_back(collision_object_4);

    /*
     *
     *  Lastly, we create the one for the belt, we also think this one as a single
     *  structure that is long enough that our arm cannot reach the end of it.
     *
     */

   /* moveit_msgs::CollisionObject collision_object_5;

    // The id of the object is used to identify it and the reference
    // frame for this collision object.    
    collision_object_5.id = "belt_box";
    collision_object_5.header.frame_id = group.getPlanningFrame();

    // Define a box to add to the world.
    shape_msgs::SolidPrimitive primitive_5;
    primitive_5.type = primitive_5.BOX;
    primitive_5.dimensions.resize(3);
    primitive_5.dimensions[0] = 1.0;
    primitive_5.dimensions[1] = 4.5;
    primitive_5.dimensions[2] = 0.1;

    // A pose for the box (specified relative to frame_id).
    geometry_msgs::Pose box_pose_5;
    box_pose_5.orientation.w = 1.0;
    box_pose_5.position.x =  1.40;
    box_pose_5.position.y = -0.2;
    box_pose_5.position.z = 0.15;

    // it seems like we add our box to our collision object...
    collision_object_5.primitives.push_back(primitive_5);
    collision_object_5.primitive_poses.push_back(box_pose_5);
    collision_object_5.operation = collision_object_5.ADD;

    // We add our collision object to our vector
    collision_objects.push_back(collision_object_5);
*/
    // here, we add all of our collision objects to the planning
    // scene and hope for the best
    planning_scene_interface.addCollisionObjects(collision_objects);

    // /*
    //  *
    //  *  Here, you will find a hardcoded pose for our arm, with the following
    //  *  lines of code, I believe that you will have a good grasp of how can we
    //  *  define and go to the poses we want.
    //  *
    //  */
 
    // Planning with collision detection can be slow. Lets set 
    // the planning time to be sure the planner has enough time to 
    // plan around the collisions. 8 seconds should be plenty.
    group.setPlanningTime(8.0);

    // we create a new pose object
    geometry_msgs::Pose target_pose1;

	/* Default Values
	    target_pose1.orientation.x = 0.250749;
	    target_pose1.orientation.y = -0.661154;
	    target_pose1.orientation.z = 0.250749;
	    target_pose1.orientation.w = 0.661154;

	    
	    target_pose1.position.x = 0.7551;
	    target_pose1.position.y = 0.24275;
	    target_pose1.position.z = -0.005491;
	*/
    // we set orientations for our pose
    // notice that we use quaternions
    target_pose1.orientation.x = 0.500066;
    target_pose1.orientation.y = 0.49997;
    target_pose1.orientation.z = 0.499988;
    target_pose1.orientation.w = -0.499977;

    // we set positions for our pose
    target_pose1.position.x = 0.717263;
    target_pose1.position.y = 0.191372;
    target_pose1.position.z = 0.483229;

    // we set our pose as a target pose for our arm
    group.setPoseTarget(target_pose1);

    // we create a plan for the target position
    // we can use the "success" variable to check if we got
    // a plan and do something accordingly
    moveit::planning_interface::MoveGroup::Plan my_plan;
//    bool success = group.plan(my_plan);

    // THE ARM SHOULD MOVE WITH THIS FUNCTION
    // actually if (success)
    group.move();

    geometry_msgs::Pose target_pose2;
  /*
    // we set orientations for our pose
    // notice that we use quaternions
    target_pose2.orientation.x = 0.5;
    target_pose2.orientation.y = -0.5;
    target_pose2.orientation.z = -0.5;
    target_pose2.orientation.w = -0.5;

    // we set positions for our pose
    target_pose2.position.x = -0.466930;
    target_pose2.position.y = -0.498318;
    target_pose2.position.z = 0.75;

   
    // we set our pose as a target pose for our arm
    group.setPoseTarget(target_pose2);

    // we create a plan for the target position
    // we can use the "success" variable to check if we got
    // a plan and do something accordingly
    moveit::planning_interface::MoveGroup::Plan my_plan2;
    success = group.plan(my_plan2);

    // THE ARM SHOULD MOVE WITH THIS FUNCTION
    group.move();

    // we create a new pose object
    geometry_msgs::Pose target_pose3;

    // we set orientations for our pose
    // notice that we use quaternions
    target_pose3.orientation.x = 0.5;
    target_pose3.orientation.y = -0.5;
    target_pose3.orientation.z = -0.5;
    target_pose3.orientation.w = -0.5;

    // we set positions for our pose
    target_pose3.position.x = -0.466930;
    target_pose3.position.y = -0.498318;
    target_pose3.position.z = 1.10;

    // we set our pose as a target pose for our arm
    group.setPoseTarget(target_pose3);

    // we create a plan for the target position
    // we can use the "success" variable to check if we got
    // a plan and do something accordingly
    moveit::planning_interface::MoveGroup::Plan my_plan3;
    success = group.plan(my_plan3);

    // THE ARM SHOULD MOVE WITH THIS FUNCTION
    // actually if (success)
    group.move();
 */
    ros::shutdown();
    return 0;
}

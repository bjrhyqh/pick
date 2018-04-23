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
    collision_object.id = "bbox";
    collision_object.header.frame_id = group.getPlanningFrame();

    // Define a box to add to the world.
    shape_msgs::SolidPrimitive primitive;
    primitive.type = primitive.BOX;
    primitive.dimensions.resize(3);
    primitive.dimensions[0] = 0.1;
    primitive.dimensions[1] = 0.1;
    primitive.dimensions[2] = 0.1;

    // A pose for the box (specified relative to frame_id)
    geometry_msgs::Pose box_pose;
    box_pose.orientation.w = 1.0;
    box_pose.position.x =  0.82;
    box_pose.position.y = -0.25;
    box_pose.position.z = 0.005;

    // it seems like we add our box to our collision object...
  /*  collision_object.primitives.push_back(primitive);
    collision_object.primitive_poses.push_back(box_pose);
    collision_object.operation = collision_object.ADD;

    // We add our collision object to our vector
    collision_objects.push_back(collision_object);

    planning_scene_interface.addCollisionObjects(collision_objects);
   */
    group.setPlanningTime(20.0);

    // we create a new pose object
    geometry_msgs::Pose target_pose1;

    // we set orientations for our pose
    // notice that we use quaternions
    target_pose1.orientation.x = box_pose.orientation.x;
    target_pose1.orientation.y = box_pose.orientation.y;
    target_pose1.orientation.z = box_pose.orientation.z;
    target_pose1.orientation.w = box_pose.orientation.w;

    // we set positions for our pose
    target_pose1.position.x = box_pose.position.x;
    target_pose1.position.y = box_pose.position.y;
    target_pose1.position.z = box_pose.position.z;
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



    ros::shutdown();
    return 0;
}

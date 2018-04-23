#include <ros/ros.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "ur5_gripped");
  ros::NodeHandle nh;

  ROS_INFO("Hello world!");
}

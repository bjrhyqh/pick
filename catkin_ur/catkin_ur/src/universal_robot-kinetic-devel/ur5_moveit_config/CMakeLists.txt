cmake_minimum_required(VERSION 2.8.3)
project(ur5_moveit_config)

find_package(catkin REQUIRED COMPONENTS
  cmake_modules
  interactive_markers
  moveit_core
  moveit_ros_perception
  moveit_ros_planning_interface
  pluginlib
  roscpp
  std_msgs
)
find_package(Boost REQUIRED COMPONENTS system)

catkin_package()

SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -std=gnu++0x")

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})



include_directories(
  ${catkin_INCLUDE_DIRS}
)


## Declare a cpp executable
add_executable(test_random_node test_random.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
add_dependencies(test_random_node ur5_moveit_config_generate_messages_cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(test_random_node
   ${catkin_LIBRARIES}
 )

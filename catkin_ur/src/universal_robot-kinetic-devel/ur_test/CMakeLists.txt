cmake_minimum_required(VERSION 2.8.3)
project(ur_test)
set(CMAKE_MODULE_PATH ${ZBARCV_SOURCE_DIR})
## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  cmake_modules
  interactive_markers
  pluginlib
  roscpp
  std_msgs
  pcl_conversions
  pcl_ros
  cv_bridge
  image_transport
  sensor_msgs
)
find_package(catkin REQUIRED)
find_package(OpenCV REQUIRED)
find_package(ZBar0)

find_package(PkgConfig)
pkg_check_modules(PC_ZBAR QUIET zbar)
set(ZBAR_DEFINITIONS ${PC_ZBAR_CFLAGS_OTHER})
find_library(ZBAR_LIBRARIES NAMES zbar
             HINTS ${PC_ZBAR_LIBDIR} ${PC_ZBAR_LIBRARY_DIRS} )
find_path(ZBAR_INCLUDE_DIR Decoder.h
          HINTS ${PC_ZBAR_INCLUDEDIR} ${PC_ZBAR_INCLUDE_DIRS}
          PATH_SUFFIXES zbar )
include(FindPackageHandleStandardArgs)
find_package_handle_standard_args(ZBAR  DEFAULT_MSG  ZBAR_LIBRARIES ZBAR_INCLUDE_DIR)
## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES zbar_opencv
  CATKIN_DEPENDS cv_bridge image_transport roscpp sensor_msgs std_msgs
#  DEPENDS system_lib
)
include_directories(
  ${catkin_INCLUDE_DIRS}
)
## Declare a cpp executable
add_executable(pcl_write ur5_pointcl.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
add_dependencies(pcl_write ur_test_generate_messages_cpp)

## Specify libraries to link a library or executable target against
target_link_libraries(pcl_write
   ${catkin_LIBRARIES}
 )

add_executable(grayImage dxcimage.cpp)   #将src中的文件添加成名字为grayImage的可执行文件
#target_link_libraries(grayImage ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} opencv_nonfree)  #将相关的库和可执行文件链接
target_link_libraries(grayImage ${catkin_LIBRARIES} ${OpenCV_LIBRARIES})  #将相关的库和可执行文件链接
add_dependencies(grayImage robot_vision_generate_messages_cpp)  #给可执行文件添加依赖包

add_executable(zbar_opencv zbar_opencv.cpp)
target_link_libraries(zbar_opencv
  ${catkin_LIBRARIES}
  ${OpenCV_LIBRARIES}
  ${ZBAR_LIBRARIES}
)
#add_dependencies(zbar_opencv robot_vision_generate_messages_cpp)

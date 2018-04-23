cmake_minimum_required(VERSION 2.8.3)

project(pcl_test)
SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -std=gnu++0x")
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
find_package (PCL 1.8 REQUIRED)

set(PCL_INCLUDE_DIRS /usr/local/include/pcl-1.8)  #指定pcl1.8路径

add_definitions(${PCL_DEFINITIONS})


catkin_package(

#  INCLUDE_DIRS include

#  LIBRARIES ur_test

#  CATKIN_DEPENDS other_catkin_pkg

#  DEPENDS system_lib

)


include_directories(

# include

# ${catkin_INCLUDE_DIRS}

)

INCLUDE_DIRECTORIES(include ${OpenCV_INCLUDE_DIRS})


include_directories(

  ${catkin_INCLUDE_DIRS}
${PCL_INCLUDE_DIRS}
)


#add_executable(grayImage dxcimage.cpp)   #将src中的文件添加成名字为grayImage的可执行文件

#target_link_libraries(grayImage ${catkin_LIBRARIES} ${OpenCV_LIBRARIES} opencv_nonfree)  #将相关的库和可执行文件链接#


add_executable(LCCP LCCP.cpp)

target_link_libraries(LCCP ${catkin_LIBRARIES} ${PCL_LIBRARIES})

# Install script for directory: /home/cyr/catkin_ur/src

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/cyr/catkin_ur/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/cyr/catkin_ur/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/cyr/catkin_ur/install" TYPE PROGRAM FILES "/home/cyr/catkin_ur/build/catkin_generated/installspace/_setup_util.py")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/cyr/catkin_ur/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/cyr/catkin_ur/install" TYPE PROGRAM FILES "/home/cyr/catkin_ur/build/catkin_generated/installspace/env.sh")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/cyr/catkin_ur/install/setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/cyr/catkin_ur/install" TYPE FILE FILES "/home/cyr/catkin_ur/build/catkin_generated/installspace/setup.bash")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/cyr/catkin_ur/install/setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/cyr/catkin_ur/install" TYPE FILE FILES "/home/cyr/catkin_ur/build/catkin_generated/installspace/setup.sh")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/cyr/catkin_ur/install/setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/cyr/catkin_ur/install" TYPE FILE FILES "/home/cyr/catkin_ur/build/catkin_generated/installspace/setup.zsh")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/cyr/catkin_ur/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/cyr/catkin_ur/install" TYPE FILE FILES "/home/cyr/catkin_ur/build/catkin_generated/installspace/.rosinstall")
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/cyr/catkin_ur/build/gtest/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/bhand_description/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/universal_robot/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/ur5_robotiq_parallel-master/ur5_robotiq_parallel_description/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/ur5_robotiq_parallel-master/ur5_robotiq_parallel_moveit/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur_bringup/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur_description/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur_gazebo/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur_msgs/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/qr_detector-master/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/ur5_robotiq_parallel-master/robotiq_85_description/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/rqt_image_view-master/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/gazebo_ros_link_attacher-master/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/my_grasp/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/pcl_test/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/roboticsgroup_gazebo_plugins-master/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/ur5_robotiq_parallel-master/ur5_robotiq_parallel_bringup/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur_driver/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur_test/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur10_moveit_config/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur3_moveit_config/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur5_moveit_config/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur5hand_moveit_config/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur_kinematics/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/moveit_simple_grasps/cmake_install.cmake")
  include("/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/ur5_test/cmake_install.cmake")

endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/cyr/catkin_ur/build/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")

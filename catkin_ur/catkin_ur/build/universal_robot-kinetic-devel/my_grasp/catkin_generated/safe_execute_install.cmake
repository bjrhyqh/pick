execute_process(COMMAND "/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/my_grasp/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/cyr/catkin_ur/build/universal_robot-kinetic-devel/my_grasp/catkin_generated/python_distutils_install.sh) returned error code ")
endif()

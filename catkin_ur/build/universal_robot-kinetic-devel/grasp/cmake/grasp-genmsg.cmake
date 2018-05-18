# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "grasp: 1 messages, 0 services")

set(MSG_I_FLAGS "-Igrasp:/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(grasp_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg" NAME_WE)
add_custom_target(_grasp_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "grasp" "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(grasp
  "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grasp
)

### Generating Services

### Generating Module File
_generate_module_cpp(grasp
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grasp
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(grasp_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(grasp_generate_messages grasp_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg" NAME_WE)
add_dependencies(grasp_generate_messages_cpp _grasp_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grasp_gencpp)
add_dependencies(grasp_gencpp grasp_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grasp_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(grasp
  "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grasp
)

### Generating Services

### Generating Module File
_generate_module_eus(grasp
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grasp
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(grasp_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(grasp_generate_messages grasp_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg" NAME_WE)
add_dependencies(grasp_generate_messages_eus _grasp_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grasp_geneus)
add_dependencies(grasp_geneus grasp_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grasp_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(grasp
  "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grasp
)

### Generating Services

### Generating Module File
_generate_module_lisp(grasp
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grasp
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(grasp_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(grasp_generate_messages grasp_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg" NAME_WE)
add_dependencies(grasp_generate_messages_lisp _grasp_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grasp_genlisp)
add_dependencies(grasp_genlisp grasp_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grasp_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(grasp
  "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grasp
)

### Generating Services

### Generating Module File
_generate_module_nodejs(grasp
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grasp
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(grasp_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(grasp_generate_messages grasp_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg" NAME_WE)
add_dependencies(grasp_generate_messages_nodejs _grasp_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grasp_gennodejs)
add_dependencies(grasp_gennodejs grasp_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grasp_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(grasp
  "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grasp
)

### Generating Services

### Generating Module File
_generate_module_py(grasp
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grasp
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(grasp_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(grasp_generate_messages grasp_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/cyr/catkin_ur/src/universal_robot-kinetic-devel/grasp/msg/Num.msg" NAME_WE)
add_dependencies(grasp_generate_messages_py _grasp_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(grasp_genpy)
add_dependencies(grasp_genpy grasp_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS grasp_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grasp)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/grasp
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(grasp_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grasp)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/grasp
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(grasp_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grasp)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/grasp
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(grasp_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grasp)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/grasp
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(grasp_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grasp)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grasp\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grasp
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grasp
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/grasp/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(grasp_generate_messages_py std_msgs_generate_messages_py)
endif()

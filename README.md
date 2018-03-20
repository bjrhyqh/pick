# pick
20170317 cyr\
ur_description/urdf/ur_with_double.urdf 带抓手的机械臂\
ur_gazebo/controller/controllers.yaml 控制带抓手的机械臂，positioncontrollers/jointpositioncontroller已成功运行，但这种类型不一定存在于原始版本，可用rosservice call /controller_manager/list_controller_types检查，若没有可用sudo apt-get install ros*control*下载更多依赖包\
ur_test/dxcimage.cpp 双目视觉读取并定位，所用orb位于include中，暂未提交\
turtlebot_description 用来参考代码的，没有用\
20170318 cyr\
ur_gazebo/launch/testmoveit.launch moveit与gazebo的结合，在ur5hand_moveit_config中u5_moveit_planning_execution.launch无法用配置助手生成，关于srdf的载入有少量警告，move_group接口是否可以运用尚未得到验证

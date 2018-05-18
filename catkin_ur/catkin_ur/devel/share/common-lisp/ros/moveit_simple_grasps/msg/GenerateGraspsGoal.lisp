; Auto-generated. Do not edit!


(cl:in-package moveit_simple_grasps-msg)


;//! \htmlinclude GenerateGraspsGoal.msg.html

(cl:defclass <GenerateGraspsGoal> (roslisp-msg-protocol:ros-message)
  ((pose
    :reader pose
    :initarg :pose
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose))
   (width
    :reader width
    :initarg :width
    :type cl:float
    :initform 0.0)
   (options
    :reader options
    :initarg :options
    :type (cl:vector moveit_simple_grasps-msg:GraspGeneratorOptions)
   :initform (cl:make-array 0 :element-type 'moveit_simple_grasps-msg:GraspGeneratorOptions :initial-element (cl:make-instance 'moveit_simple_grasps-msg:GraspGeneratorOptions))))
)

(cl:defclass GenerateGraspsGoal (<GenerateGraspsGoal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GenerateGraspsGoal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GenerateGraspsGoal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name moveit_simple_grasps-msg:<GenerateGraspsGoal> is deprecated: use moveit_simple_grasps-msg:GenerateGraspsGoal instead.")))

(cl:ensure-generic-function 'pose-val :lambda-list '(m))
(cl:defmethod pose-val ((m <GenerateGraspsGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader moveit_simple_grasps-msg:pose-val is deprecated.  Use moveit_simple_grasps-msg:pose instead.")
  (pose m))

(cl:ensure-generic-function 'width-val :lambda-list '(m))
(cl:defmethod width-val ((m <GenerateGraspsGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader moveit_simple_grasps-msg:width-val is deprecated.  Use moveit_simple_grasps-msg:width instead.")
  (width m))

(cl:ensure-generic-function 'options-val :lambda-list '(m))
(cl:defmethod options-val ((m <GenerateGraspsGoal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader moveit_simple_grasps-msg:options-val is deprecated.  Use moveit_simple_grasps-msg:options instead.")
  (options m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GenerateGraspsGoal>) ostream)
  "Serializes a message object of type '<GenerateGraspsGoal>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'pose) ostream)
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'width))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((__ros_arr_len (cl:length (cl:slot-value msg 'options))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_arr_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_arr_len) ostream))
  (cl:map cl:nil #'(cl:lambda (ele) (roslisp-msg-protocol:serialize ele ostream))
   (cl:slot-value msg 'options))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GenerateGraspsGoal>) istream)
  "Deserializes a message object of type '<GenerateGraspsGoal>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'pose) istream)
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'width) (roslisp-utils:decode-double-float-bits bits)))
  (cl:let ((__ros_arr_len 0))
    (cl:setf (cl:ldb (cl:byte 8 0) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 8) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 16) __ros_arr_len) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 24) __ros_arr_len) (cl:read-byte istream))
  (cl:setf (cl:slot-value msg 'options) (cl:make-array __ros_arr_len))
  (cl:let ((vals (cl:slot-value msg 'options)))
    (cl:dotimes (i __ros_arr_len)
    (cl:setf (cl:aref vals i) (cl:make-instance 'moveit_simple_grasps-msg:GraspGeneratorOptions))
  (roslisp-msg-protocol:deserialize (cl:aref vals i) istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GenerateGraspsGoal>)))
  "Returns string type for a message object of type '<GenerateGraspsGoal>"
  "moveit_simple_grasps/GenerateGraspsGoal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GenerateGraspsGoal)))
  "Returns string type for a message object of type 'GenerateGraspsGoal"
  "moveit_simple_grasps/GenerateGraspsGoal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GenerateGraspsGoal>)))
  "Returns md5sum for a message object of type '<GenerateGraspsGoal>"
  "162875df5b62e9fb4be6d2aa5a67176d")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GenerateGraspsGoal)))
  "Returns md5sum for a message object of type 'GenerateGraspsGoal"
  "162875df5b62e9fb4be6d2aa5a67176d")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GenerateGraspsGoal>)))
  "Returns full string definition for message of type '<GenerateGraspsGoal>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal~%geometry_msgs/Pose pose~%float64 width~%moveit_simple_grasps/GraspGeneratorOptions[] options~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: moveit_simple_grasps/GraspGeneratorOptions~%uint8 grasp_axis~%uint8 GRASP_AXIS_X = 0~%uint8 GRASP_AXIS_Y = 1~%uint8 GRASP_AXIS_Z = 2~%~%uint8 grasp_direction~%uint8 GRASP_DIRECTION_UP = 0~%uint8 GRASP_DIRECTION_DOWN = 1~%~%uint8 grasp_rotation~%uint8 GRASP_ROTATION_HALF = 0~%uint8 GRASP_ROTATION_FULL = 1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GenerateGraspsGoal)))
  "Returns full string definition for message of type 'GenerateGraspsGoal"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal~%geometry_msgs/Pose pose~%float64 width~%moveit_simple_grasps/GraspGeneratorOptions[] options~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: moveit_simple_grasps/GraspGeneratorOptions~%uint8 grasp_axis~%uint8 GRASP_AXIS_X = 0~%uint8 GRASP_AXIS_Y = 1~%uint8 GRASP_AXIS_Z = 2~%~%uint8 grasp_direction~%uint8 GRASP_DIRECTION_UP = 0~%uint8 GRASP_DIRECTION_DOWN = 1~%~%uint8 grasp_rotation~%uint8 GRASP_ROTATION_HALF = 0~%uint8 GRASP_ROTATION_FULL = 1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GenerateGraspsGoal>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'pose))
     8
     4 (cl:reduce #'cl:+ (cl:slot-value msg 'options) :key #'(cl:lambda (ele) (cl:declare (cl:ignorable ele)) (cl:+ (roslisp-msg-protocol:serialization-length ele))))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GenerateGraspsGoal>))
  "Converts a ROS message object to a list"
  (cl:list 'GenerateGraspsGoal
    (cl:cons ':pose (pose msg))
    (cl:cons ':width (width msg))
    (cl:cons ':options (options msg))
))

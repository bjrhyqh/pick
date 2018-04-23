; Auto-generated. Do not edit!


(cl:in-package moveit_simple_grasps-msg)


;//! \htmlinclude GraspGeneratorOptions.msg.html

(cl:defclass <GraspGeneratorOptions> (roslisp-msg-protocol:ros-message)
  ((grasp_axis
    :reader grasp_axis
    :initarg :grasp_axis
    :type cl:fixnum
    :initform 0)
   (grasp_direction
    :reader grasp_direction
    :initarg :grasp_direction
    :type cl:fixnum
    :initform 0)
   (grasp_rotation
    :reader grasp_rotation
    :initarg :grasp_rotation
    :type cl:fixnum
    :initform 0))
)

(cl:defclass GraspGeneratorOptions (<GraspGeneratorOptions>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <GraspGeneratorOptions>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'GraspGeneratorOptions)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name moveit_simple_grasps-msg:<GraspGeneratorOptions> is deprecated: use moveit_simple_grasps-msg:GraspGeneratorOptions instead.")))

(cl:ensure-generic-function 'grasp_axis-val :lambda-list '(m))
(cl:defmethod grasp_axis-val ((m <GraspGeneratorOptions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader moveit_simple_grasps-msg:grasp_axis-val is deprecated.  Use moveit_simple_grasps-msg:grasp_axis instead.")
  (grasp_axis m))

(cl:ensure-generic-function 'grasp_direction-val :lambda-list '(m))
(cl:defmethod grasp_direction-val ((m <GraspGeneratorOptions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader moveit_simple_grasps-msg:grasp_direction-val is deprecated.  Use moveit_simple_grasps-msg:grasp_direction instead.")
  (grasp_direction m))

(cl:ensure-generic-function 'grasp_rotation-val :lambda-list '(m))
(cl:defmethod grasp_rotation-val ((m <GraspGeneratorOptions>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader moveit_simple_grasps-msg:grasp_rotation-val is deprecated.  Use moveit_simple_grasps-msg:grasp_rotation instead.")
  (grasp_rotation m))
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql '<GraspGeneratorOptions>)))
    "Constants for message type '<GraspGeneratorOptions>"
  '((:GRASP_AXIS_X . 0)
    (:GRASP_AXIS_Y . 1)
    (:GRASP_AXIS_Z . 2)
    (:GRASP_DIRECTION_UP . 0)
    (:GRASP_DIRECTION_DOWN . 1)
    (:GRASP_ROTATION_HALF . 0)
    (:GRASP_ROTATION_FULL . 1))
)
(cl:defmethod roslisp-msg-protocol:symbol-codes ((msg-type (cl:eql 'GraspGeneratorOptions)))
    "Constants for message type 'GraspGeneratorOptions"
  '((:GRASP_AXIS_X . 0)
    (:GRASP_AXIS_Y . 1)
    (:GRASP_AXIS_Z . 2)
    (:GRASP_DIRECTION_UP . 0)
    (:GRASP_DIRECTION_DOWN . 1)
    (:GRASP_ROTATION_HALF . 0)
    (:GRASP_ROTATION_FULL . 1))
)
(cl:defmethod roslisp-msg-protocol:serialize ((msg <GraspGeneratorOptions>) ostream)
  "Serializes a message object of type '<GraspGeneratorOptions>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasp_axis)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasp_direction)) ostream)
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasp_rotation)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <GraspGeneratorOptions>) istream)
  "Deserializes a message object of type '<GraspGeneratorOptions>"
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasp_axis)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasp_direction)) (cl:read-byte istream))
    (cl:setf (cl:ldb (cl:byte 8 0) (cl:slot-value msg 'grasp_rotation)) (cl:read-byte istream))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<GraspGeneratorOptions>)))
  "Returns string type for a message object of type '<GraspGeneratorOptions>"
  "moveit_simple_grasps/GraspGeneratorOptions")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'GraspGeneratorOptions)))
  "Returns string type for a message object of type 'GraspGeneratorOptions"
  "moveit_simple_grasps/GraspGeneratorOptions")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<GraspGeneratorOptions>)))
  "Returns md5sum for a message object of type '<GraspGeneratorOptions>"
  "99863eab001728611523218e2a9810a3")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'GraspGeneratorOptions)))
  "Returns md5sum for a message object of type 'GraspGeneratorOptions"
  "99863eab001728611523218e2a9810a3")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<GraspGeneratorOptions>)))
  "Returns full string definition for message of type '<GraspGeneratorOptions>"
  (cl:format cl:nil "uint8 grasp_axis~%uint8 GRASP_AXIS_X = 0~%uint8 GRASP_AXIS_Y = 1~%uint8 GRASP_AXIS_Z = 2~%~%uint8 grasp_direction~%uint8 GRASP_DIRECTION_UP = 0~%uint8 GRASP_DIRECTION_DOWN = 1~%~%uint8 grasp_rotation~%uint8 GRASP_ROTATION_HALF = 0~%uint8 GRASP_ROTATION_FULL = 1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'GraspGeneratorOptions)))
  "Returns full string definition for message of type 'GraspGeneratorOptions"
  (cl:format cl:nil "uint8 grasp_axis~%uint8 GRASP_AXIS_X = 0~%uint8 GRASP_AXIS_Y = 1~%uint8 GRASP_AXIS_Z = 2~%~%uint8 grasp_direction~%uint8 GRASP_DIRECTION_UP = 0~%uint8 GRASP_DIRECTION_DOWN = 1~%~%uint8 grasp_rotation~%uint8 GRASP_ROTATION_HALF = 0~%uint8 GRASP_ROTATION_FULL = 1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <GraspGeneratorOptions>))
  (cl:+ 0
     1
     1
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <GraspGeneratorOptions>))
  "Converts a ROS message object to a list"
  (cl:list 'GraspGeneratorOptions
    (cl:cons ':grasp_axis (grasp_axis msg))
    (cl:cons ':grasp_direction (grasp_direction msg))
    (cl:cons ':grasp_rotation (grasp_rotation msg))
))

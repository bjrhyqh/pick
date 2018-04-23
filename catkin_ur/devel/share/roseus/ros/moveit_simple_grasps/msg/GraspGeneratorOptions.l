;; Auto-generated. Do not edit!


(when (boundp 'moveit_simple_grasps::GraspGeneratorOptions)
  (if (not (find-package "MOVEIT_SIMPLE_GRASPS"))
    (make-package "MOVEIT_SIMPLE_GRASPS"))
  (shadow 'GraspGeneratorOptions (find-package "MOVEIT_SIMPLE_GRASPS")))
(unless (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS")
  (make-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))

(in-package "ROS")
;;//! \htmlinclude GraspGeneratorOptions.msg.html


(intern "*GRASP_AXIS_X*" (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(shadow '*GRASP_AXIS_X* (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(defconstant moveit_simple_grasps::GraspGeneratorOptions::*GRASP_AXIS_X* 0)
(intern "*GRASP_AXIS_Y*" (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(shadow '*GRASP_AXIS_Y* (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(defconstant moveit_simple_grasps::GraspGeneratorOptions::*GRASP_AXIS_Y* 1)
(intern "*GRASP_AXIS_Z*" (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(shadow '*GRASP_AXIS_Z* (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(defconstant moveit_simple_grasps::GraspGeneratorOptions::*GRASP_AXIS_Z* 2)
(intern "*GRASP_DIRECTION_UP*" (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(shadow '*GRASP_DIRECTION_UP* (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(defconstant moveit_simple_grasps::GraspGeneratorOptions::*GRASP_DIRECTION_UP* 0)
(intern "*GRASP_DIRECTION_DOWN*" (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(shadow '*GRASP_DIRECTION_DOWN* (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(defconstant moveit_simple_grasps::GraspGeneratorOptions::*GRASP_DIRECTION_DOWN* 1)
(intern "*GRASP_ROTATION_HALF*" (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(shadow '*GRASP_ROTATION_HALF* (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(defconstant moveit_simple_grasps::GraspGeneratorOptions::*GRASP_ROTATION_HALF* 0)
(intern "*GRASP_ROTATION_FULL*" (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(shadow '*GRASP_ROTATION_FULL* (find-package "MOVEIT_SIMPLE_GRASPS::GRASPGENERATOROPTIONS"))
(defconstant moveit_simple_grasps::GraspGeneratorOptions::*GRASP_ROTATION_FULL* 1)
(defclass moveit_simple_grasps::GraspGeneratorOptions
  :super ros::object
  :slots (_grasp_axis _grasp_direction _grasp_rotation ))

(defmethod moveit_simple_grasps::GraspGeneratorOptions
  (:init
   (&key
    ((:grasp_axis __grasp_axis) 0)
    ((:grasp_direction __grasp_direction) 0)
    ((:grasp_rotation __grasp_rotation) 0)
    )
   (send-super :init)
   (setq _grasp_axis (round __grasp_axis))
   (setq _grasp_direction (round __grasp_direction))
   (setq _grasp_rotation (round __grasp_rotation))
   self)
  (:grasp_axis
   (&optional __grasp_axis)
   (if __grasp_axis (setq _grasp_axis __grasp_axis)) _grasp_axis)
  (:grasp_direction
   (&optional __grasp_direction)
   (if __grasp_direction (setq _grasp_direction __grasp_direction)) _grasp_direction)
  (:grasp_rotation
   (&optional __grasp_rotation)
   (if __grasp_rotation (setq _grasp_rotation __grasp_rotation)) _grasp_rotation)
  (:serialization-length
   ()
   (+
    ;; uint8 _grasp_axis
    1
    ;; uint8 _grasp_direction
    1
    ;; uint8 _grasp_rotation
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _grasp_axis
       (write-byte _grasp_axis s)
     ;; uint8 _grasp_direction
       (write-byte _grasp_direction s)
     ;; uint8 _grasp_rotation
       (write-byte _grasp_rotation s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _grasp_axis
     (setq _grasp_axis (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _grasp_direction
     (setq _grasp_direction (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _grasp_rotation
     (setq _grasp_rotation (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get moveit_simple_grasps::GraspGeneratorOptions :md5sum-) "99863eab001728611523218e2a9810a3")
(setf (get moveit_simple_grasps::GraspGeneratorOptions :datatype-) "moveit_simple_grasps/GraspGeneratorOptions")
(setf (get moveit_simple_grasps::GraspGeneratorOptions :definition-)
      "uint8 grasp_axis
uint8 GRASP_AXIS_X = 0
uint8 GRASP_AXIS_Y = 1
uint8 GRASP_AXIS_Z = 2

uint8 grasp_direction
uint8 GRASP_DIRECTION_UP = 0
uint8 GRASP_DIRECTION_DOWN = 1

uint8 grasp_rotation
uint8 GRASP_ROTATION_HALF = 0
uint8 GRASP_ROTATION_FULL = 1

")



(provide :moveit_simple_grasps/GraspGeneratorOptions "99863eab001728611523218e2a9810a3")



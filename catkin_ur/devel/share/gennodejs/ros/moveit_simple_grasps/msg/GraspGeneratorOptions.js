// Auto-generated. Do not edit!

// (in-package moveit_simple_grasps.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class GraspGeneratorOptions {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.grasp_axis = null;
      this.grasp_direction = null;
      this.grasp_rotation = null;
    }
    else {
      if (initObj.hasOwnProperty('grasp_axis')) {
        this.grasp_axis = initObj.grasp_axis
      }
      else {
        this.grasp_axis = 0;
      }
      if (initObj.hasOwnProperty('grasp_direction')) {
        this.grasp_direction = initObj.grasp_direction
      }
      else {
        this.grasp_direction = 0;
      }
      if (initObj.hasOwnProperty('grasp_rotation')) {
        this.grasp_rotation = initObj.grasp_rotation
      }
      else {
        this.grasp_rotation = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type GraspGeneratorOptions
    // Serialize message field [grasp_axis]
    bufferOffset = _serializer.uint8(obj.grasp_axis, buffer, bufferOffset);
    // Serialize message field [grasp_direction]
    bufferOffset = _serializer.uint8(obj.grasp_direction, buffer, bufferOffset);
    // Serialize message field [grasp_rotation]
    bufferOffset = _serializer.uint8(obj.grasp_rotation, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type GraspGeneratorOptions
    let len;
    let data = new GraspGeneratorOptions(null);
    // Deserialize message field [grasp_axis]
    data.grasp_axis = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [grasp_direction]
    data.grasp_direction = _deserializer.uint8(buffer, bufferOffset);
    // Deserialize message field [grasp_rotation]
    data.grasp_rotation = _deserializer.uint8(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 3;
  }

  static datatype() {
    // Returns string type for a message object
    return 'moveit_simple_grasps/GraspGeneratorOptions';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '99863eab001728611523218e2a9810a3';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    uint8 grasp_axis
    uint8 GRASP_AXIS_X = 0
    uint8 GRASP_AXIS_Y = 1
    uint8 GRASP_AXIS_Z = 2
    
    uint8 grasp_direction
    uint8 GRASP_DIRECTION_UP = 0
    uint8 GRASP_DIRECTION_DOWN = 1
    
    uint8 grasp_rotation
    uint8 GRASP_ROTATION_HALF = 0
    uint8 GRASP_ROTATION_FULL = 1
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new GraspGeneratorOptions(null);
    if (msg.grasp_axis !== undefined) {
      resolved.grasp_axis = msg.grasp_axis;
    }
    else {
      resolved.grasp_axis = 0
    }

    if (msg.grasp_direction !== undefined) {
      resolved.grasp_direction = msg.grasp_direction;
    }
    else {
      resolved.grasp_direction = 0
    }

    if (msg.grasp_rotation !== undefined) {
      resolved.grasp_rotation = msg.grasp_rotation;
    }
    else {
      resolved.grasp_rotation = 0
    }

    return resolved;
    }
};

// Constants for message
GraspGeneratorOptions.Constants = {
  GRASP_AXIS_X: 0,
  GRASP_AXIS_Y: 1,
  GRASP_AXIS_Z: 2,
  GRASP_DIRECTION_UP: 0,
  GRASP_DIRECTION_DOWN: 1,
  GRASP_ROTATION_HALF: 0,
  GRASP_ROTATION_FULL: 1,
}

module.exports = GraspGeneratorOptions;

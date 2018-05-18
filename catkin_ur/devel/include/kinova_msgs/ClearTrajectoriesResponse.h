// Generated by gencpp from file kinova_msgs/ClearTrajectoriesResponse.msg
// DO NOT EDIT!


#ifndef KINOVA_MSGS_MESSAGE_CLEARTRAJECTORIESRESPONSE_H
#define KINOVA_MSGS_MESSAGE_CLEARTRAJECTORIESRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace kinova_msgs
{
template <class ContainerAllocator>
struct ClearTrajectoriesResponse_
{
  typedef ClearTrajectoriesResponse_<ContainerAllocator> Type;

  ClearTrajectoriesResponse_()
    : result()  {
    }
  ClearTrajectoriesResponse_(const ContainerAllocator& _alloc)
    : result(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _result_type;
  _result_type result;




  typedef boost::shared_ptr< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> const> ConstPtr;

}; // struct ClearTrajectoriesResponse_

typedef ::kinova_msgs::ClearTrajectoriesResponse_<std::allocator<void> > ClearTrajectoriesResponse;

typedef boost::shared_ptr< ::kinova_msgs::ClearTrajectoriesResponse > ClearTrajectoriesResponsePtr;
typedef boost::shared_ptr< ::kinova_msgs::ClearTrajectoriesResponse const> ClearTrajectoriesResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace kinova_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'kinova_msgs': ['/home/cyr/catkin_ur/src/kinova-ros-master/kinova_msgs/msg', '/home/cyr/catkin_ur/devel/share/kinova_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "c22f2a1ed8654a0b365f1bb3f7ff2c0f";
  }

  static const char* value(const ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xc22f2a1ed8654a0bULL;
  static const uint64_t static_value2 = 0x365f1bb3f7ff2c0fULL;
};

template<class ContainerAllocator>
struct DataType< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "kinova_msgs/ClearTrajectoriesResponse";
  }

  static const char* value(const ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string result\n\
\n\
";
  }

  static const char* value(const ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.result);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ClearTrajectoriesResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::kinova_msgs::ClearTrajectoriesResponse_<ContainerAllocator>& v)
  {
    s << indent << "result: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.result);
  }
};

} // namespace message_operations
} // namespace ros

#endif // KINOVA_MSGS_MESSAGE_CLEARTRAJECTORIESRESPONSE_H

#include<ros/ros.h> //ros标准库头文件
#include<iostream> //C++标准输入输出库
/*
  cv_bridge中包含CvBridge库
*/
#include<cv_bridge/cv_bridge.h>
/*
  ROS图象类型的编码函数
*/
#include<sensor_msgs/image_encodings.h>
/*
   image_transport 头文件用来在ROS系统中的话题上发布和订阅图象消息
*/
#include<image_transport/image_transport.h>

//OpenCV2标准头文件
#include<cv.h>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc/imgproc.hpp>
#include <myinclude/orb.h>
#include <boost/thread.hpp>
#include <vector>

static const std::string INPUT1 = "Input1"; //定义输入窗口名称
static const std::string INPUT2 = "Input2"; //定义输入窗口名称
static const std::string OUTPUT = "Output"; //定义输出窗口名称

//定义一个转换的类
class RGB_GRAY
{
private:
    ros::NodeHandle nh_; //定义ROS句柄
    image_transport::ImageTransport it_; //定义一个image_transport实例
    image_transport::Subscriber image_sub_left; //定义ROS图象接收器
    image_transport::Subscriber image_sub_right; //定义ROS图象接收器
//    image_transport::Publisher image_pub_; //定义ROS图象发布器
    cv::Mat left;
    cv::Mat right;
    bool receive;
public:
    RGB_GRAY()
      :it_(nh_) //构造函数
    {
        image_sub_left = it_.subscribe("double_camera/narrow_stereo/left/image_raw", 1, &RGB_GRAY::convert_callback1, this); //定义图象接受器，订阅话题是“camera/rgb/image_raw”
        image_sub_right = it_.subscribe("double_camera/narrow_stereo/right/image_raw", 1, &RGB_GRAY::convert_callback2, this);
        //初始化输入输出窗口
        cv::namedWindow(INPUT1);
         cv::namedWindow(INPUT2);
        cv::namedWindow(OUTPUT);
//        sad(left,right);
    }
    ~RGB_GRAY() //析构函数
    {
         cv::destroyWindow(INPUT1);
         cv:destroyWindow(INPUT2);
//         cv::destroyWindow(OUTPUT);
    }
    /*
      这是一个ROS和OpenCV的格式转换回调函数，将图象格式从sensor_msgs/Image  --->  cv::Mat
    */
    void convert_callback1(const sensor_msgs::ImageConstPtr& msg)
    {
        cv_bridge::CvImagePtr cv_ptr; // 声明一个CvImage指针的实例

        try
        {
            cv_ptr =  cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::RGB8); //将ROS消息中的图象信息提取，生成新cv类型的图象，复制给CvImage指针
        }
        catch(cv_bridge::Exception& e)  //异常处理
        {
            ROS_ERROR("cv_bridge exception: %s", e.what());
            return;
        }

        image_process1(cv_ptr->image); //得到了cv::Mat类型的图象，在CvImage指针的image中，将结果传送给处理函数
    }
    /*
       这是图象处理的主要函数，一般会把图像处理的主要程序写在这个函数中。这里的例子只是一个彩色图象到灰度图象的转化
    */
    void image_process1(cv::Mat img1)
    {
       cv::Mat img_out1;
       img1=convert_cut(img1);
       cv::cvtColor(img1, img_out1, CV_RGB2GRAY);  //转换成灰度图象
       left=img1;
       receive=true;
       cv::imshow(INPUT1, img_out1);
//       cv::imshow(OUTPUT, img_out);
       cv::waitKey(5);
    }
    //这是一个ROS和OpenCV的格式转换回调函数，将图象格式从sensor_msgs/Image  --->  cv::Mat
 // */
  void convert_callback2(const sensor_msgs::ImageConstPtr& msg)
  {
      cv_bridge::CvImagePtr cv_ptr; // 声明一个CvImage指针的实例

      try
      {
          cv_ptr =  cv_bridge::toCvCopy(msg, sensor_msgs::image_encodings::RGB8); //将ROS消息中的图象信息提取，生成新cv类型的图象，复制给CvImage指针
      }
      catch(cv_bridge::Exception& e)  //异常处理
      {
          ROS_ERROR("cv_bridge exception: %s", e.what());
          return;
      }

      image_process2(cv_ptr->image); //得到了cv::Mat类型的图象，在CvImage指针的image中，将结果传送给处理函数
  }
  /*
     这是图象处理的主要函数，一般会把图像处理的主要程序写在这个函数中。这里的例子只是一个彩色图象到灰度图象的转化
  */
  void image_process2(cv::Mat img2)
  {
     cv::Mat img_out2;
     img2=convert_cut(img2);
     cv::cvtColor(img2, img_out2, CV_RGB2GRAY);  //转换成灰度图象
     if(receive==true){
     right=img2;
       cv::imshow(INPUT2, img_out2);
//       cv::imshow(OUTPUT, img_out);
     cv::waitKey(5);
     cv::Mat matchMat=cacORBFeatureAndCompare(left,right);
//     vector<Point3f> matchMat=cacORB(left,right);
//     int sizep=matchMat.size();
//     for(int i=0;i<sizep;i++){
//       cout<<matchMat[i].x<<','<<matchMat[i].y<<','<<matchMat[i].z<<endl;
//     }
//     matchMat.clear();
     cv::imshow("matchMat",matchMat);
     }
     receive=false;

  }

  cv::Mat convert_cut(cv::Mat img){
     Vec3f tdata=img.at<Vec3f>(50,600);
     Vec3f *pxvec=img.ptr<Vec3f>(0);
     int i,j;
     for(i=0;i<img.rows;i++){
       pxvec=img.ptr<Vec3f>(i);
       for(j=0;j<25;j++){
         pxvec[j]=tdata;
       }
     }
     cv::waitKey(10);
     return img;
  }
};

//主函数
int main(int argc, char** argv)
{
    ros::init(argc, argv, "grayImage");
    RGB_GRAY obj;
    ros::MultiThreadedSpinner spinner(2);  //多线程
    ros::spin();
}

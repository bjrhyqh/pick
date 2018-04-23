//#include <myinclude/surffandc.h>
#include<vector>
#include<iostream> //C++标准输入输出库
#include<cv.h>
#include <opencv2/opencv.hpp>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc/imgproc.hpp>
#include <opencv2/features2d/features2d.hpp>
#include <myinclude/orb.h>
#include<ros/ros.h>
using namespace std;
using namespace cv;

//cv::Mat cacORBFeatureAndCompare(cv::Mat srcImage1,cv::Mat srcImage2)
//{
//  CV_Assert(srcImage1.data != NULL && srcImage2.data != NULL);
//  vector<KeyPoint> keyPoint1,keyPoint2;
//  Ptr<ORB> orb = ORB::create();
//  orb->detect(srcImage1,keyPoint1);
//  orb->detect(srcImage2,keyPoint2);
//  Mat descriptorMat1,descriptorMat2;
//  orb->compute(srcImage1,keyPoint1,descriptorMat1);
//  orb->compute(srcImage2,keyPoint2,descriptorMat2);
//  BFMatcher matcher(NORM_HAMMING);
//  vector<DMatch> matches;
//  matcher.match(descriptorMat1,descriptorMat2,matches);
//  Mat matchMat;
//  drawMatches(srcImage1,keyPoint1,srcImage2,keyPoint2,matches,matchMat);
//  cv::imshow("Matches",matchMat);
//  return matchMat;
//}
int main()
{
    Mat Img_L=imread("/home/cyr/图片/Input1.png",1);
    Mat img=Img_L;
//    Mat Img_R=imread("/home/cyr/图片/Input2.png",1);
    imshow("input",img);
    waitKey(1000);
    Vec3f tdata=img.at<Vec3f>(50,600);
    cout<<tdata[0]<<','<<tdata[1]<<','<<tdata[2]<<endl;
    cout<<img.cols<<endl;
    Vec3f *pxvec=img.ptr<Vec3f>(0);
    int i,j;
    for(i=0;i<img.rows;i++){
      pxvec=img.ptr<Vec3f>(i);
      for(j=0;j<10;j++){
        pxvec[j]=tdata;
      }
    }
    imshow("out",img);
    waitKey(10000);
}


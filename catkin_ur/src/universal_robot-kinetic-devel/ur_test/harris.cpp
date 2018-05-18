#include<vector>
#include<iostream> //C++标准输入输出库
#include<cv.h>
#include <opencv2/opencv.hpp>
#include<opencv2/core/core.hpp>
#include<opencv2/highgui/highgui.hpp>
#include<opencv2/imgproc/imgproc.hpp>
#include <opencv2/features2d/features2d.hpp>
#include<ros/ros.h>
using namespace std;
using namespace cv;
int main()
{
    Mat Img_L=imread("/home/cyr/图片/Input2.png",1);
    Mat img=Img_L;
//    Mat Img_R=imread("/home/cyr/图片/Input2.png",1);
    imshow("input",img);
    cvtColor(img,img,CV_BGR2GRAY);
    waitKey(1000);
    Mat cornerstrength;
    cornerHarris(img,cornerstrength,2,3,0.01);
    cout<<"harris get";
    Mat harriscorners;
    double thres=0.001;
    threshold(cornerstrength,harriscorners,thres,255,cv::THRESH_BINARY);
    imshow("harris",harriscorners);
    waitKey(10000);
}

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
    Mat Img_R=imread("/home/cyr/图片/Input2.png",1);
    vector<Point3f>  matchMat;
    matchMat=cacORB(Img_L,Img_R);
//    vector<Point3f> matchMat;
//    float matchRate= cacSURFFeatureAndCompare(Img_L,Img_R,1000);
//    std::cout <<"matchRate:"<<matchRate<<std::endl;
//    cv::imshow(matchMat);
    int sizep=matchMat.size();
    cout<<sizep<<endl;
    for(int i=0;i<sizep;i++){
      cout<<matchMat[i].x<<','<<matchMat[i].y<<','<<matchMat[i].z<<endl;
    }
    matchMat.clear();
//    cv::waitKey(0);
    return 0;
}


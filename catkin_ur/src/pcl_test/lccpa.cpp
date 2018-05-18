#include <iostream>
//ROS
#include <ros/ros.h>
// PCL specific includes
#include <sensor_msgs/PointCloud2.h>
#include <pcl_conversions/pcl_conversions.h>
#include <pcl/conversions.h>
#include <pcl/point_cloud.h>
#include <pcl/point_types.h>
#include <pcl/io/pcd_io.h>
#include <stdlib.h>
#include <cmath>
#include <limits.h>
#include <boost/format.hpp>
#include <pcl/console/parse.h>
#include <pcl/io/pcd_io.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <pcl/visualization/point_cloud_color_handlers.h>
#include <pcl/filters/passthrough.h>
#include <pcl/segmentation/supervoxel_clustering.h>
#include <pcl/segmentation/lccp_segmentation.h>
#define Random(x) (rand() % x)

typedef pcl::PointXYZRGBA PointT;
typedef pcl::LCCPSegmentation<PointT>::SupervoxelAdjacencyList SuperVoxelAdjacencyList;

ros::Publisher pub;

void
cloud_cb (const sensor_msgs::PointCloud2ConstPtr& input)
{
  // 将点云格式为sensor_msgs/PointCloud2 格式转为 pcl/PointCloud
  pcl::PointCloud<PointT>::Ptr input_cloud_ptr(new pcl::PointCloud<PointT>);
  pcl::PCLPointCloud2 input_pointcloud2;
  pcl_conversions::toPCL(*input, input_pointcloud2);   //关键的一句数据的转换
  pcl::fromPCLPointCloud2(input_pointcloud2, *input_cloud_ptr);
  PCL_INFO("Done making cloud\n");

    //超体聚类 参数依次是粒子距离、晶核距离、颜色容差、
    float voxel_resolution = 0.0075f;
    float seed_resolution = 0.03f;
    float color_importance = 0.0f;
    float spatial_importance = 1.0f;
    float normal_importance = 4.0f;
    bool use_single_cam_transform = false;
    bool use_supervoxel_refinement = false;

    unsigned int k_factor = 0;

    //voxel_resolution is the resolution (in meters) of voxels used、seed_resolution is the average size (in meters) of resulting supervoxels
    pcl::SupervoxelClustering<PointT> super(voxel_resolution, seed_resolution);
//    super.setUseSingleCameraTransform(false);
    super.setInputCloud(input_cloud_ptr);
    //Set the importance of color for supervoxels.
    super.setColorImportance(color_importance);
    //Set the importance of spatial distance for supervoxels.
    super.setSpatialImportance(spatial_importance);
    //Set the importance of scalar normal product for supervoxels.
    super.setNormalImportance(normal_importance);
    std::map<uint32_t, pcl::Supervoxel<PointT>::Ptr> supervoxel_clusters;

    PCL_INFO("Extracting supervoxels\n");
    super.extract(supervoxel_clusters);

    PCL_INFO("Getting supervoxel adjacency\n");
    std::multimap<uint32_t, uint32_t> supervoxel_adjacency;
    super.getSupervoxelAdjacency(supervoxel_adjacency);
    pcl::PointCloud<pcl::PointXYZL>::Ptr overseg = super.getLabeledCloud();
        ofstream outFile1("guofenge3.txt", std::ios_base::out);
        for (int i = 0; i < overseg->size(); i++) {
            outFile1 << overseg->points[i].x << "\t" << overseg->points[i].y << "\t" << overseg->points[i].z << "\t" << overseg->points[i].label << endl;
        }
        int label_max1 = 0;
        for (int i = 0;i< overseg->size(); i++) {
            if (overseg->points[i].label>label_max1)
                label_max1 = overseg->points[i].label;
        }
        pcl::PointCloud<pcl::PointXYZRGB>::Ptr ColoredCloud1(new pcl::PointCloud<pcl::PointXYZRGB>);
        ColoredCloud1->height = 1;
        ColoredCloud1->width = overseg->size();
        ColoredCloud1->resize(overseg->size());
        for (int i = 0; i < label_max1; i++) {
            int color_R = Random(255);
            int color_G = Random(255);
            int color_B = Random(255);

            for (int j = 0; j < overseg->size(); j++) {
                if (overseg->points[j].label == i) {
                    ColoredCloud1->points[j].x = overseg->points[j].x;
                    ColoredCloud1->points[j].y = overseg->points[j].y;
                    ColoredCloud1->points[j].z = overseg->points[j].z;
                    ColoredCloud1->points[j].r = color_R;
                    ColoredCloud1->points[j].g = color_G;
                    ColoredCloud1->points[j].b = color_B;
                }
            }
        }
        pcl::io::savePCDFileASCII("guofenge3.pcd", *ColoredCloud1);

    //LCCP分割
    float concavity_tolerance_threshold = 10;
    float smoothness_threshold = 0.1;
    uint32_t min_segment_size = 0;
    bool use_extended_convexity = false;
    bool use_sanity_criterion = false;
    PCL_INFO("Starting Segmentation\n");
    pcl::LCCPSegmentation<PointT> lccp;
    lccp.setConcavityToleranceThreshold(concavity_tolerance_threshold);
    lccp.setSmoothnessCheck(true, voxel_resolution, seed_resolution, smoothness_threshold);
    lccp.setKFactor(k_factor);
    lccp.setInputSupervoxels(supervoxel_clusters, supervoxel_adjacency);
    lccp.setMinSegmentSize(min_segment_size);
    lccp.segment();

    PCL_INFO("Interpolation voxel cloud -> input cloud and relabeling\n");

    pcl::PointCloud<pcl::PointXYZL>::Ptr sv_labeled_cloud = super.getLabeledCloud();
    pcl::PointCloud<pcl::PointXYZL>::Ptr lccp_labeled_cloud = sv_labeled_cloud->makeShared();
    lccp.relabelCloud(*lccp_labeled_cloud);
    SuperVoxelAdjacencyList sv_adjacency_list;
    lccp.getSVAdjacencyList(sv_adjacency_list);
  // 把提取出来的分割发布出去
    ofstream outFile2("fenge3.txt", std::ios_base::out);
        for (int i = 0; i < lccp_labeled_cloud->size();i++) {
            outFile2 << lccp_labeled_cloud->points[i].x << "\t" << lccp_labeled_cloud->points[i].y << "\t" << lccp_labeled_cloud->points[i].z << "\t" << lccp_labeled_cloud->points[i].label << endl;
        }

        int label_max2 = 0;
        for (int i = 0; i< lccp_labeled_cloud->size(); i++) {
            if (lccp_labeled_cloud->points[i].label>label_max2)
                label_max2 = lccp_labeled_cloud->points[i].label;
        }
        pcl::PointCloud<pcl::PointXYZRGB>::Ptr ColoredCloud2(new pcl::PointCloud<pcl::PointXYZRGB>);
        ColoredCloud2->height = 1;
        ColoredCloud2->width = lccp_labeled_cloud->size();
        ColoredCloud2->resize(lccp_labeled_cloud->size());
        for (int i = 0; i < label_max2; i++) {
            int color_R = Random(255);
            int color_G = Random(255);
            int color_B = Random(255);

            for (int j = 0; j < lccp_labeled_cloud->size(); j++) {
                if (lccp_labeled_cloud->points[j].label == i) {
                    ColoredCloud2->points[j].x = lccp_labeled_cloud->points[j].x;
                    ColoredCloud2->points[j].y = lccp_labeled_cloud->points[j].y;
                    ColoredCloud2->points[j].z = lccp_labeled_cloud->points[j].z;
                    ColoredCloud2->points[j].r = color_R;
                    ColoredCloud2->points[j].g = color_G;
                    ColoredCloud2->points[j].b = color_B;
                }
            }
        }
        pcl::io::savePCDFileASCII("fenge3.pcd", *ColoredCloud2);
}

int main (int argc, char** argv)
{
  // Initialize ROS
  ros::init (argc, argv, "my_pcl_tutorial");
  ros::NodeHandle nh;

  // Create a ROS subscriber for the input point cloud
  ros::Subscriber sub = nh.subscribe ("/head_mount_kinect/depth_registered/points", 1, cloud_cb);

  // Create a ROS publisher for the output model coefficients
//   pub = nh.advertise<sensor_msgs::PointCloud2> ("output", 1);

  // Spin
  ros::Rate loop_rate(5);
      while (ros::ok())
      {
          /*...TODO...*/

          ros::spinOnce();
          loop_rate.sleep();
      }
      return 0;
}

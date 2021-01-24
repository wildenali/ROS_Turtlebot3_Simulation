#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2 as pc2
from sensor_msgs.msg import LaserScan
from laser_geometry import LaserProjection

class LaserToPointCloud():
    def __init__(self):
        self.laserProj = LaserProjection()
        self.pcPub = rospy.Publisher("/laser_point_cloud", pc2, queue_size=1)
        self.laserSub = rospy.Subscriber("/scan", LaserScan, self.laserCallBack)
 
    def laserCallBack(self, data):
        cloud_out = self.laserProj.projectLaser(data)
        self.pcPub.publish(cloud_out)

if __name__ == '__main__':
     rospy.init_node("laserToPointCloud")
     laserToPointCloud = LaserToPointCloud()
     rospy.spin()
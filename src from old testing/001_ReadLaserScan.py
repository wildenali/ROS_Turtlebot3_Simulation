#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    print("range[0]  : ", msg.ranges[0])
    print("range[360]: ", msg.ranges[360])
    print("range[719]: ", msg.ranges[719])
 
    
if __name__ == '__main__':
    rospy.init_node("read_laser_scan_node")
    sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
    rospy.spin()
    # cek
#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

def callback(msg):
    # print(msg.header.seq)
    # print(msg.header.stamp)
    # print(msg.header.stamp.secs)
    # print(msg.header.stamp.nsecs)
    # print(msg.header.frame_id)
    # print(msg.angle_min)
    # print(msg.angle_max)
    # print(msg.angle_increment)
    # print(msg.time_increment)
    # print(msg.scan_time)
    # print(msg.range_min)
    # print(msg.range_max)

    # print(msg.ranges[0])
    print("range[0]  : %.4f" % msg.ranges[0])
    print("range[90] : %.4f" % msg.ranges[90])
    print("range[180]: %.4f" % msg.ranges[179])     # max 179
 
    
if __name__ == '__main__':
    rospy.init_node("read_laser_scan_node")
    sub = rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

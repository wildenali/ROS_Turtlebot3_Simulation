#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan

distance = 0.0


def callback(msg):
    global distance
    distance = msg.ranges[0]


rospy.init_node("read_laser_scan_node")
sub = rospy.Subscriber('/scan', LaserScan, callback)

while not rospy.is_shutdown():
    print(distance)

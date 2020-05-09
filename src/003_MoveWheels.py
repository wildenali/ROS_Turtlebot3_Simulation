#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import time

rospy.init_node("move_wheel_node")
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
rate = rospy.Rate(1)

if __name__ == '__main__':
    twist = Twist()
    twist.linear.x = 0.0
    pub.publish(twist)
    rate.sleep()
    while True:
        twist.linear.x = 0.5
        pub.publish(twist)
        rate.sleep()

        twist.linear.x = 0.0
        pub.publish(twist)
        rate.sleep()

        twist.linear.x = -0.5
        pub.publish(twist)
        rate.sleep()

        twist.linear.x = 0.0
        pub.publish(twist)
        rate.sleep()
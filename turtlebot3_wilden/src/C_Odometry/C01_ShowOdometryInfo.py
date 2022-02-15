#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def callback(msg):
    # print(msg.header.seq)
    # print(msg.header.stamp)
    # print(msg.header.stamp.secs)
    # print(msg.header.stamp.nsecs)
    # print(msg.header.frame_id)
    # print(msg.pose.pose.position.x)
    # print(msg.pose.pose.position.y)
    # print(msg.pose.pose.position.z)
    # print(msg.pose.pose.orientation.x)
    # print(msg.pose.pose.orientation.y)
    # print(msg.pose.pose.orientation.z)
    # print(msg.pose.pose.orientation.w)
    # print(msg.pose.covariance)
    # print(msg.twist.twist.linear.x)
    # print(msg.twist.twist.linear.y)
    # print(msg.twist.twist.linear.z)
    # print(msg.twist.twist.angular.x)
    # print(msg.twist.twist.angular.y)
    # print(msg.twist.twist.angular.z)
    # print(msg.twist.covariance)

    rospy.loginfo("frame_id: %s", msg.header.frame_id)
    rospy.loginfo("pose position x: %s", msg.pose.pose.position.x)
    rospy.loginfo("pose position y: %s", msg.pose.pose.position.y)
    rospy.loginfo("pose position x: %s", msg.pose.pose.position.z)


if __name__ == '__main__':
    rospy.init_node("read_odom")
    sub = rospy.Subscriber('/odom', Odometry, callback)
    rospy.spin()

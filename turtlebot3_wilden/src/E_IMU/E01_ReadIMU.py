#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Imu


def imu_callback(msg):
    print(msg.header.seq)
    print(msg.header.stamp)
    print(msg.header.stamp.secs)
    print(msg.header.stamp.nsecs)
    print(msg.header.frame_id)
    # print(msg.orientation)
    # print(msg.orientation.x)
    # print(msg.orientation.y)
    # print(msg.orientation.z)
    # print(msg.orientation.w)
    # print(msg.orientation_covariance)
    # print(msg.angular_velocity.x)
    # print(msg.angular_velocity.y)
    # print(msg.angular_velocity.z)
    # print(msg.angular_velocity_covariance)
    # print(msg.linear_acceleration.y)
    # print(msg.linear_acceleration.x)
    # print(msg.linear_acceleration.z)
    # print(msg.linear_acceleration_covariance)

    # rospy.loginfo("frame_id: %s", msg.header.frame_id)
    # rospy.loginfo("pose position x: %s", msg.orientation.x)
    # rospy.loginfo("pose position y: %s", msg.orientation.y)
    # rospy.loginfo("pose position x: %s", msg.orientation.z)


if __name__ == '__main__':
    rospy.init_node("read_imu")
    sub = rospy.Subscriber('/imu', Imu, imu_callback)
    rospy.spin()

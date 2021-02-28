#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu

def odom_callback(msg):
    print "pose x = " + str(msg.pose.pose.position.x)
    print "pose y = " + str(msg.pose.pose.position.y)
    print "orientation x = " + str(msg.pose.pose.orientation.x)
    print "orientation y = " + str(msg.pose.pose.orientation.y)

def imu_callback(msg):
    print "vel angular y = " + str(msg.angular_velocity.y)
    print "vel angular z = " + str(msg.angular_velocity.z)
    print "accel linear x = " + str(msg.linear_acceleration.x)
    print "accel linear y = " + str(msg.linear_acceleration.y)
    
rospy.init_node("monitoring_position_and_speed")
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
sub_odom = rospy.Subscriber('/odom', Odometry, odom_callback)
sub_imu = rospy.Subscriber('/imu', Imu, imu_callback)
rate = rospy.Rate(0.5)


if __name__ == '__main__':
    while not rospy.is_shutdown():
        move = Twist()
        move.linear.x = 0.4     # m/s
        move.angular.z = 0.3     # m/s
        pub.publish(move)
        rate.sleep()

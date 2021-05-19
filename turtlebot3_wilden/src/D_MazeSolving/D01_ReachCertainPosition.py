#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2

x = 0.0
y = 0.0
theta = 0.0

def odomCallback(msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    orien_q = msg.pose.pose.orientation

    (roll, pitch, theta) = euler_from_quaternion([orien_q.x, orien_q.y, orien_q.z, orien_q.w])

rospy.init_node("reach_certain_position")
sub = rospy.Subscriber("/odom", Odometry, odomCallback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)

speed = Twist()
rate = rospy.Rate(5)
goal = Point()

goal.x = 1
goal.y = 1

while not rospy.is_shutdown():
    length_x = goal.x - x
    length_y = goal.y - y

    angle_to_goal = atan2(length_y, length_x)

    if abs(angle_to_goal - theta) > 0.1:    # 0.1 on radian unit
        speed.linear.x = 0.0
        speed.angular.z = 0.3
    else:
        speed.linear.x = 0.5
        speed.angular.z = 0.0
    
    pub.publish(speed)
    rate.sleep()
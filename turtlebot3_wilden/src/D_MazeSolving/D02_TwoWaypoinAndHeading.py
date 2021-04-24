#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion, quaternion_from_euler
from geometry_msgs.msg import Point, Twist
from math import atan2, pi, sqrt

pos_x = 0.0
pos_y = 0.0

roll  = 0.0
pitch = 0.0
yaw   = 0.0

kP_Linear = 0.05
kP_Angular = 0.5

def odomCallback(msg):
    global pos_x, pos_y, yaw

    pos_x = msg.pose.pose.position.x
    pos_y = msg.pose.pose.position.y

    orientation_q = msg.pose.pose.orientation
    orient_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orient_list)

def stopTwist():
    print("Stop the Robot")
    speed.linear.x  = 0.0
    speed.angular.z = 0.0
    pub.publish(speed)

def my_shutdown_hook():
    rospy.loginfo("It's shutdown time!") 
    rospy.loginfo("STOP the robot !!!") 
    speed.linear.x = 0
    speed.angular.z = 0
    pub.publish(speed)

def run():
    print("Run")
    while not rospy.is_shutdown():

        # How to calculate distance between current position with goal position
        length_x = goal.x - pos_x
        length_y = goal.y - pos_y
        angle_to_goal = atan2(length_y, length_x)
        distance_to_goal = sqrt(length_x * length_x + length_y * length_y)

        # How Calculate angle error
        # quat = quaternion_from_euler(roll, pitch, yaw)
        # print(quat)
        # print(yaw)
        error_yaw = angle_to_goal - yaw
        print("angle to goal: {:.3f}  yaw: {:.3f}  distance: {:.3f}  speed linear x: {:.3f}".format(error_yaw, speed.angular.z, distance_to_goal, speed.linear.x))
        
        # speed.linear.x = kP_Linear * (distance_to_goal)
        speed.angular.z = kP_Angular * error_yaw
        # print("target_rad:{}  current yaw:{}  distance_to_goal:{}".format(target_rad, yaw, distance_to_goal))

        
        # if error_yaw < 0.1 and error_yaw > -0.1:    # 0.1 on radian unit
        #     speed.linear.x = kP_Linear * (distance_to_goal)
        #     # speed.angular.z = kP_Angular * error_yaw
        #     speed.angular.z = 0.0
        # else:
        #     speed.linear.x = 0.0
        #     speed.angular.z = kP_Angular * error_yaw
        # print("error yaw: {:.3f}  speed angular z: {:.3f}  distance: {:.3f}  speed linear x: {:.3f}".format(error_yaw, speed.angular.z, distance_to_goal, speed.linear.x))
        pub.publish(speed)
        rate.sleep()

rospy.init_node("two_waypoint_and_heading")
sub = rospy.Subscriber("/odom", Odometry, odomCallback)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

speed = Twist()
rate  = rospy.Rate(5)
goal  = Point()

# 

'''
contoh xy = 0 -1
            y
-1 1       0 1       1 1
            |
            |
            |
-1 0--------|--------1 0 x
            |
            |
            |
            |
-1 -1      0 -1      1 -1
'''
goal.x  = 1         # units in meter  0  0 -1  1  1 -1
goal.y  = 1         # units in meter -1  1  0  0  1  1

if __name__ == '__main__':
    try:
        rospy.on_shutdown(my_shutdown_hook)
        run()
    except rospy.ROSInterruptException:
        pass

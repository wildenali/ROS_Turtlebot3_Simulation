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
current_yaw = 0.0
error_yaw = 0.0

kP_linearY      = 1.0
kP_angularZ     = 0.01


def odomCallback(msg):
    global pos_x, pos_y, yaw, current_yaw

    pos_x = msg.pose.pose.position.x
    pos_y = msg.pose.pose.position.y

    orientation_q = msg.pose.pose.orientation
    orient_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orient_list)

    # Convert yaw in rad to current_yaw in deg
    current_yaw = yaw * 180/pi

    # print("pos_x:" + str(pos_x))
    # print("pos_y:" + str(pos_y))

def my_shutdown_hook():
    rospy.loginfo("It's shutdown time!") 
    rospy.loginfo("STOP the robot !!!") 
    speed.linear.x = 0
    speed.angular.z = 0
    pub.publish(speed)

def run():
    global pos_x, pos_y, current_yaw
    print("Run")
    while not rospy.is_shutdown():
        print("pos_x:" + str(pos_x))
        print("pos_y:" + str(pos_y))
        print("yaw  :" + str(current_yaw))

        speed.linear.x  = 0.1
        speed.angular.z = kP_angularZ * (-1*current_yaw) + kP_linearY * (-1*pos_y)
        
        pub.publish(speed)
        rate.sleep()

rospy.init_node("followTheGridYAxis")
sub = rospy.Subscriber("/odom", Odometry, odomCallback)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

speed = Twist()
rate  = rospy.Rate(100)

if __name__ == '__main__':
    try:
        rospy.on_shutdown(my_shutdown_hook)
        run()
    except rospy.ROSInterruptException:
        pass

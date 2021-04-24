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

distance_to_goal = 0.0

kP_Linear = 0.2
kP_Angular = 0.01


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
goal  = Point()
goal.x  = 1         # units in meter  0  0 -1  1  1 -1
goal.y  = 1         # units in meter -1  1  0  0  1  1

def odomCallback(msg):
    global pos_x, pos_y, yaw, current_yaw

    pos_x = msg.pose.pose.position.x
    pos_y = msg.pose.pose.position.y

    orientation_q = msg.pose.pose.orientation
    orient_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion(orient_list)

    # Convert yaw in rad to current_yaw in deg
    current_yaw = yaw * 180/pi

def readDistanceAndYaw():
    global distance_to_goal, error_yaw
    # How to calculate distance between current position with goal position
    length_x = goal.x - pos_x
    length_y = goal.y - pos_y
    distance_to_goal = sqrt(length_x * length_x + length_y * length_y)
    
    # Convert theta in rad to target_yaw in deg
    theta = atan2(length_y, length_x)   # theta         in rad
    target_yaw = theta * 180/pi         # target_yaw    in deg
    
    # How Calculate yaw error
    error_yaw = target_yaw - current_yaw
    if length_x >= 0 and length_y >= 0 and error_yaw > 180:       #Q1
        error_yaw = error_yaw - 360
    elif length_x < 0 and length_y >= 0 and error_yaw > 180:      #Q2
        error_yaw = error_yaw - 360
    elif length_x < 0 and length_y < 0 and error_yaw < -180:      #Q3
        error_yaw = 360 + error_yaw
    elif length_x >= 0 and length_y < 0 and error_yaw < -180:     #Q4
        error_yaw = 360 + error_yaw

def my_shutdown_hook():
    rospy.loginfo("It's shutdown time!") 
    rospy.loginfo("STOP the robot !!!") 
    speed.linear.x = 0
    speed.angular.z = 0
    pub.publish(speed)

def run():
    print("Run")
    isHeading = False
    while not rospy.is_shutdown():
        
        readDistanceAndYaw()

        if distance_to_goal > 0.05:
            while isHeading == False:   # execute when decide the new heading
                readDistanceAndYaw()
                
                if error_yaw > -10 and error_yaw < 10:  # if the robot is already facing the target position
                    print("isHeading True")
                    speed.linear.x  = 0
                    speed.angular.z = 0
                    pub.publish(speed)
                    rate.sleep()
                    isHeading = True    

                speed.linear.x  = 0
                speed.angular.z = kP_Angular * error_yaw
                pub.publish(speed)
                rate.sleep()

            if error_yaw > -20 and error_yaw < 20:  # if error_yaw less than 20 deg
                speed.linear.x  = kP_Linear * distance_to_goal
                speed.angular.z = kP_Angular * error_yaw
            else:
                speed.linear.x  = 0
                speed.angular.z = kP_Angular * error_yaw
        else:
            print("Sampai")
            speed.linear.x  = 0
            speed.angular.z = 0

        # set max speed linear x
        if speed.linear.x >= 0.3:
            speed.linear.x = 0.3

        print("error_yaw:{:.3f}  distance_to_goal:{:.3f}  speed.linear.x:{:.3f}  speed.angular.z:{:.3f}".format(error_yaw, distance_to_goal, speed.linear.x, speed.angular.z))

        pub.publish(speed)
        rate.sleep()

rospy.init_node("two_waypoint_and_heading")
sub = rospy.Subscriber("/odom", Odometry, odomCallback)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

speed = Twist()
rate  = rospy.Rate(5)

if __name__ == '__main__':
    try:
        rospy.on_shutdown(my_shutdown_hook)
        run()
    except rospy.ROSInterruptException:
        pass

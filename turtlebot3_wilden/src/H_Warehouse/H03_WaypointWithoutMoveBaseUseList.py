#!/usr/bin/env python

from distutils.log import error
import rospy
import math
import numpy

from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from tf.transformations import quaternion_from_euler, euler_from_quaternion

from nav_msgs.msg import Odometry
from math import atan2, pi, sqrt

class Run():

    def __init__(self):
        rospy.init_node('H03_WaypointWithoutMoveBaseUseList')

        self.rate  = rospy.Rate(50)
        self.pub_odom = rospy.Subscriber("/odom", Odometry, self.odomCallback)
        self.pub_cmd_vel = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        self.twist = Twist()

        self.current_pose_position = list()
        self.current_pose_orientation = list()
        self.target_pose = list()

        # point = [-2.0, -0.5, 0] # B1
        # point = [-1.5, -1.6, 0] # B2
        # point = [-0.5, -2.1, 0] # B3
        # point = [0.5, -2.1, 0] # B4
        # point = [1.5, -1.6, 0] # B5
        # point = [2.0, -0.5, 0] # B6
        # point = [2.0, 0.5, 0] # B7
        # point = [1.5, 1.6, 0] # B8
        # point = [0.5, 2.1, 0] # B9
        # point = [-0.5, 2.1, 0] # B10
        # point = [-1.5, 1.6, 0] # B11
        # point = [-2.0, 0.5, 0] # B12
        # point = [-1.5, 0.5, 0] # B13
        # point = [-1.5, -0.5, 0] # B14
        # point = [-0.7, -1.6, 0] # B15
        # point = [-0.35, -1.6, 0] # B16
        # point = [0.5, -1.6, 0] # B17
        # point = [0.7, -1.6, 0] # B18
        # point = [1.5, -0.5, 0] # B19
        # point = [1.5, 0.5, 0] # B20
        # point = [0.7, 1.6, 0] # B21
        # point = [0.4, 1.6, 0] # B22
        # point = [-0.35, 1.6, 0] # B23
        # point = [-0.7, 1.6, 0] # B24
        # point = [-0.7, 0.5, 0] # B25
        # point = [-0.7, -0.5, 0] # B26
        # point = [-0.35, -0.5, 0] # B27
        # point = [0.4, -0.5, 0] # B28
        # point = [0.7, -0.5, 0] # B29
        # point = [0.7, 0.5, 0] # B30
        # point = [0.4, 0.5, 0] # B31
        point = [-0.35, 0.5, 0] # B31

        yaw = [90]

        self.kP_Angular = 0.01
        self.kP_Linear = 0.2

        print("")
        print("Ini Menentukan POSE Position")
        posePosition  = Point(*point)
        print(posePosition)

        print("")
        print("Ini Menentukan POSE Orientation")
        q = quaternion_from_euler(0.0, 0.0, numpy.deg2rad(yaw))
        # print(q)
        poseOrientation = Quaternion(*q)
        print(poseOrientation)
        # qq = quaternion_from_euler(0, 0, 0*math.pi/180, axes='sxyz')
        # qqq = Quaternion(*qq)
        # qqqq = quaternion_from_euler(0, 0, 90*math.pi/180, axes='sxyz')
        # qqqqq = Quaternion(*qqqq)

        print("")
        print("Ini Menentukan POSE POSE Position Orientation")
        self.target_pose = Pose(posePosition, poseOrientation)
        print(self.target_pose)
        # print(self.target_pose.position.x)

        self.moveToTarget()
    
    def moveToTarget(self):
        print("")
        print("moveToTarget(self)")
        print(self.target_pose)

        while not rospy.is_shutdown():
            # Read the environment (odom)
            # print(self.errorDistance())
            # print(self.errorAngle())
            print("errorDistance: " + str(self.errorDistance()) + ", errorAngle: " + str(self.errorAngle()))
            # print(type(self.errorAngle()))

            # Check the odom is Ready or not
            if not self.current_pose_position or not self.current_pose_orientation:     # check if the list is empty
                rospy.loginfo("Odometry not Ready")
            else:
                if self.errorAngle() > -10 and self.errorAngle() < 10:      # if the robot is already facing the target position
                    # rospy.loginfo("Heading to Target until errorAngle > -10 and errorAngle < 10")
                    # rospy.loginfo("Good Heading")
                    # self.twist.linear.x = 0
                    # self.twist.angular.z = 0
                    # self.pub_cmd_vel.publish(self.twist)

                    if self.errorDistance() < 0.05: # unit in meter, if the robot close with the target position
                        rospy.loginfo("Arrived")
                        self.twist.linear.x = 0
                        self.twist.angular.z = 0
                        self.pub_cmd_vel.publish(self.twist)
                    else:
                        rospy.loginfo("Good Heading")
                        self.twist.linear.x = self.kP_Linear * self.errorDistance()
                        self.twist.angular.z = self.kP_Angular * self.errorAngle()
                        self.pub_cmd_vel.publish(self.twist)

                else:
                    rospy.loginfo("Correction the Heading")
                    self.twist.linear.x = 0
                    self.twist.angular.z = self.kP_Angular * self.errorAngle()
                    rospy.loginfo(self.twist)
                    self.pub_cmd_vel.publish(self.twist)



            self.rate.sleep()
        # rospy.spin()
    
    def odomCallback(self, msg):
        # print("odomCallback(self, msg)")
        self.current_pose_position = msg.pose.pose.position
        self.current_pose_orientation = msg.pose.pose.orientation
        # print(self.current_pose_position)
        # print(self.current_pose_orientation)
        # print(self.current_pose_position.x)
        # print(self.current_pose_orientation.x)

        orientation_q = msg.pose.pose.orientation
        orient_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        (roll, pitch, yaw) = euler_from_quaternion(orient_list)
        self.current_yaw = yaw * 180/pi  # Convert yaw in rad to current_yaw in deg
    
    def errorDistance(self):
        # print("errorDistance(self)")
        if not self.current_pose_position or not self.current_pose_orientation:     # check if the list is empty
            print("odom not ready")
            return None
        else:
            length_x = self.target_pose.position.x - self.current_pose_position.x
            length_y = self.target_pose.position.y - self.current_pose_position.y
            distance_to_target = sqrt(length_x * length_x + length_y * length_y)
            # print("x: " + str(length_x) + ", y: " + str(length_y) + ", distance: " + str(distance_to_target))
            return distance_to_target

    def errorAngle(self):
        # print("errorAngle(self)")
        if not self.current_pose_position or not self.current_pose_orientation:     # check if the list is empty
            print("odom not ready")
            return None
        else:
            length_x = self.target_pose.position.x - self.current_pose_position.x
            length_y = self.target_pose.position.y - self.current_pose_position.y
            # Convert theta in rad to target_yaw in deg
            theta = atan2(length_y, length_x)   # theta         in rad
            target_yaw = theta * 180/pi         # target_yaw    in deg
            error_yaw = target_yaw - self.current_yaw  # How Calculate yaw error
            if length_x >= 0 and length_y >= 0 and error_yaw > 180:       #Q1
                error_yaw = error_yaw - 360
            elif length_x < 0 and length_y >= 0 and error_yaw > 180:      #Q2
                error_yaw = error_yaw - 360
            elif length_x < 0 and length_y < 0 and error_yaw < -180:      #Q3
                error_yaw = 360 + error_yaw
            elif length_x >= 0 and length_y < 0 and error_yaw < -180:     #Q4
                error_yaw = 360 + error_yaw
            return error_yaw


        
if __name__ == '__main__':
    try:
        Run()
    except rospy.ROSInterruptException:
        rospy.loginfo("rospy.ROSInterruptException")
        pub_cmd_vel = rospy.Publisher("/cmd_vel", Twist, queue_size=10)
        twist = Twist()
        twist.linear.x = 0
        twist.angular.z = 0
        pub_cmd_vel.publish(twist)
        rospy.loginfo(twist)
        rospy.loginfo("Navigation finished.")
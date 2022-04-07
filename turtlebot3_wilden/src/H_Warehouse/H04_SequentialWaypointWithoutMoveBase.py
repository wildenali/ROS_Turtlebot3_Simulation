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
        self.target_pose_sequential = list()
        self.goal_cnt = 0


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
        # point = [-0.35, 0.5, 0] # B32

        self.kP_Angular = 0.01
        self.kP_Linear = 0.2

        yaweulerangles_seq = [90, 180]
        quat_seq = list()
        print("")
        print("Ini Menentukan POSE Orientation")
        # q = quaternion_from_euler(0.0, 0.0, numpy.deg2rad(yaweulerangles_seq))
        # print(q)
        # poseOrientation = Quaternion(*q)
        # print(poseOrientation)
        # qq = quaternion_from_euler(0, 0, 0*math.pi/180, axes='sxyz')
        # qqq = Quaternion(*qq)
        # qqqq = quaternion_from_euler(0, 0, 90*math.pi/180, axes='sxyz')
        # qqqqq = Quaternion(*qqqq)
        for yawAngle in yaweulerangles_seq:
            q = quaternion_from_euler(0.0, 0.0, numpy.deg2rad(yawAngle))
            print(q)
            quat_seq.append(Quaternion(*q))
        print(quat_seq)


        # points_seq = [-2.0, -0.5, 0] # to B1
        # points_seq = [-1.5, -1.6, 0, -0.5, -2.1, 0] # to B2 to B3
        points_seq = [-1.5, -1.6, 0, -2.0, -0.5, 0] # to B2 to B1
        # because the point more than 1 poin, than we have to split the points
        points = []
        n = 3
        print("MASUK 1")
        for i in range(0, len(points_seq), n):
            points += [points_seq[i:i+n]]
        print(points)
        print("MASUK 2")
        for point in points:
            posePosition  = Point(*point)
            # print(posePosition)
            self.target_pose_sequential.append(Pose(posePosition, quat_seq[n-3]))
            # print(self.target_pose_sequential)
            n += 1
        print(self.target_pose_sequential)
        print("")
        print("lenght of self.target_pose_sequential")
        # print(len(self.target_pose_sequential))
        for i in range(len(self.target_pose_sequential)):
            print("")
            print("self.target_pose_sequential["+ str(i) + "]")
            print(self.target_pose_sequential[i])
        self.moveToTarget()
    
    def moveToTarget(self):
        print("")
        print("moveToTarget(self)")
        print(self.target_pose_sequential)
        
        # print("errorDistance: " + str(self.errorDistance(self.target_pose_sequential[0])))# + ", errorAngle: " + str(self.errorAngle()))

        while not rospy.is_shutdown():
            # OKE TAHAP 1, tahap 2 tinggal ganti target ke [1]
            # Read the environment (odom)
            # print(self.errorDistance(self.target_pose_sequential[0]))
            # print(self.errorAngle(self.target_pose_sequential[0]))
            error_Distance = self.errorDistance(self.target_pose_sequential[self.goal_cnt])
            error_Angle = self.errorAngle(self.target_pose_sequential[self.goal_cnt])
            print("errorDistance: " + str(error_Distance) + ", errorAngle: " + str(error_Angle))

            # Check the odom is Ready or not
            if not self.current_pose_position or not self.current_pose_orientation:     # check if the list is empty
                rospy.loginfo("Odometry not Ready")
            else:
                if error_Angle > -10 and error_Angle < 10:      # if the robot is already facing the target position
                    if error_Distance < 0.05: # unit in meter, if the robot close with the target position
                        rospy.loginfo("Arrived: " + str(self.goal_cnt) + " " +str(len(self.target_pose_sequential)))
                        self.twist.linear.x = 0
                        self.twist.angular.z = 0
                        if self.goal_cnt == len(self.target_pose_sequential) - 1:   # disini untuk membatasi sampai maksimal target_pose_sequential 
                            rospy.loginfo("DONE FINISH")
                        else:
                            self.goal_cnt += 1
                    else:
                        rospy.loginfo("Good Heading")
                        self.twist.linear.x = self.kP_Linear * error_Distance
                        self.twist.angular.z = self.kP_Angular * error_Angle
                else:
                    rospy.loginfo("Correction the Heading")
                    self.twist.linear.x = 0
                    self.twist.angular.z = self.kP_Angular * error_Angle
                    rospy.loginfo(self.twist)

                self.pub_cmd_vel.publish(self.twist)
            self.rate.sleep()
    
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
    
    def errorDistance(self, msg_targetPose):
        # print("errorDistance(self)")
        # print(msg_targetPose)
        if not self.current_pose_position or not self.current_pose_orientation:     # check if the list is empty
            print("odom not ready")
            return None
        else:
            print("errorDistance(self)")
            # print(msg_targetPose)
            # print(msg_targetPose.position.x)
            # print(msg_targetPose.position.y)
            length_x = msg_targetPose.position.x - self.current_pose_position.x
            length_y = msg_targetPose.position.y - self.current_pose_position.y
            distance_to_target = sqrt(length_x * length_x + length_y * length_y)
            # print("x: " + str(length_x) + ", y: " + str(length_y) + ", distance: " + str(distance_to_target))
            return distance_to_target

    def errorAngle(self, msg_targetPose):
        # print("errorAngle(self)")
        if not self.current_pose_position or not self.current_pose_orientation:     # check if the list is empty
            print("odom not ready")
            return None
        else:
            length_x = msg_targetPose.position.x - self.current_pose_position.x
            length_y = msg_targetPose.position.y - self.current_pose_position.y
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
#!/usr/bin/env python

import rospy
import math
import numpy

from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler, euler_from_quaternion

from nav_msgs.msg import Odometry
from math import atan2, pi, sqrt

class Run():

    def __init__(self):
        rospy.init_node('H03_WaypointWithoutMoveBaseUseList')

        self.pub_odom = rospy.Subscriber("/odom", Odometry, self.odomCallback)
        # self.pub_cmd_vel = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

        self.current_pose_position = list()
        self.current_pose_orientation = list()
        self.target_pose = list()

        point = [0, 0.8, 0]
        yaw = [90]

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

        self.move_to_target()
    
    def move_to_target(self):
        print("")
        print("move_to_target")
        print(self.target_pose)

        # Read the environment (odom)
        rospy.spin()
    
    def odomCallback(self, msg):
        self.current_pose_position = msg.pose.pose.position
        self.current_pose_orientation = msg.pose.pose.orientation
        # print(self.current_pose_position)
        # print(self.current_pose_orientation)

        # global current_yaw
        # orientation_q = msg.pose.pose.orientation
        # orient_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
        # (roll, pitch, yaw) = euler_from_quaternion(orient_list)
        # # Convert yaw in rad to current_yaw in deg
        # current_yaw = yaw * 180/pi
        # # print(current_yaw)
        # # print(msg.pose.pose.position)
        
if __name__ == '__main__':
    try:
        Run()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation finished.")


        
# #!/usr/bin/env python

# import rospy
# from nav_msgs.msg import Odometry
# from tf.transformations import euler_from_quaternion, quaternion_from_euler
# from geometry_msgs.msg import Point, Twist, Pose, Quaternion
# from math import atan2, pi, sqrt

# # pos_x = 0.0
# # pos_y = 0.0

# # roll  = 0.0
# # pitch = 0.0
# # yaw   = 0.0
# # current_yaw = 0.0
# # error_yaw = 0.0

# # distance_to_goal = 0.0

# # kP_Linear = 0.2
# # kP_Angular = 0.01


# goal  = Point()
# POSEU = Pose()
# kua = Quaternion()
# # goal.x  = -1         # units in meter  0  0 -1  1  1 -1
# # goal.y  = 1         # units in meter -1  1  0  0  1  1

# # current_goal_x  = -1.9
# # current_goal_y  = 0.4
# # next_goal_x     = -1.9
# # next_goal_y     = 0.0

# # def odomCallback(msg):
# #     global pos_x, pos_y, yaw, current_yaw

# #     pos_x = msg.pose.pose.position.x
# #     pos_y = msg.pose.pose.position.y

# #     orientation_q = msg.pose.pose.orientation
# #     orient_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
# #     (roll, pitch, yaw) = euler_from_quaternion(orient_list)

# #     # Convert yaw in rad to current_yaw in deg
# #     current_yaw = yaw * 180/pi

# # def readDistanceAndYaw():
# #     global distance_to_goal, error_yaw
# #     # How to calculate distance between current position with goal position
# #     length_x = goal.x - pos_x
# #     length_y = goal.y - pos_y
# #     distance_to_goal = sqrt(length_x * length_x + length_y * length_y)
    
# #     # Convert theta in rad to target_yaw in deg
# #     theta = atan2(length_y, length_x)   # theta         in rad
# #     target_yaw = theta * 180/pi         # target_yaw    in deg
    
# #     # How Calculate yaw error
# #     error_yaw = target_yaw - current_yaw
# #     if length_x >= 0 and length_y >= 0 and error_yaw > 180:       #Q1
# #         error_yaw = error_yaw - 360
# #     elif length_x < 0 and length_y >= 0 and error_yaw > 180:      #Q2
# #         error_yaw = error_yaw - 360
# #     elif length_x < 0 and length_y < 0 and error_yaw < -180:      #Q3
# #         error_yaw = 360 + error_yaw
# #     elif length_x >= 0 and length_y < 0 and error_yaw < -180:     #Q4
# #         error_yaw = 360 + error_yaw

# # def my_shutdown_hook():
# #     rospy.loginfo("It's shutdown time!") 
# #     rospy.loginfo("STOP the robot !!!") 
# #     speed.linear.x = 0
# #     speed.angular.z = 0
# #     pub.publish(speed)


# class Run():
    
#     def __init__(self):
#         rospy.init_node('H02_WaypointWithoutMoveBaseUseList')

#         # points_seq = [-1.9,0.4,0.0, -1.9,0.0,0.0]

#         # pose: 
#         #     position: 
#         #     x: -1.9
#         #     y: 0.4
#         #     z: 0.0
#         #     orientation: 
#         #     x: 0.0
#         #     y: 0.0
#         #     z: 0.999933589754
#         #     w: -0.011414187123
#         pose_raw = [-1.9,0.4,0.0, 0.0,0.0,0.99,-0.01,
#                     -1.9,0.0,0.0, 0.0,0.0,0.99,-0.01]
#         self.pose_seq = list()
#         self.goal_cnt = 0
#         # points = [pose_raw[i:i+n]]
#         # for point in point
#         print(pose_raw)
#         print(self.pose_seq)
#         print(goal)
#         print(POSEU)
#         print(kua)




#     # print("Run")
#     # goal.x = current_goal_x
#     # goal.y = current_goal_y
#     # isHeading = False
#     # while not rospy.is_shutdown():
        
#     #     readDistanceAndYaw()

#     #     if distance_to_goal > 0.05:
#     #         while isHeading == False:   # execute when decide the new heading
#     #             readDistanceAndYaw()
                
#     #             if error_yaw > -10 and error_yaw < 10:  # if the robot is already facing the target position
#     #                 print("isHeading True")
#     #                 speed.linear.x  = 0
#     #                 speed.angular.z = 0
#     #                 pub.publish(speed)
#     #                 rate.sleep()
#     #                 isHeading = True    

#     #             speed.linear.x  = 0
#     #             speed.angular.z = kP_Angular * error_yaw
#     #             pub.publish(speed)
#     #             rate.sleep()

#     #         if error_yaw > -20 and error_yaw < 20:  # if error_yaw less than 20 deg
#     #             speed.linear.x  = kP_Linear * distance_to_goal
#     #             speed.angular.z = kP_Angular * error_yaw
#     #         else:
#     #             speed.linear.x  = 0
#     #             speed.angular.z = kP_Angular * error_yaw
#     #     else:
#     #         print("Sampai")
#     #         speed.linear.x  = 0
#     #         speed.angular.z = 0

#     #         if goal.x != next_goal_x: 
#     #             goal.x = next_goal_x
#     #         elif goal.x != current_goal_x: 
#     #             goal.x = current_goal_x
#     #         if goal.y != next_goal_y: 
#     #             goal.y = next_goal_y
#     #         elif goal.y != current_goal_y: 
#     #             goal.y = current_goal_y

#     #     # set max speed linear x
#     #     if speed.linear.x >= 0.3:
#     #         speed.linear.x = 0.3

#     #     print("error_yaw:{:.3f}  distance_to_goal:{:.3f}  speed.linear.x:{:.3f}  speed.angular.z:{:.3f}".format(error_yaw, distance_to_goal, speed.linear.x, speed.angular.z))

#     #     pub.publish(speed)
#     #     rate.sleep()

#     # def run_client(self):

# # sub = rospy.Subscriber("/odom", Odometry, odomCallback)
# # pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

# # speed = Twist()
# # rate  = rospy.Rate(5)

# if __name__ == '__main__':
#     try:
#         # rospy.on_shutdown(my_shutdown_hook)
#         Run()
#     except rospy.ROSInterruptException:
#         rospy.loginfo("Navigation finished.")
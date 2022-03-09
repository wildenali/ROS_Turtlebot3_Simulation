# #!/usr/bin/env python

# import rospy
# from nav_msgs.msg import Odometry
# from tf.transformations import euler_from_quaternion, quaternion_from_euler
# from geometry_msgs.msg import Point, Twist, Pose
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


# # goal  = Point()
# # # goal.x  = -1         # units in meter  0  0 -1  1  1 -1
# # # goal.y  = 1         # units in meter -1  1  0  0  1  1

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
#         points_seq = [-1.9,0.4,0.0, 0.0,0.0,0.99,-0.01,
#                     -1.9,0.0,0.0, 0.0,0.0,0.99,-0.01]
#         self.pose_seq = list()
#         self.goal_cnt = 0
#         # points = [points_seq[i:i+n]]
#         # for point in point
#         print(points_seq)
#         print(self.pose_seq)




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





#!/usr/bin/env python

# license removed for brevity

# Source: https://hotblackrobotics.github.io/en/blog/2018/01/29/seq-goals-py/

__author__ = 'fiorellasibona'
import rospy
import math

import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from actionlib_msgs.msg import GoalStatus
from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

class MoveBaseSeq():

    def __init__(self):

        rospy.init_node('move_base_sequence')
        # points_seq = rospy.get_param('move_base_seq/p_seq')
        # yaweulerangles_seq = rospy.get_param('move_base_seq/yea_seq')
        points_seq = [0,0,0, 0,1.8,0]
        yaweulerangles_seq = [0, 90]
        quat_seq = list()
        self.pose_seq = list()
        self.goal_cnt = 0
        print("MASUK POINTS")
        for yawangle in yaweulerangles_seq:
            quat_seq.append(Quaternion(*(quaternion_from_euler(0, 0, yawangle*math.pi/180, axes='sxyz'))))
            print("MASUK qut_")
            print(quat_seq)
        n = 3
        points = [points_seq[i:i+n] for i in range(0, len(points_seq), n)]
        # print(points)
        # print(quat_seq[0])
        for point in points:
            self.pose_seq.append(Pose(Point(*point),quat_seq[n-3]))
            print("POINT_SEQ")
            print(point)
            # print(quat_seq[n-3])
            n += 1
        self.client = actionlib.SimpleActionClient('move_base',MoveBaseAction)
        rospy.loginfo("Waiting for move_base action server...")
        wait = self.client.wait_for_server(rospy.Duration(5.0))
        if not wait:
            rospy.logerr("Action server not available!")
            rospy.signal_shutdown("Action server not available!")
            return
        rospy.loginfo("Connected to move base server")
        rospy.loginfo("Starting goals achievements ...")
        self.movebase_client()

    def active_cb(self):
        rospy.loginfo("Goal pose "+str(self.goal_cnt+1)+" is now being processed by the Action Server...")

    def feedback_cb(self, feedback):
        pass
        # rospy.loginfo("Feedback for goal pose "+str(self.goal_cnt+1)+" received")

    def done_cb(self, status, result):
        self.goal_cnt += 1
        if status == 2:
            rospy.loginfo("Goal pose "+str(self.goal_cnt)+" received a cancel request after it started executing, completed execution!")

        if status == 3:
            rospy.loginfo("Goal pose "+str(self.goal_cnt)+" reached") 
            if self.goal_cnt< len(self.pose_seq):
                next_goal = MoveBaseGoal()
                next_goal.target_pose.header.frame_id = "map"
                next_goal.target_pose.header.stamp = rospy.Time.now()
                next_goal.target_pose.pose = self.pose_seq[self.goal_cnt]
                rospy.loginfo("Sending goal pose "+str(self.goal_cnt+1)+" to Action Server")
                rospy.loginfo(str(self.pose_seq[self.goal_cnt]))
                print("MASUK 2")
                print(self.pose_seq[self.goal_cnt])
                print(next_goal.target_pose.pose)
                self.client.send_goal(next_goal, self.done_cb, self.active_cb, self.feedback_cb) 
            else:
                rospy.loginfo("Final goal pose reached!")
                rospy.signal_shutdown("Final goal pose reached!")
                return

        if status == 4:
            rospy.loginfo("Goal pose "+str(self.goal_cnt)+" was aborted by the Action Server")
            rospy.signal_shutdown("Goal pose "+str(self.goal_cnt)+" aborted, shutting down!")
            return

        if status == 5:
            rospy.loginfo("Goal pose "+str(self.goal_cnt)+" has been rejected by the Action Server")
            rospy.signal_shutdown("Goal pose "+str(self.goal_cnt)+" rejected, shutting down!")
            return

        if status == 8:
            rospy.loginfo("Goal pose "+str(self.goal_cnt)+" received a cancel request before it started executing, successfully cancelled!")

    def movebase_client(self):
        goal = MoveBaseGoal()
        goal.target_pose.header.frame_id = "map"
        goal.target_pose.header.stamp = rospy.Time.now() 
        goal.target_pose.pose = self.pose_seq[self.goal_cnt]
        print("MASUK")
        print(self.pose_seq[self.goal_cnt])
        print(goal.target_pose.pose)
        print("GOAL 1")
        print(self.pose_seq[0])
        print("GOAL 2")
        print(self.pose_seq[1])
        print("GOAL 3")
        print(self.pose_seq[2])
        rospy.loginfo("Sending goal pose "+str(self.goal_cnt+1)+" to Action Server")
        rospy.loginfo(str(self.pose_seq[self.goal_cnt]))
        self.client.send_goal(goal, self.done_cb, self.active_cb, self.feedback_cb)
        rospy.spin()

if __name__ == '__main__':
    try:
        MoveBaseSeq()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation finished.")




# dewatic@robotic:~/catkin_ws/src/ROS_Turtlebot3_Simulation/turtlebot3_wilden/src/H_Warehouse$ python H02_WaypointWithoutMoveBaseUseList.py 
# MASUK POINTS
# [x: 0.0
# y: 0.0
# z: 0.0
# w: 1.0]
# [x: 0.0
# y: 0.0
# z: 0.0
# w: 1.0, x: 0.0
# y: 0.0
# z: 0.707106781187
# w: 0.707106781187]
# [0, 0, 0]
# x: 0.0
# y: 0.0
# z: 0.0
# w: 1.0
# [0, 1.8, 0]
# x: 0.0
# y: 0.0
# z: 0.707106781187
# w: 0.707106781187
# [INFO] [1646668755.718517, 4297.702000]: Waiting for move_base action server...
# [INFO] [1646668755.951090, 4297.893000]: Connected to move base server
# [INFO] [1646668755.962326, 4297.895000]: Starting goals achievements ...
# MASUK
# position: 
#   x: 0
#   y: 0
#   z: 0
# orientation: 
#   x: 0.0
#   y: 0.0
#   z: 0.0
#   w: 1.0
# position: 
#   x: 0
#   y: 0
#   z: 0
# orientation: 
#   x: 0.0
#   y: 0.0
#   z: 0.0
#   w: 1.0
# [INFO] [1646668755.971435, 4297.900000]: Sending goal pose 1 to Action Server
# [INFO] [1646668755.979403, 4297.908000]: position: 
#   x: 0
#   y: 0
#   z: 0
# orientation: 
#   x: 0.0
#   y: 0.0
#   z: 0.0
#   w: 1.0
# [INFO] [1646668755.991014, 4297.916000]: Goal pose 1 is now being processed by the Action Server...
# [INFO] [1646668784.297921, 4320.218000]: Goal pose 1 reached
# [INFO] [1646668784.305664, 4320.226000]: Sending goal pose 2 to Action Server
# [INFO] [1646668784.315862, 4320.230000]: position: 
#   x: 0
#   y: 1.8
#   z: 0
# orientation: 
#   x: 0.0
#   y: 0.0
#   z: 0.707106781187
#   w: 0.707106781187
# MASUK 2
# position: 
#   x: 0
#   y: 1.8
#   z: 0
# orientation: 
#   x: 0.0
#   y: 0.0
#   z: 0.707106781187
#   w: 0.707106781187
# position: 
#   x: 0
#   y: 1.8
#   z: 0
# orientation: 
#   x: 0.0
#   y: 0.0
#   z: 0.707106781187
#   w: 0.707106781187
# [INFO] [1646668784.332957, 4320.246000]: Goal pose 2 is now being processed by the Action Server...
# [INFO] [1646668809.688188, 4338.838000]: Goal pose 2 reached
# [INFO] [1646668809.695968, 4338.839000]: Final goal pose reached!
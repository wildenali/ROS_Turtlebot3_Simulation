#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import time

position_x = 0
position_y = 0
orientation_z = 0

def callbackOdometry(msg):
    # print(msg.header.seq)
    # print(msg.header.stamp)
    # print(msg.header.stamp.secs)
    # print(msg.header.stamp.nsecs)
    # print(msg.header.frame_id)
    # print(msg.pose.pose.position.x)
    # print(msg.pose.pose.position.y)
    # print(msg.pose.pose.position.z)
    # print(msg.pose.pose.orientation.x)
    # print(msg.pose.pose.orientation.y)
    # print(msg.pose.pose.orientation.z)
    # print(msg.pose.pose.orientation.w)
    # print(msg.pose.covariance)
    # print(msg.twist.twist.linear.x)
    # print(msg.twist.twist.linear.y)
    # print(msg.twist.twist.l inear.z)
    # print(msg.twist.twist.angular.x)
    # print(msg.twist.twist.angular.y)
    # print(msg.twist.twist.angular.z)
    # print(msg.twist.covariance)

    # rospy.loginfo("frame_id: %s", msg.header.frame_id)
    # rospy.loginfo("pose position x: %s", msg.pose.pose.position.x)
    # rospy.loginfo("pose position y: %s", msg.pose.pose.position.y)
    # rospy.loginfo("pose position x: %s", msg.pose.pose.position.z)
    global position_x, position_y, orientation_z
    position_x = msg.pose.pose.position.x
    position_y = msg.pose.pose.position.y
    orientation_z = msg.pose.pose.orientation.z


def main():
    rospy.init_node("movesquare")
    # sub_odometry = rospy.Subscriber('/odom', Odometry, callbackOdometry)
    # pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    # twist = Twist()
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    pub_twist.publish(twist)
    square()


def square():
    # assume that the default position of robot x=0 y=0
    print("Square")
    lastpos_x = position_x
    lastpos_y = position_y
    distance_x = position_x - lastpos_x
    distance_y = position_y - lastpos_y
    twist.linear.x = 0.1
    pub_twist.publish(twist)
    while not rospy.is_shutdown():
        distance_x = position_x - lastpos_x
        distance_y = position_y - lastpos_y
        print("distance x : %.2f" %distance_x)
        pub_twist.publish(twist)
        if(distance_x >= 1.0):
            print("Stop")
            twist.linear.x = 0.0
            pub_twist.publish(twist)
            time.sleep(1)
            print("Belok Kiri ke 1")
            twist.angular.z = 0.1
            pub_twist.publish(twist)
            time.sleep(16)
            print("Stop")
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            pub_twist.publish(twist)
            time.sleep(1)
            belok_kiri_1 = True
            lastpos_y = position_y
            while (belok_kiri_1):
                twist.linear.x = 0.1
                distance_y = position_y - lastpos_y
                pub_twist.publish(twist)
                if(distance_y >= 1.0):
                    print("Stop")
                    twist.linear.x = 0.0
                    pub_twist.publish(twist)
                    time.sleep(1)
                    print("Belok Kiri ke 2")
                    twist.angular.z = 0.1
                    pub_twist.publish(twist)
                    time.sleep(16)
                    print("Stop")
                    twist.linear.x = 0.0
                    twist.angular.z = 0.0
                    pub_twist.publish(twist)
                    time.sleep(1)
                    belok_kiri_1 = False
                    belok_kiri_2 = True
                    lastpos_x = position_x
                    while (belok_kiri_2):
                        twist.linear.x = 0.1
                        distance_x = position_x - lastpos_x
                        pub_twist.publish(twist)
                        if(distance_x <= -1.0):
                            print("Stop")
                            twist.linear.x = 0.0
                            pub_twist.publish(twist)
                            time.sleep(1)
                            print("Belok Kiri ke 3")
                            twist.angular.z = 0.1
                            pub_twist.publish(twist)
                            time.sleep(16)
                            print("Stop")
                            twist.linear.x = 0.0
                            twist.angular.z = 0.0
                            pub_twist.publish(twist)
                            time.sleep(1)
                            belok_kiri_2 = False
                            belok_kiri_3 = True
                            lastpos_y = position_y
                            while (belok_kiri_3):
                                twist.linear.x = 0.1
                                distance_y = position_y - lastpos_y
                                pub_twist.publish(twist)
                                if(distance_y <= -1.0):
                                    print("Stop")
                                    twist.linear.x = 0.0
                                    pub_twist.publish(twist)
                                    time.sleep(1)
                                    print("Stop")
                                    belok_kiri_3 = False
            print("Selesai")
            break

if __name__ == '__main__':
    sub_odometry = rospy.Subscriber('/odom', Odometry, callbackOdometry)
    pub_twist = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
    twist = Twist()
    try:
        main()
    except rospy.ROSInterruptException:
        pass
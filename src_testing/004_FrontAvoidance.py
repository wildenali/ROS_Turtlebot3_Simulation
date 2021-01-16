#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import time

distance = 0.0

def callback(msg):
    global distance
    distance = msg.ranges[360]
    
def main():
    rospy.init_node("frontAvoidance")
    sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    twist = Twist()
    
    while distance == 0.0:
        print(distance)

    while not rospy.is_shutdown():
        if(distance < 1):
            # print(distance)
            print("udah dekat: " + str(distance))
            twist.linear.x = 0.0
            pub.publish(twist)
            time.sleep(2)

            twist.angular.z = -0.2
            pub.publish(twist)
            time.sleep(7)
        else:
            # print(distance)
            print("masih jauh: " + str(distance))
            twist.linear.x = 0.2
            twist.angular.z = 0.0
            pub.publish(twist)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

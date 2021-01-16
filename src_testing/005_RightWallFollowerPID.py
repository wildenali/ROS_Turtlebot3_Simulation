#!/usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import time
distance0 = 0.0
distance1 = 0.0
distance2 = 0.0

def callback(msg):
    global distance0, distance1, distance2
    distance0 = msg.ranges[360]
    distance1 = msg.ranges[120]
    distance2 = msg.ranges[0]
    
def main():
    rospy.init_node("frontAvoidance")
    sub = rospy.Subscriber('/kobuki/laser/scan', LaserScan, callback)
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
    twist = Twist()
    
    while distance1 == 0.0:
        print(distance1)

    while not rospy.is_shutdown():

        if(distance0 < 0.7):
            print("udah dekat: " + str(distance0))
            twist.linear.x = 0.0
            pub.publish(twist)
            time.sleep(2)

            twist.angular.z = 0.2
            pub.publish(twist)
            time.sleep(8)
        else:
            errorDistance1 = distance1 - 0.78 
            errorDistance2 = distance2 - 0.68 
            error = errorDistance1 + errorDistance2
            control_P = 1 * error
            steer = control_P
            if(steer < -0.2):
                steer = -0.2
            print("D1: %.2f  D2: %.2f  e1: %.2f e2: %.2f e: %.2f control_P: %.2f steer: %.2f" %(distance1, distance2, errorDistance1, errorDistance2, error, control_P, steer))
            
            twist.linear.x = 0.4
            twist.angular.z = -1 * steer
            pub.publish(twist)

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
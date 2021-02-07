#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def run():
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.init_node('accel_vel_array_publisher')
    rate = rospy.Rate(1)    # 1 Hz
    cmd_vel_array = [0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10]
    vel = Twist()
    while not rospy.is_shutdown():
        for i in range(len(cmd_vel_array)):
            vel.linear.x = cmd_vel_array[i]
            print("Publishing velocity: " + str(cmd_vel_array[int(i)]))
            pub.publish(vel)
            i = i+1
            rate.sleep()

if __name__ == '__main__':
    try:
        run()
    except rospy.ROSInterruptException:
        pass
#!/usr/bin/env python

import rospy
import math
import numpy

from geometry_msgs.msg import Pose, Point, Quaternion
from tf.transformations import quaternion_from_euler

class Run():

    def __init__(self):

        rospy.init_node('move_base_sequence')
        
        self.pose_seq = list()
        self.goal_cnt = 0

        print("")
        print("Ini Menentukan POSE Position")
        print("ini_point")
        ini_point = [0, 0.8, 0]
        iniPoint  = Point(*ini_point)
        print(ini_point)
        print(iniPoint)


        print("")
        print("Ini Menentukan POSE Orientation")
        print("q")
        q = quaternion_from_euler(0.0, 0.0, numpy.deg2rad(90.0))
        hasil_q = Quaternion(*q)
        print(q)
        print(Quaternion(*q))
        print(hasil_q)
        # qq = quaternion_from_euler(0, 0, 0*math.pi/180, axes='sxyz')
        # qqq = Quaternion(*qq)
        # qqqq = quaternion_from_euler(0, 0, 90*math.pi/180, axes='sxyz')
        # qqqqq = Quaternion(*qqqq)


        print("")
        print("Ini Menentukan POSE POSE Position Orientation")
        ini_pose = Pose(iniPoint, hasil_q)
        print(ini_pose)
        
if __name__ == '__main__':
    try:
        Run()
    except rospy.ROSInterruptException:
        rospy.loginfo("Navigation finished.")
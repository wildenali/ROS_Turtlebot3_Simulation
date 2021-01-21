# `How to Get Odometry Data Turtlebot3`

1. Create a file called C01_ShowOdometryInfo.py

- `$ roscd turtlebot3_wilden/src/C_ShowOdometryInfo`
- `$ touch C01_ShowOdometryInfo.py`

2. Launch the turtlebot3_world.launch
   Open a terminal and run:

- `$ export TURTLEBOT3_MODEL=burger`
- `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`

3. Find the /odom Topic
   Open a new terminal and run:

- `$ rostopic list`
- `$ rostopic info /odom`
- `$ rosmsg show nav_msgs/Odometry`
- `$ rosmsg show nav_msgs/Odometry`

4. Launch the teleop
   Open a new terminal and run:

- `$ export TURTLEBOT3_MODEL=burger`
- `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`
  atau
- `$ rosrun turtlebot3_wilden B01_MoveWheels.py`

5. Show the /odom message using command line

- `$ rostopic echo /odom -n1`
- `$ rostopic echo /odom`

6. Show the /odom message using python script
   Open a new terminal and run:

- Open a C01_ShowOdometryInfo.py file and write the code
- `$ chmod +x C01_ShowOdometryInfo.py` change the permissions
- Open a CMakeLists.txt inside turtlebot3_wilden package and edit

```
catkin_install_python(PROGRAMS
  src/A_ReadLaserScan/A01_ReadLaserScan.py
  src/A_ReadLaserScan/A02_ReadLaserScan.py
  src/B_MoveWheels/C01_ShowOdometryInfo.py
  src/C_ShowOdometryInfo/C01_ShowOdometryInfo.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

- Open a C01_ShowOdometryInfo.py file and write the code
- `$ roscd ~/catkin_ws`
- `$ catkin_make`
- `$ rosrun turtlebot3_wilden C01_ShowOdometryInfo.py`

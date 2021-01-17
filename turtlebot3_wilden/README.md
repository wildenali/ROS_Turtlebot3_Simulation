## Create a New ROS Package

Open a new terminal

- `$ cd ~/catkin_ws/src/ROS_Turtlebot3_Simulation`
- `$ catkin_create_pkg turtlebot3_wilden std_msgs rospy`
- `$ cd ~/catkin_ws`
- `$ catkin_make`
- `$ . ~/catkin_ws/devel/setup.bash`

# `Measure the Distance with Laser Scanner Lidar`

1. Create a file called 001_ReadLaserScan.py

- `$ roscd turtlebot3_wilden/src`
- `$ touch 001_ReadLaserScan.py`

2. Find the Laser Scanner Lidar Topic

- `$ rostopic list` it will list the active topic and find `scan` topic
- `$ rostopic info /scan` show the /scan topic information
- `$ rostopic echo /scan` looping print messages to screen
- `$ rostopic echo /scan -n1` just once print messages to screen
- `$ rosmsg show sensor_msgs/LaserScan` show the data type

3. Create a Code and Configuration

- Open a 001_ReadLaserScan.py file and write the code
- `$ chmod +x 001_ReadLaserScan.py` change the permissions
- Open a CMakeLists.txt inside turtlebot3_wilden package and edit

```
catkin_install_python(PROGRAMS
  src/001_ReadLaserScan.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

- `$ roscd ~/catkin_ws`
- `$ catkin_make`

4. Launch the turtlebot3_world.launch
   Open a terminal and run:

- `$ export TURTLEBOT3_MODEL=burger`
- `$ roslaunch turtlebot3_gazebo t7rtlebot3_world.launch`

5. Run Gazebo

6. Launch the turtlebot3_world.launch
   Open a new terminal and run:

- `$ export TURTLEBOT3_MODEL=burger`
- `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

7. Run the Code
   Open a new terminal and run:

- `$ rosrun turtlebot3_wilden 001_ReadLaserScan.py`

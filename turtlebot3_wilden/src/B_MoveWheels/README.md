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

- `$ export TURTLEBOT3_MODEL=burger`
- `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`
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
- `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`

5. Run Gazebo

6. Launch the turtlebot3_world.launch
   Open a new terminal and run:

- `$ export TURTLEBOT3_MODEL=burger`
- `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

7. Run the Code
   Open a new terminal and run:

- `$ rosrun turtlebot3_wilden 001_ReadLaserScan.py`

8. Try another code and create a file called 002_ReadLaserScan.py

- `$ roscd turtlebot3_wilden/src`
- `$ touch 002_ReadLaserScan.py`

9. Configuration 002_ReadLaserScan.py File

- Open a 002_ReadLaserScan.py file and write the code
- `$ chmod +x 002_ReadLaserScan.py` change the permissions
- Open a CMakeLists.txt inside turtlebot3_wilden package and edit

```
catkin_install_python(PROGRAMS
  src/001_ReadLaserScan.py
  src/002_ReadLaserScan.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

- `$ roscd ~/catkin_ws`
- `$ catkin_make`

10. Run the Code

- Do no 4, 5, and 6
- `$ rosrun turtlebot3_wilden 002_ReadLaserScan.py`

# `Move the Turtlebot3`

1. Create a file called 001_ReadLaserScan.py

- `$ roscd turtlebot3_wilden/src`
- `$ touch 003_MoveWheels.py`

2. Launch the turtlebot3_world.launch
   Open a terminal and run:

- `$ export TURTLEBOT3_MODEL=burger`
- `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`

3. Find the cmd_vel Topic
   Open a new terminal and run:

- `$ rostopic list` it will list the active topic and find `/cmd_vel` topic
- `$ rostopic info /cmd_vel` show the /cmd_vel topic information
- `$ rosmsg show geometry_msgs/Twist` show the data type

4. Move the turtle with command line

- `$ rostopic pub -r 10 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}'` -r 10 means rate 10Hz
- `$ rostopic pub -1 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}'` -1 means once move or can use --once

5. Move the turtle with python script

- Open a 003_MoveWheels.py file and write the code
- `$ chmod +x 003_MoveWheels.py` change the permissions
- Open a CMakeLists.txt inside turtlebot3_wilden package and edit

```
catkin_install_python(PROGRAMS
  src/001_ReadLaserScan.py
  src/002_ReadLaserScan.py
  src/003_MoveWheels.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

- `$ roscd ~/catkin_ws`
- `$ catkin_make`
- `$ rosrun turtlebot3_wilden 003_MoveWheels.py`

# `How to Get Odometry Data Turtlebot3`

1. Launch the turtlebot3_world.launch
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
- `$ rosrun turtlebot3_wilden 003_MoveWheels.py`

5. Show the /odom message using command line

- `$ rostopic echo /odom -n1`
- `$ rostopic echo /odom`

6. Show the /odom message using python script
   Open a new terminal and run:

- `$ roscd turtlebot3_wilden/src`
- `$ touch 004_ShowOdometryInfo.py`
- `$ chmod +x 004_ShowOdometryInfo.py` change the permissions
- Open a CMakeLists.txt inside turtlebot3_wilden package and edit

```
catkin_install_python(PROGRAMS
  src/001_ReadLaserScan.py
  src/002_ReadLaserScan.py
  src/003_MoveWheels.py
  src/004_ShowOdometryInfo.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

- Open a 004_ShowOdometryInfo.py file and write the code
- `$ roscd ~/catkin_ws`
- `$ catkin_make`
- `$ rosrun turtlebot3_wilden 004_ShowOdometryInfo.py`

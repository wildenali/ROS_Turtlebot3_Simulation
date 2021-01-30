# `Odometry`

## Show Odometry Info

1. Create a file called C01_ShowOdometryInfo.py

   - `$ roscd turtlebot3_wilden/src/C_Odometry`
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
   - `$ rostopic echo /odom -n1`
   - `$ rostopic echo /odom`

4. Launch the teleop
   Open a new terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

5. Show the /odom message using python script
   Open a new terminal and run:

   - Open a C01_ShowOdometryInfo.py file and write the code
   - `$ chmod +x C01_ShowOdometryInfo.py` change the permissions
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/C_Odometry/C01_ShowOdometryInfo.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a C01_ShowOdometryInfo.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden C01_ShowOdometryInfo.py`

## Square Movement

1. Create a file called C02_SquareMovementBasedOnOdometry.py

   - `$ roscd turtlebot3_wilden/src/C_Odometry`
   - `$ touch C02_SquareMovementBasedOnOdometry.py`

2. Launch the turtlebot3_stage_1.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_stage_1.launch`

3. Find the /odom Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /odom`
   - `$ rosmsg show nav_msgs/Odometry`

4. Find the cmd_vel Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /cmd_vel`
   - `$ rosmsg show geometry_msgs/Twist`

5. Show the /odom message using python script
   Open a new terminal and run:

   - Open a C02_SquareMovementBasedOnOdometry.py file and write the code
   - `$ roscd turtlebot3_wilden/src/C_Odometry`
   - `$ chmod +x C02_SquareMovementBasedOnOdometry.py` change the permissions
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/C_Odometry/C02_SquareMovementBasedOnOdometry.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a C02_SquareMovementBasedOnOdometry.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden C02_SquareMovementBasedOnOdometry.py`

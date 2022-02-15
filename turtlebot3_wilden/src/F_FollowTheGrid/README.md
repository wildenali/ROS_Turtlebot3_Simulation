# `FollowTheGrid`

## F01_FollowTheGrid_Y_Axis

1. Create a file called F01_FollowTheGrid_Y_Axis.py

   - `$ roscd turtlebot3_wilden/src`
   - `$ mkdir F_FollowTheGrid`
   - `$ roscd turtlebot3_wilden/src/F_FollowTheGrid`
   - `$ touch F01_FollowTheGrid_Y_Axis.py`
   - `$ chmod +x F01_FollowTheGrid_Y_Axis.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch`

3. Find the /odom Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /odom`
   - `$ rosmsg show nav_msgs/Odometry`
   - `$ rostopic echo /odom`

4. Show the /odom message using python script
   Open a new terminal and run:

   - Open a F01_FollowTheGrid_Y_Axis.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/F_FollowTheGrid/F01_FollowTheGrid_Y_Axis.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a F01_FollowTheGrid_Y_Axis.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden F01_FollowTheGrid_Y_Axis.py`


## F02_FollowTheGrid_X_Axis

1. Create a file called F02_FollowTheGrid_X_Axis.py

   - `$ roscd turtlebot3_wilden/src`
   - `$ mkdir F_FollowTheGrid`
   - `$ roscd turtlebot3_wilden/src/F_FollowTheGrid`
   - `$ touch F02_FollowTheGrid_X_Axis.py`
   - `$ chmod +x F02_FollowTheGrid_X_Axis.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch`

3. Find the /odom Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /odom`
   - `$ rosmsg show nav_msgs/Odometry`
   - `$ rostopic echo /odom`

4. Show the /odom message using python script
   Open a new terminal and run:

   - Open a F02_FollowTheGrid_X_Axis.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/F_FollowTheGrid/F02_FollowTheGrid_X_Axis.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a F02_FollowTheGrid_X_Axis.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden F02_FollowTheGrid_X_Axis.py`

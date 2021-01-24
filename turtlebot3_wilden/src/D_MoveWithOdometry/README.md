# `Make Various of Movement Based on Odometry`

In this part we learn how to make various of movement like make squre, triangel, circle etc movement

### Square

1. Create a file called D01_Square.py

   - `$ roscd turtlebot3_wilden/src/D_MoveWithOdometry`
   - `$ touch D01_Square.py`

2. Launch the turtlebot3_stage_1.launch.launch
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

   - Open a D01_Square.py file and write the code
   - `$ roscd turtlebot3_wilden/src/D_MoveWithOdometry`
   - `$ chmod +x D01_Square.py` change the permissions
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
   src/D_MoveWithOdometry/D01_Square.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a D01_Square.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ rosrun turtlebot3_wilden D01_Square.py`

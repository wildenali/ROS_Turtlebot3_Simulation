# `Maze Solving`

## D01_ReachCertainPosition

How to move the robot to certain position using odometry for position and euler, atan2 for desired angle

1. Create a file called D01_ReachCertainPosition.py

   - `$ roscd turtlebot3_wilden/src/D_MazeSolving`
   - `$ touch D01_ReachCertainPosition.py`
   - `$ chmod +x D01_ReachCertainPosition.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch`

3. Find the /odom Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /odom`
   - `$ rosmsg show nav_msgs/Odometry`
   - `$ rostopic echo /odom -n1`
   - `$ rostopic echo /odom`

4. Move to certain point using python script
   Open a new terminal and run:

   - Open a D01_ReachCertainPosition.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/D_MazeSolving/D01_ReachCertainPosition.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a D01_ReachCertainPosition.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden D01_ReachCertainPosition.py`

## D02_OneWaypoinAndHeading

How to move the robot to certain position using odometry for position and euler, atan2 for desired angle

1. Create a file called D02_OneWaypoinAndHeading.py

   - `$ roscd turtlebot3_wilden/src/D_MazeSolving`
   - `$ touch D02_OneWaypoinAndHeading.py`
   - `$ chmod +x D02_OneWaypoinAndHeading.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch`

3. Find the /odom Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /odom`
   - `$ rosmsg show nav_msgs/Odometry`
   - `$ rostopic echo /odom -n1`
   - `$ rostopic echo /odom`

4. Move to certain point using python script
   Open a new terminal and run:

   - Open a D02_OneWaypoinAndHeading.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/D_MazeSolving/D02_OneWaypoinAndHeading.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a D02_OneWaypoinAndHeading.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden D02_OneWaypoinAndHeading.py`

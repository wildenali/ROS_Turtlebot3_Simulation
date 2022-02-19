# `FollowTheGrid`

## Create the Map and Navigation Stack

1. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

2. Open a new tab, run, and try to move the robot
   - `$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py`
   atau
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

3. Create the Map (Skip this step if you already created the map)
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping`
   atau
   - `$ roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch`
   - `$ rosrun gmapping slam_gmapping scan:=base_scan`

4. Save the Map
    - `$ rosrun map_server map_saver -f ~/map`

5. Run Navigation Node (run the map)
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml`
   - note: install `$ sudo apt-get install ros-noetic-map-server` if ERROR: cannot launch node of type [map_server/map_server]: map_server
   - note: install `$ sudo apt install ros-noetic-amcl` if ERROR: cannot launch node of type [amcl/amcl]: amcl
   - note: install `$ sudo apt install ros-noetic-move-base` if ERROR: cannot launch node of type [move_base/move_base]: move_base
   - if Error Failed to create the dwa_local_planner/DWAPlannerROS then install`$ sudo apt-get install ros-indigo-dwa-local-planner`

6. Move the turtlebot3 using 2D Pose Estimation until same as in Gazebo
7. Desire the point turtlebot3 going to using 2D Nav Goal button


## G01_MoveBaseGoal

1. Create a file called G01_MoveBaseGoal.py

   - `$ roscd turtlebot3_wilden/src`
   - `$ mkdir G_Navigation`
   - `$ roscd turtlebot3_wilden/src/G_Navigation`
   - `$ touch G01_MoveBaseGoal.py`
   - `$ chmod +x G01_MoveBaseGoal.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

3. Run Navigation Node (run the rviz and map)
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml`

4. Create a Code and Configuration
   Open a new terminal and run:

   - Open a G01_MoveBaseGoal.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/G_Navigation/G01_MoveBaseGoal.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a G01_MoveBaseGoal.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ rosrun turtlebot3_wilden G01_MoveBaseGoal.py`


## G02_SequentialGoal

1. Create a file called G02_SequentialGoal.py

   - `$ roscd turtlebot3_wilden/src/G_Navigation`
   - `$ touch G02_SequentialGoal.py`
   - `$ chmod +x G02_SequentialGoal.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

3. Run Navigation Node (run the rviz and map)
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml`

4. Create a Code and Configuration
   Open a new terminal and run:

   - Open a G02_SequentialGoal.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/G_Navigation/G02_SequentialGoal.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a G02_SequentialGoal.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ rosrun turtlebot3_wilden G02_SequentialGoal.py`
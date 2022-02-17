# `FollowTheGrid`

## G01_ReadLocalPlanner

1. Create a file called G01_ReadLocalPlanner.py

   - `$ roscd turtlebot3_wilden/src`
   - `$ mkdir G_PathPlanning`
   - `$ roscd turtlebot3_wilden/src/G_PathPlanning`
   - `$ touch G01_ReadLocalPlanner.py`
   - `$ chmod +x G01_ReadLocalPlanner.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

3. Open a new tab, run, and try to move the robot
   - `$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py`
   atau
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

4. Create the Map (Skip this step if you already created the map)
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping`
   atau
   - `$ roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch`
   - `$ rosrun gmapping slam_gmapping scan:=base_scan`

5. Run Navigation Node (run the map)
   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map.yaml`
   - note: install `$ sudo apt-get install ros-noetic-map-server` if ERROR: cannot launch node of type [map_server/map_server]: map_server
   - note: install `$ sudo apt install ros-noetic-amcl` if ERROR: cannot launch node of type [amcl/amcl]: amcl
   - note: install `$ sudo apt install ros-noetic-move-base` if ERROR: cannot launch node of type [move_base/move_base]: move_base
   - if Error Failed to create the dwa_local_planner/DWAPlannerROS then install`$ sudo apt-get install ros-indigo-dwa-local-planner`

4. Show the /odom message using python script
   Open a new terminal and run:

   - Open a G01_ReadLocalPlanner.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/G_PathPlanning/G01_ReadLocalPlanner.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a G01_ReadLocalPlanner.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden G01_ReadLocalPlanner.py`
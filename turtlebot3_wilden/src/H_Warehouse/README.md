## Create the Map and Navigation Stack

1. Launch the turtlebot3_empty_world.launch (edited)
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

2. Open a new tab, run, and try to move the robot
   - `$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py`
   atau
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

3. Create the Map (Skip this step if you already created the map)
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_slam turtlebot3_slam.launch slam_methods:=gmapping`
   atau
   - `$ roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch`
   - `$ rosrun gmapping slam_gmapping scan:=base_scan`

4. Save the Map
    - `$ rosrun map_server map_saver -f ~/map_warehouse`

5. Run Navigation Node (run the map)
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_warehouse.yaml`
   - note: install `$ sudo apt-get install ros-noetic-map-server` if ERROR: cannot launch node of type [map_server/map_server]: map_server
   - note: install `$ sudo apt install ros-noetic-amcl` if ERROR: cannot launch node of type [amcl/amcl]: amcl
   - note: install `$ sudo apt install ros-noetic-move-base` if ERROR: cannot launch node of type [move_base/move_base]: move_base
   - if Error Failed to create the dwa_local_planner/DWAPlannerROS then install`$ sudo apt-get install ros-indigo-dwa-local-planner`

6. Move the turtlebot3 using 2D Pose Estimation until same as in Gazebo
7. Desire the point turtlebot3 going to using 2D Nav Goal button


## Get the waypoint

1. Launch the turtlebot3_empty_world.launch (edited)
   Open a terminal and run:
   - `$ cd catkin_ws`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`

2. Open a new tab, run, and try to move the robot
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

3. Run Navigation Node (run the map)
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_warehouse.yaml`

4. Find the /odom Topic
   Open a new terminal and run:
   - `$ rostopic list`
   - `$ rostopic info /odom`
   - `$ rosmsg show nav_msgs/Odometry`
   - `$ rostopic echo -n1 /odom`

A1:
pose: 
  pose: 
    position: 
      x: -0.70
      y: -1.5
      z: 0.00
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A2:
pose: 
  pose: 
    position: 
      x: -0.35
      y: -1.5
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A3:
pose: 
  pose: 
    position: 
      x: 0.5
      y: -1.5
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A4:
pose: 
  pose: 
    position: 
      x: 0.7
      y: -1.5
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A5:
pose: 
  pose: 
    position: 
      x: 0.7
      y: -0.7
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A6:
pose: 
  pose: 
    position: 
      x: 0.4
      y: -0.7
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A7:
pose: 
  pose: 
    position: 
      x: -0.35
      y: -0.7
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A8:
pose: 
  pose: 
    position: 
      x: -0.7
      y: -0.7
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A9:
pose: 
  pose: 
    position: 
      x: -0.7
      y: -0.3
      z: 0.00
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A10:
pose: 
  pose: 
    position: 
      x: -0.35
      y: -0.3
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A11:
pose: 
  pose: 
    position: 
      x: 0.5
      y: -0.3
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A12:
pose: 
  pose: 
    position: 
      x: 0.7
      y: -0.3
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A13:
pose: 
  pose: 
    position: 
      x: 0.7
      y: 0.3
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A14:
pose: 
  pose: 
    position: 
      x: 0.4
      y: 0.3
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A15:
pose: 
  pose: 
    position: 
      x: -0.35
      y: 0.3
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A16:
pose: 
  pose: 
    position: 
      x: -0.7
      y: 0.3
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A17:
pose: 
  pose: 
    position: 
      x: -0.70
      y: 0.7
      z: 0.00
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A18:
pose: 
  pose: 
    position: 
      x: -0.35
      y: 0.7
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A19:
pose: 
  pose: 
    position: 
      x: 0.5
      y: 0.7
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A20:
pose: 
  pose: 
    position: 
      x: 0.7
      y: 0.7
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: 0.707440592144

A21:
pose: 
  pose: 
    position: 
      x: 0.7
      y: 1.5
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A22:
pose: 
  pose: 
    position: 
      x: 0.4
      y: 1.5
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A23:
pose: 
  pose: 
    position: 
      x: -0.35
      y: 1.5
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144

A24:
pose: 
  pose: 
    position: 
      x: -0.7
      y: 1.5
      z: 0.0
    orientation: 
      x: 0.00
      y: 0.00
      z: 0.706771021148
      w: -0.707440592144



## H01_WaypointWithoutMoveBase

1. Create a file called H01_WaypointWithoutMoveBase.py

   - `$ roscd turtlebot3_wilden/src/H_Warehouse`
   - `$ touch H01_WaypointWithoutMoveBase.py`
   - `$ chmod +x H01_WaypointWithoutMoveBase.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

3. Run Navigation Node (run the map)
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_warehouse.yaml`

4. Create a Code and Configuration
   Open a new terminal and run:

   - Open a H01_WaypointWithoutMoveBase.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/H_Warehouse/H01_WaypointWithoutMoveBase.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a H01_WaypointWithoutMoveBase.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ rosrun turtlebot3_wilden H01_WaypointWithoutMoveBase.py`

## H02_HowToUseQuaternion

This tutorial about how to use quaternion to desired POSE position and orientation from data

1. Create a file called H02_HowToUseQuaternion.py

   - `$ roscd turtlebot3_wilden/src/H_Warehouse`
   - `$ touch H02_HowToUseQuaternion.py`
   - `$ chmod +x H02_HowToUseQuaternion.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ cd ~/catkin_ws`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

3. Run Navigation Node (run the map)
   - `$ cd ~/catkin_ws`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_warehouse.yaml`

4. Create a Code and Configuration
   Open a new terminal and run:

   - Open a H02_HowToUseQuaternion.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/H_Warehouse/H02_HowToUseQuaternion.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a H02_HowToUseQuaternion.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ rosrun turtlebot3_wilden H02_HowToUseQuaternion.py`


## H03_WaypointWithoutMoveBaseUseList

1. Create a file called H03_WaypointWithoutMoveBaseUseList.py

   - `$ roscd turtlebot3_wilden/src/H_Warehouse`
   - `$ touch H03_WaypointWithoutMoveBaseUseList.py`
   - `$ chmod +x H03_WaypointWithoutMoveBaseUseList.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ cd ~/catkin_ws`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

3. Run Navigation Node (run the map)
   - `$ cd ~/catkin_ws`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_warehouse.yaml`

4. Create a Code and Configuration
   Open a new terminal and run:

   - Open a H03_WaypointWithoutMoveBaseUseList.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/H_Warehouse/H03_WaypointWithoutMoveBaseUseList.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a H03_WaypointWithoutMoveBaseUseList.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ rosrun turtlebot3_wilden H03_WaypointWithoutMoveBaseUseList.py`


## H04_MultiWaypointWithoutMoveBaseUseList

1. Create a file called H04_MultiWaypointWithoutMoveBaseUseList.py
   - `$ cd catkin_ws/src/ROS_Turtlebot3_Simulation/turtlebot3_wilden/src/H_Warehouse`
   - `$ touch H04_MultiWaypointWithoutMoveBaseUseList.py`
   - `$ chmod +x H04_MultiWaypointWithoutMoveBaseUseList.py` change the permissions

2. Launch the turtlebot3_empty_world.launch
   Open a terminal and run:

   - `$ cd ~/catkin_ws`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch` 

3. Run Navigation Node (run the map)
   - `$ cd ~/catkin_ws`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ roslaunch turtlebot3_navigation turtlebot3_navigation.launch map_file:=$HOME/map_warehouse.yaml`

4. Create a Code and Configuration
   Open a new terminal and run:

   - Open a H04_MultiWaypointWithoutMoveBaseUseList.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/H_Warehouse/H04_MultiWaypointWithoutMoveBaseUseList.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a H04_MultiWaypointWithoutMoveBaseUseList.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ export TURTLEBOT3_MODEL=waffle`
   - `$ rosrun turtlebot3_wilden H04_MultiWaypointWithoutMoveBaseUseList.py`

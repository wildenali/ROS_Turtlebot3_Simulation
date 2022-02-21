# `Velocity`

## B01_MoveWheels

Move the Turtlebot using Velocity Command

1. Create a file called B01_MoveWheels.py

   - `$ roscd turtlebot3_wilden/src/B_Velocity`
   - `$ touch B01_MoveWheels.py`

2. Launch the turtlebot3_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`

3. Find the cmd_vel Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /cmd_vel`
   - `$ rosmsg show geometry_msgs/Twist`

4. Move the turtle with command line

   - `$ rostopic pub -r 10 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}'` -r 10 means rate 10Hz
   - `$ rostopic pub -1 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}'` -1 means once move or can use --once
   - `$ rostopic pub -1 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.0}}'` -1 means once move or can use --once

5. Move the turtle with python script

   - Open a B01_MoveWheels.py file and write the code
   - `$ chmod +x B01_MoveWheels.py` change the permissions
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/B_Velocity/B01_MoveWheels.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - `$ roscd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden B01_MoveWheels.py`

## B02_AccelVelocity

Acceleration velocity using array in the twist

1. Create a file called B02_AccelVelocity.py

   - `$ roscd turtlebot3_wilden/src/B_Velocity`
   - `$ touch B02_AccelVelocity.py`

2. Launch the turtlebot3_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_state_1.launch`

3. Find the cmd_vel Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /cmd_vel`
   - `$ rosmsg show geometry_msgs/Twist`

4. Move the turtle with python script

   - `$ roscd turtlebot3_wilden/src/B_Velocity`
   - `$ chmod +x B02_AccelVelocity.py`
   - Open a B02_AccelVelocity.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/B_Velocity/B02_AccelVelocity.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - `$ roscd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden B02_AccelVelocity.py`

## B03_StopUsingTimer

How to stop the robot using timer

The topics used are:
/cmd_vel
/clock

1. Create a file called B03_StopUsingTimer.py

   - `$ roscd turtlebot3_wilden/src/B_Velocity`
   - `$ touch B03_StopUsingTimer.py`
   - `$ chmod +x B03_StopUsingTimer.py`

2. Launch the turtlebot3_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch`

3. Find the cmd_vel Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /cmd_vel`
   - `$ rosmsg show geometry_msgs/Twist`

4. Find the clock Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /clock`
   - `$ rosmsg show rosgraph_msgs/Clock`

5. Move the turtle with python script

   - `$ roscd turtlebot3_wilden/src/B_Velocity`
   - Open a B03_StopUsingTimer.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/B_Velocity/B03_StopUsingTimer.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - `$ roscd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden B03_StopUsingTimer.py`

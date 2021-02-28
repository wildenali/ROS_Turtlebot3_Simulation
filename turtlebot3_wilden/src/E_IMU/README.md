# `IMU`

## E01_ReadIMU

1. Create a file called E01_ReadIMU.py

   - `$ roscd turtlebot3_wilden/src`
   - `$ mkdir E_IMU`
   - `$ roscd turtlebot3_wilden/src/E_IMU`
   - `$ touch E01_ReadIMU.py`
   - `$ chmod +x E01_ReadIMU.py` change the permissions

2. Launch the turtlebot3_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`

3. Find the /imu Topic
   Open a new terminal and run:

   - `$ rostopic list`
   - `$ rostopic info /imu`
   - `$ rosmsg show sensor_msgs/Imu`
   - `$ rostopic echo /imu -n1`
   - `$ rostopic echo /imu`

4. Show the /odom message using python script
   Open a new terminal and run:

   - Open a E01_ReadIMU.py file and write the code
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/E_IMU/E01_ReadIMU.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - Open a E01_ReadIMU.py file and write the code
   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`
   - `$ rosrun turtlebot3_wilden E01_ReadIMU.py`

5. Launch the teleop
   Open a new terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

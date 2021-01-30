# `Laser Scanner Lidar`

## Measured the Distance

1. Create a file called A01_ReadLaserScan.py

   - `$ roscd turtlebot3_wilden/src/A_LaserScanner`
   - `$ touch A01_ReadLaserScan.py`

2. Find the Laser Scanner Lidar Topic

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`
   - `$ rostopic list` it will list the active topic and find `scan` topic
   - `$ rostopic info /scan` show the /scan topic information
   - `$ rosmsg show sensor_msgs/LaserScan` show the data type
   - `$ rostopic echo /scan` looping print messages to screen
   - `$ rostopic echo /scan -n1` just once print messages to screen

3. Create a Code and Configuration

   - Open a A01_ReadLaserScan.py file and write the code
   - `$ chmod +x A01_ReadLaserScan.py` change the permissions
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
       src/A_LaserScanner/A01_ReadLaserScan.py
       DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`

4. Launch the turtlebot3_world.launch
   Open a terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`

5. Launch the turtlebot3_world.launch
   Open a new terminal and run:

   - `$ export TURTLEBOT3_MODEL=burger`
   - `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`

6. Run the Code
   Open a new terminal and run:

   - `$ rosrun turtlebot3_wilden A01_ReadLaserScan.py`

7. Try another code and create a file called A02_ReadLaserScan.py

   - `$ roscd turtlebot3_wilden/src/A_LaserScanner`
   - `$ touch A02_ReadLaserScan.py`

8. Configuration A02_ReadLaserScan.py File

   - Open a A02_ReadLaserScan.py file and write the code
   - `$ chmod +x A02_ReadLaserScan.py` change the permissions
   - Open a CMakeLists.txt inside turtlebot3_wilden package and edit

   ```
   catkin_install_python(PROGRAMS
   # src/A_LaserScanner/A01_ReadLaserScan.py
   src/A_LaserScanner/A02_ReadLaserScan.py
   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
   )
   ```

   - `$ cd ~/catkin_ws`
   - `$ catkin_make`
   - `$ source devel/setup.bash`

9. Run the Code

   - Do no 4, and 5
   - `$ rosrun turtlebot3_wilden A02_ReadLaserScan.py`

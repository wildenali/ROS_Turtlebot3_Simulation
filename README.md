# ROS_Turlebot

# Install Turtlebot3 Packages
- `$ source /opt/ros/kinetic/setup.bash`
- `$ sudo apt-get install ros-kinetic-turtlebot3-msgs`
- `$ sudo apt-get install ros-kinetic-turtlebot3`

or

- `$ sudo apt-get remove ros-kinetic-turtlebot3-msgs`
- `$ sudo apt-get remove ros-kinetic-turtlebot3`
- `$ mkdir -p ~/catkin_ws/src`
- `$ cd ~/catkin_ws/src/`
- `$ git clone -b kinetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git`
- `$ git clone -b kinetic-devel https://github.com/ROBOTIS-GIT/turtlebot3.git`
- `$ cd ~/catkin_ws && catkin_make`
- `$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc`

# Set Turtlebot3 Model Name
- `$ echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc`
or
- `$ echo "export TURTLEBOT3_MODEL=waffle_pi" >> ~/.bashrc`

# Install Simulation Package
- `git clone -b kinetic-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git`
- `cd ~/catkin_ws && catkin_make`

# Launch Simulation World
- Change the turtlebot3_empty_world.launch file
from <br>
<!-- <arg name="model" default="$(env TURTLEBOT3_MODEL)" doc="model type [burger, waffle, waffle_pi]"/> -->

<arg name="model" default="burger" doc="model type [burger, waffle, waffle_pi]"/>
or

- `$ export TURTLEBOT3_MODEL=burger`

- Run:
`$ roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch`

# Launch Teleop
- `$ export TURTLEBOT3_MODEL=burger`
- `$ roslaunch turtlebot3_teleop turtlebot3_teleop_key.launch`
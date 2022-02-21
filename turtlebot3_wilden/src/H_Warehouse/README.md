1. Edit file model.sdf in turtlebot3_gazebo/models/turtlebot3_world/model.sdf

`
<sdf version='1.5'>
    <!-- Draw Circle -->
    <model name='ros_symbol'>
      <static>1</static>
      <link name='symbol'>

        <collision name='meja_no_1'>
          <pose>-2.6-0.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_1'>
          <pose>-2.6 -0.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_2'>
          <pose>-2.6 0.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_2'>
          <pose>-2.6 0.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_3'>
          <pose>-2.6 0.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_3'>
          <pose>-2.6 0.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_A1'>
          <pose>-1.0 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_A1'>
          <pose>-1.0 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_A2'>
          <pose>-0.6 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_A2'>
          <pose>-0.6 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_A3'>
          <pose>-0.2 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_A3'>
          <pose>-0.2 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_A4'>
          <pose>0.2 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_A4'>
          <pose>0.2 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_A5'>
          <pose>0.6 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_A5'>
          <pose>0.6 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_A6'>
          <pose>1.0 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_A6'>
          <pose>1.0 -2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_B1'>
          <pose>-1.0 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_B1'>
          <pose>-1.0 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_B2'>
          <pose>-0.6 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_B2'>
          <pose>-0.6 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_B3'>
          <pose>-0.2 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_B3'>
          <pose>-0.2 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_B4'>
          <pose>0.2 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_B4'>
          <pose>0.2 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_B5'>
          <pose>0.6 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_B5'>
          <pose>0.6 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>
        
        <collision name='meja_no_C1'>
          <pose>-1.0 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_C1'>
          <pose>-1.0 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_C2'>
          <pose>-0.6 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_C2'>
          <pose>-0.6 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_C3'>
          <pose>-0.2 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_C3'>
          <pose>-0.2 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_C4'>
          <pose>0.2 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_C4'>
          <pose>0.2 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_C5'>
          <pose>0.6 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_C5'>
          <pose>0.6 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_D1'>
          <pose>-1.0 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_D1'>
          <pose>-1.0 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_D2'>
          <pose>-0.6 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_D2'>
          <pose>-0.6 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_D3'>
          <pose>-0.2 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_D3'>
          <pose>-0.2 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_D4'>
          <pose>0.2 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_D4'>
          <pose>0.2 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_D5'>
          <pose>0.6 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_D5'>
          <pose>0.6 0.8 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_E1'>
          <pose>-1.0 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_E1'>
          <pose>-1.0 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_E2'>
          <pose>-0.6 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_E2'>
          <pose>-0.6 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_E3'>
          <pose>-0.2 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_E3'>
          <pose>-0.2 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_E4'>
          <pose>0.2 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_E4'>
          <pose>0.2 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_E5'>
          <pose>0.6 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_E5'>
          <pose>0.6 1.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_F1'>
          <pose>-1.0 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_F1'>
          <pose>-1.0 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_F2'>
          <pose>-0.6 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_F2'>
          <pose>-0.6 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_F3'>
          <pose>-0.2 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_F3'>
          <pose>-0.2 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_F4'>
          <pose>0.2 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_F4'>
          <pose>0.2 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_F5'>
          <pose>0.6 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_F5'>
          <pose>0.6 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_F6'>
          <pose>1.0 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_F6'>
          <pose>1.0 2.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_G1'>
          <pose>2.0 1.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_G1'>
          <pose>2.0 1.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_G2'>
          <pose>2.0 1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_G2'>
          <pose>2.0 1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_G3'>
          <pose>2.0 0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_G3'>
          <pose>2.0 0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_G4'>
          <pose>2.0 0.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_G4'>
          <pose>2.0 0.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>
        
        <collision name='meja_no_G5'>
          <pose>2.0 -0.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_G5'>
          <pose>2.0 -0.2 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_G6'>
          <pose>2.0 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_G6'>
          <pose>2.0 -0.6 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>
        
        <collision name='meja_no_G7'>
          <pose>2.0 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_G7'>
          <pose>2.0 -1.0 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <collision name='meja_no_G8'>
          <pose>2.0 -1.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='meja_no_G8'>
          <pose>2.0 -1.4 0.1 0 0 0</pose>
          <geometry>
            <box>
              <size>0.3 0.3 0.20</size>
            </box>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/White</name>
            </script>
          </material>
        </visual>

        <!-- Draw Hexagon -->
        <collision name='head'>
          <pose>3.5 0 -0.5 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.8 0.8 0.8</scale>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='head'>
          <pose>3.5 0 -0.5 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.8 0.8 0.8</scale>
            </mesh>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Green</name>
            </script>
          </material>
        </visual>

        <collision name='left_hand'>
          <pose>1.8 2.7 0 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.55 0.55 0.55</scale>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='left_hand'>
          <pose>1.8 2.7 0 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.55 0.55 0.55</scale>
            </mesh>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Green</name>
            </script>
          </material>
        </visual>

        <collision name='right_hand'>
          <pose>1.8 -2.7 0 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.55 0.55 0.55</scale>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='right_hand'>
          <pose>1.8 -2.7 0 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.55 0.55 0.55</scale>
            </mesh>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Green</name>
            </script>
          </material>
        </visual>

        <collision name='left_foot'>
          <pose>-1.8 2.7 0 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.55 0.55 0.55</scale>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='left_foot'>
          <pose>-1.8 2.7 0 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.55 0.55 0.55</scale>
            </mesh>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Green</name>
            </script>
          </material>
        </visual>

        <collision name='right_foot'>
          <pose>-1.8 -2.7 0 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.55 0.55 0.55</scale>
            </mesh>
          </geometry>
          <max_contacts>10</max_contacts>
          <surface>
            <bounce/>
            <friction>
              <ode/>
            </friction>
            <contact>
              <ode/>
            </contact>
          </surface>
        </collision>

        <visual name='right_foot'>
          <pose>-1.8 -2.7 0 0 0 0</pose>
          <geometry>
            <mesh>
              <uri>model://turtlebot3_world/meshes/hexagon.dae</uri>
              <scale>0.55 0.55 0.55</scale>
            </mesh>
          </geometry>
          <material>
            <script>
              <uri>file://media/materials/scripts/gazebo.material</uri>
              <name>Gazebo/Green</name>
            </script>
          </material>
        </visual>

        <!-- Draw Wall -->
        <collision name='body'>
        <pose>0 0 -0.3 0 0 -1.5708</pose>
        <geometry>
          <mesh>
            <uri>model://turtlebot3_world/meshes/wall.dae</uri>
            <scale>0.25 0.25 0.25</scale>
          </mesh>
        </geometry>
        <max_contacts>10</max_contacts>
        <surface>
          <bounce/>
          <friction>
            <ode/>
          </friction>
          <contact>
            <ode/>
          </contact>
        </surface>
      </collision>

      <visual name='body'>
        <pose>0 0 -0.3 0 0 -1.5708</pose>
        <geometry>
          <mesh>
            <uri>model://turtlebot3_world/meshes/wall.dae</uri>
            <scale>0.25 0.25 0.25</scale>
          </mesh>
        </geometry>
        <material>
          <script>
            <uri>file://media/materials/scripts/gazebo.material</uri>
            <name>Gazebo/FlatBlack</name>
          </script>
        </material>
      </visual>
    </link>
  </model>
</sdf>

`

- `$ export TURTLEBOT3_MODEL=waffle`
- `$ source devel/setup.bash`
- `$ roslaunch turtlebot3_gazebo turtlebot3_world.launch`


## Create the Map and Navigation Stack

1. Launch the turtlebot3_empty_world.launch
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


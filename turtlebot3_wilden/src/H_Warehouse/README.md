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
      x: -1.9
      y: 0.4
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.999933589754
      w: -0.011414187123

A2:
pose: 
  pose: 
    position: 
      x: -1.9
      y: 0.0
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.999933589754
      w: -0.011414187123

A3:
pose: 
  pose: 
    position: 
      x: -1.9
      y: -0.4
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.999933589754
      w: -0.011414187123

B1:
pose: 
  pose: 
    position: 
      x: -0.9
      y: -1.9
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.712404379097
      w: 0.701767389226

B2:
pose: 
  pose: 
    position: 
      x: -0.6
      y: -1.9
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.73314243972
      w: -0.680073253102

B3:
pose: 
  pose: 
    position: 
      x: -0.2
      y: -1.9
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.678606138054
      w: 0.734500630411

B4:
pose: 
  pose: 
    position: 
      x: 0.2
      y: -1.9
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.690492640808
      w: -0.723337668471

B5:
pose: 
  pose: 
    position: 
      x: 0.6
      y: -1.9
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.709203098062
      w: 0.70500243582

B6:
pose: 
  pose: 
    position: 
      x: 0.9
      y: -1.9
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.699311081634
      w: 0.714815695103

C1:
pose: 
  pose: 
    position: 
      x: -0.9
      y: -1.5
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.704594837174
      w: 0.709608048616

C2:
pose: 
  pose: 
    position: 
      x: -0.6
      y: -1.5
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.704594837174
      w: 0.709608048616

C3:
pose: 
  pose: 
    position: 
      x: -0.2
      y: -1.5
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.704594837174
      w: 0.709608048616

C4:
pose: 
  pose: 
    position: 
      x: 0.2
      y: -1.5
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.704594837174
      w: 0.709608048616

C5:
pose: 
  pose: 
    position: 
      x: 0.6
      y: -1.5
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.709497026881
      w: 0.704706629111

D1:
pose: 
  pose: 
    position: 
      x: -0.9
      y: -0.1
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.708106699157
      w: -0.706103651688

D2:
pose: 
  pose: 
    position: 
      x: -0.6
      y: -0.1
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.708106699157
      w: -0.706103651688

D3:
pose: 
  pose: 
    position: 
      x: -0.2
      y: -0.1
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.708106699157
      w: -0.706103651688

D4:
pose: 
  pose: 
    position: 
      x: 0.2
      y: -0.1
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.708106699157
      w: -0.706103651688

D5:
pose: 
  pose: 
    position: 
      x: 0.6
      y: -0.1
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.708106699157
      w: -0.706103651688

E1:
pose: 
  pose: 
    position: 
      x: -1.0
      y: 0.28
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

E2:
pose: 
  pose: 
    position: 
      x: -0.6
      y: -0.28
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

E3:
pose: 
  pose: 
    position: 
      x: -0.2
      y: 0.28
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

E4:
pose: 
  pose: 
    position: 
      x: 0.2
      y: 0.28
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

E5:
pose: 
  pose: 
    position: 
      x: 0.6
      y: 0.28
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

F1:
pose: 
  pose: 
    position: 
      x: -1.0
      y: 1.68
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.702925341896
      w: 0.711261862277

F2:
pose: 
  pose: 
    position: 
      x: -0.6
      y: 1.68
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.702925341896
      w: 0.711261862277

F3:
pose: 
  pose: 
    position: 
      x: -0.2
      y: 1.68
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.702925341896
      w: 0.711261862277

F4:
pose: 
  pose: 
    position: 
      x: 0.2
      y: 1.68
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.702925341896
      w: 0.711261862277

F5:
pose: 
  pose: 
    position: 
      x: 0.6
      y: 1.68
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: -0.702925341896
      w: 0.711261862277

G1:
pose: 
  pose: 
    position: 
      x: -1.0
      y: 1.88
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

G2:
pose: 
  pose: 
    position: 
      x: -0.6
      y: 1.88
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

G3:
pose: 
  pose: 
    position: 
      x: -0.2
      y: 1.88
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

G4:
pose: 
  pose: 
    position: 
      x: 0.2
      y: 1.88
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

G5:
pose: 
  pose: 
    position: 
      x: 0.6
      y: 1.88
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

G6:
pose: 
  pose: 
    position: 
      x: 0.6
      y: 1.88
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.702925341896
      w: 0.711261862277

H1:
pose: 
  pose: 
    position: 
      x: 1.54
      y: 1.41
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.0115347134045
      w: 0.999932209396

H2:
pose: 
  pose: 
    position: 
      x: 1.54
      y: 1.0
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.0115347134045
      w: 0.999932209396

H3:
pose: 
  pose: 
    position: 
      x: 1.54
      y: 0.6
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.0115347134045
      w: 0.999932209396

H4:
pose: 
  pose: 
    position: 
      x: 1.54
      y: 0.20
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.0115347134045
      w: 0.999932209396

H5:
pose: 
  pose: 
    position: 
      x: 1.54
      y: -0.20
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.0115347134045
      w: 0.999932209396

H6:
pose: 
  pose: 
    position: 
      x: 1.54
      y: -0.6
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.0115347134045
      w: 0.999932209396

H7:
pose: 
  pose: 
    position: 
      x: 1.54
      y: -1.0
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.0115347134045
      w: 0.999932209396

H8:
pose: 
  pose: 
    position: 
      x: 1.54
      y: -1.41
      z: 0.0
    orientation: 
      x: 0.0
      y: 0.0
      z: 0.0115347134045
      w: 0.999932209396



L1:
  x: -1.7
  y: 1.2

L2:
  x: -1.7
  y: 0.8

L3:
  x: -1.7
  y: 0.4

L4:
  x: -1.7
  y: 0.00

L5:
  x: -1.7
  y: -0.4

L6:
  x: -1.7
  y: -0.8

L7:
  x: -1.7
  y: -1.2

L8:
  x: -1.0
  y: -1.7

L9:
  x: -0.6
  y: -1.7

L10:
  x: -0.2
  y: -1.7

L11:
  x: 0.2
  y: -1.7

L12:
  x: 0.6
  y: -1.7

L13:
  x: 1.0
  y: -1.7

L14:
  x: 1.54
  y: -1.41

L15:
  x: 1.54
  y: -1.0

L16:
  x: 1.54
  y: -0.6

L17:
  x: 1.54
  y: -0.2

L18:
  x: 1.54
  y: 0.0

L19:
  x: 1.54
  y: 0.6

L20:
  x: 1.54
  y: 1.0

L21:
  x: 1.54
  y: 1.41

L22:
  x: 1.0
  y: -1.78

L23:
  x: 0.6
  y: -1.78

L24:
  x: 0.2
  y: -1.78

L25:
  x: -0.2
  y: -1.78

L26:
  x: -0.6
  y: -1.78

L27:
  x: -1.0
  y: -1.78

L28:
  x: -0.9
  y: 0.00

L29:
  x: -0.6
  y: 0.00

L30:
  x: -0.2
  y: 0.00

L31:
  x: 0.2
  y: 0.00

L32:
  x: 0.6
  y: 0.00


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

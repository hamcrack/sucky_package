import os

from ament_index_python.packages import get_package_share_directory


from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch_ros.actions import Node

def generate_launch_description():
    # # Declare the world argument
    # declare_world_cmd = DeclareLaunchArgument(
    #     'world',
    #     default_value=os.path.join(get_package_share_directory('gazebo_ros'), 'worlds', 'empty.world'),
    #     description='Full path to the world model file to load'
    # )

    package_name='sucky_package'

    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory(package_name),'launch','robot_state_publisher.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )

    gazebo = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')]),
             )

    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    spawn_entity = Node(package='gazebo_ros', executable='spawn_entity.py',
                        arguments=['-topic', 'robot_description',
                                   '-entity', 'my_bot', '-timeout', '60'],
                        output='screen')


    return LaunchDescription([
        rsp,
        gazebo,
        spawn_entity,
    ])
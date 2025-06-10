import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    # # Declare the world argument
    # declare_world_cmd = DeclareLaunchArgument(
    #     'world',
    #     default_value=os.path.join(get_package_share_directory('gazebo_ros'), 'worlds', 'empty.world'),
    #     description='Full path to the world model file to load'
    # )

    use_sim_time = LaunchConfiguration('use_sim_time')

    pkg_name = 'sucky_package'
    file_subpath = 'description/sucky_robot.urdf.xacro'
    xacro_file = os.path.join(get_package_share_directory(pkg_name), file_subpath)
    robot_description_config = xacro.process_file(xacro_file)
    # robot_description_raw = xacro.process_file(xacro_file).toxml()

    # Create a robot_state_publisher node
    params = {'robot_description': robot_description_config.toxml(), 'use_sim_time': use_sim_time}
    node_robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[params]
    )

    # gazebo = IncludeLaunchDescription(
    #     PythonLaunchDescriptionSource(
    #         os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
    #     ),
    #     launch_arguments={'world': world}.items()
    # )

    # spawn_entity = Node(
    #     package='gazebo_ros',
    #     executable='spawn_entity.py',
    #     arguments=['-topic', 'robot_description', '-entity', 'my_bot'],
    #     output='screen'
    # )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),

        node_robot_state_publisher
    ])
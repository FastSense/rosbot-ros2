import os
import launch_ros.actions
from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

# for rp_lidar
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    use_sim_time = LaunchConfiguration(
        'use_sim_time', default='false')
    rosbot_pkg = get_package_share_directory('rosbot')

    # rplidar_ros_pkg = get_package_share_directory('rplidar_ros')

    rosserial = launch_ros.actions.Node(
        package='rosbot',
        executable='rosserial_node.py',
        output='screen',
        parameters=[
                rosbot_pkg + '/config/rosserial.yaml'
        ]
    )

    rosbot_tf = launch_ros.actions.Node(
        package='rosbot',
        executable='rosbot_tf',
        output='log',
    )

    # rp_lidar = launch.actions.IncludeLaunchDescription(
    #     launch.launch_description_sources.PythonLaunchDescriptionSource(
    #         os.path.join(rplidar_ros_pkg, 'launch', 'rplidar.launch.py'))
    # )

    return LaunchDescription([
        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='false'
        ),
        DeclareLaunchArgument('verbose', default_value='true',
                              description='Set "true" to increase messages written to terminal.'),
        # rp_lidar,
        # laser_frame_tf,
        rosserial,
        rosbot_tf,
        Node(
            package='rosbot_controller',
            executable='publish_rosbot_tf',
            name='publish_rosbot_tf',
            output='screen',
            emulate_tty=True,
        ),

    ])


if __name__ == '__main__':
    generate_launch_description()

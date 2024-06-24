import launch
import launch_ros.actions


def generate_launch_description():
    return launch.LaunchDescription(
        [
            launch_ros.actions.Node(
                package="optitrack",
                executable="publisher_main",
                name="publisher_main",
            )
        ]
    )

cmake_minimum_required(VERSION 2.8.3)
project(odrive_ros)

find_package(catkin REQUIRED)

catkin_python_setup()

find_package(catkin REQUIRED COMPONENTS
  message_generation
  std_msgs
)

add_message_files(FILES
  JointAngleCommand.msg
)

generate_messages(DEPENDENCIES
  std_msgs
)


## Generate dynamic reconfigure parameters in the 'cfg' folder
# generate_dynamic_reconfigure_options(
#    cfg/JointPosition.cfg
# )

catkin_package(
  CATKIN_DEPENDS
  message_runtime
)


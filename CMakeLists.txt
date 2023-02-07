cmake_minimum_required(VERSION 2.8.3)
project(cmd_bridge)

add_compile_options(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  std_msgs
  robotnik_msgs
)

catkin_package(
  LIBRARIES cmd_bridge
  CATKIN_DEPENDS std_msgs robotnik_msgs
)

catkin_install_python(PROGRAMS scripts/hello_world.py scripts/hello_world.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
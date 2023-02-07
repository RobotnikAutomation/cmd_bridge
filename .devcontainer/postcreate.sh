# Update container
sudo apt-get update

# Install debs
#sudo apt-get install -y ${HOME}/deb/*

# Download repos
find ${HOME}/repos/ -type f -exec vcs import --recursive ${ROBOT_WS} --input {} \;

# Download dependencies
local_deps.sh
rosdep install --from-paths ${ROBOT_WS}/src --ignore-src --rosdistro=${ROS_DISTRO} -y -r

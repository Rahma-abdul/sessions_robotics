#! /bin/bash
pwd
source /opt/ros/noetic/setup.bash
echo "Enter path :"
read path
echo "Enter the name of the workspace to create:"
read ws
if  [ -e $ws ]; then
 echo "Filename: $ws already exits , Failed to create workspace"
 exit 1
else 
 echo "Creating workspace : $ws"
 echo $ws/src
 mkdir -p ~/$ws/src
 echo "Workspace created!!! Building Working space"
 cd $ws
 catkin_make
 echo "Workspace Built!!"
 ls 
source devel/setup.bash 
fi
echo "Enter the name of the package: "
read package
cd ~/$ws/src
catkin_create_pkg $package std_mags rospy  

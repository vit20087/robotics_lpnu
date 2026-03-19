# Lab 3: Moving Mobile Robots in ROS 2 and Gazebo Sim
## Installation & Setup
### Clone the repository:
```bash
git clone https://github.com/vit20087/robotics_lpnu.git
```
### Build and run docker:
```bash
./scripts/cmd build-docker
./scripts/cmd run
```
### Build the package:
```bash
cd /opt/ws
rm -rf build/ install/ log/
colcon build --packages-select lab3
source install/setup.bash
```

## How to Run
### 1. Launch Simulation and Visualization
This command starts Gazebo Sim, sets up the ROS-GZ bridges, starts the path publisher, and opens RViz2:
```bash
ros2 launch lab3 bringup.launch.py
```
### 2. Execute Movement
In a new terminal, run the Figure 8 trajectory script:
```bash
ros2 run lab3 figure_8_path
```
### 3. Start Path Visualization
In another terminal start odometry publisher.
```bash
ros2 run lab3 odom_path_publisher
```
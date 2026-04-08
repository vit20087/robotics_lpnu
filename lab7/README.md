# Lab 7: Introduction to Robotics (ROS 2) 🤖

This repository contains the implementation of Laboratory Work No. 7 for the "Introduction to Robotics" course.
**Topic:** Coordinate transforms (TF2), robot description (URDF/Xacro), and the RTR manipulator.

## 📋 Project Description
In this laboratory work, the following concepts are implemented:
- Working with the `tf2` transform tree in ROS 2 (creating `broadcaster` and `listener` nodes).
- 3D model description of the RTR (Revolute-Translational-Revolute) manipulator using parameterized **URDF/Xacro**.
- Adding collision geometry (`<collision>`) for proper physical interaction of the robot links.
- Visualizing the model and transform tree in **RViz2**.
- Controlling joint states via **ROS 2 Control** and verifying the mathematical forward kinematics model.

## 🛠 Requirements
- **OS:** Ubuntu 22.04 (or a Docker container with ROS 2)
- **ROS 2:** Humble / Iron
- Package manager `colcon`
- Installed ROS packages: `ros2_control`, `robot_state_publisher`, `xacro`, `rviz2`, `tf2_ros`

## 🚀 Building the Project

Clone the repository into your ROS 2 workspace and build the package:

```bash
cd /opt/ws 
colcon build --packages-select lab7 --symlink-install
source install/setup.bash
```

## 🏃‍♂️ Usage and Launch
Part A: TF2 Verification (Broadcaster and Listener)
To verify dynamic transforms and mathematical calculations, run the following in separate terminals:

### 1. Launch the broadcaster with predefined angles: theta1=0.2, theta2=0.5, theta3=0.35
```bash
ros2 run lab7 tf2_broadcaster_demo -- 0.2 0.5 0.35
```
### 2. Launch the listener
```bash
ros2 run lab7 tf2_listener_demo -- 0.2 0.5 0.35
```
### 3. Verify the result using the TF2 Echo tool
```bash
ros2 run tf2_ros tf2_echo world rtr_ee_demo
```
## Part B: URDF/Xacro Visualization in RViz2
Launch the robot model visualization and the GUI (joint_state_publisher_gui) for manual joint control:

```bash
ros2 launch lab7 rtr_visualize.launch.py
```
## Part C: ROS 2 Control
Launch the mock controller and send a positioning command:

### 1. Launch ROS 2 Control
```bash
ros2 launch lab7 rtr_ros2_control.launch.py
```
### 2. Send a command array in a separate terminal
```bash
ros2 topic pub --once /forward_position_controller/commands std_msgs/msg/Float64MultiArray "{data: [0.2, 0.6, 0.4]}"
```
### 3. Check the end-effector position change
```bash
ros2 run tf2_ros tf2_echo base_link tool0
```
## ✅ Automated Testing
The project includes automated tests to verify the correctness of the kinematics calculations. To run them, execute:
```bash
colcon test --packages-select lab7
colcon test-result --all --verbose
```

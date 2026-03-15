# Lab 2: Introduction to ROS2 and Simulation Environment
### 1. Clone Repository
  ```bash
   cd ~
   git clone https://github.com/vit20087/robotics_lpnu.git
   cd robotics_lpnu/lab2
   ```
### 2. Build Docker Image
  ```bash
   ./scripts/cmd build-docker
   This takes 10-15 minutes on first run.
   ```
### 3. Install and open VScode
  ```bash
   code .
   ```
### 4. Run Container
```bash
   ./scripts/cmd run
   ```
### 4. Build and Test
```bash
# Build your package
colcon build --packages-select lab2

# Source the workspace (makes your package visible)
source install/setup.bash
```
### 5. Launch Everything
  ```bash
   ros2 launch lab2 gazebo_ros2.launch.py
   ```
### 6. Test the Controller (New Terminal)
```bash
   ros2 run lab2 robot_controller
   ```
   Don't forget run the simulation.

### 7. Test the Subscriber (Another New Terminal)
```bash   
ros2 run lab2 lidar_subscriber
```
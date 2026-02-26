# Lab 1: Building Robot in Gazebo

### 1. Clone Repository

```bash
cd ~
git clone https://github.com/vit20087/lab1-padus-robotics.git
cd lab1-padus-robotics
```

### 2. Build Docker Image

```bash
./scripts/cmd build-docker
```

> **Note:** This takes 10-15 minutes on first run.

### 3. Install and open VSCode

```bash
code .
```

### 4. Run Container

```bash
./scripts/cmd run
```

### 5. Run Gazebo

```bash
gz sim /opt/ws/src/code/lab1/worlds/robot.sdf
```

### 6. In another terminal run next code to run our robot

```bash
gz topic -t "/cmd_vel" -m gz.msgs.Twist -p "linear: {x: 0.5}, angular: {z: 0.05}"
```
**Don't forget to run the simulation** (press the Play button in Gazebo GUI).

### 7. In another terminal run this code for gathering data from Lidar

```bash
gz topic -e -t /lidar

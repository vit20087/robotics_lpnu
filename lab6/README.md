# Lab 6: Motion Planning for Mobile Robots (Nav2)

**Objective:** Get familiar with the **Nav2 stack** (map server, localization, planner, controller, costmaps, behavior tree) by running it in simulation and **reading the official Nav2 docs** linked under **Further reading** below (start with the main site, then planner server and controller server when you tune YAML). Send goals in `room_nav2`, and **edit** `nav2_params.yaml` until the robot moves smoothly, the **local costmap** follows obstacles without too much blur or “drift,” and the robot **reaches the goal** in a sensible way. The first settings in the repo are **on purpose a bit bad** (for example **fast** motion and **slow** costmap/controller updates). Your job is to change rates, speed limits, inflation, and goal tolerances until things work better.

## Setup

Rebuild the Docker image the first time (so Nav2 packages are installed):

```bash
./scripts/cmd build-docker
```

Inside the container:

```bash
cd /opt/ws
colcon build --packages-select lab6
source install/setup.bash
```

---

## Launch and test

```bash
ros2 launch lab6 nav2_room_bringup.launch.py
```

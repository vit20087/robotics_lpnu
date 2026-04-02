import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TwistStamped, PoseStamped
from nav_msgs.msg import Path

class DeadReckoningNode(Node):
    def __init__(self):
        super().__init__("dead_reckoning")

        self.declare_parameter("cmd_vel_topic", "/cmd_vel")
        self.declare_parameter("path_dr_topic", "/path_dr")
        self.declare_parameter("frame_id", "odom")
        self.declare_parameter("max_poses", 2000)

        cmd_topic = self.get_parameter("cmd_vel_topic").value
        path_topic = self.get_parameter("path_dr_topic").value
        self.frame_id = self.get_parameter("frame_id").value
        self.max_poses = int(self.get_parameter("max_poses").value)

        self.x, self.y, self.th = 0.0, 0.0, 0.0
        self.last_time = None

        self.create_subscription(TwistStamped, cmd_topic, self.cmd_callback, 10)
        self.pub_path = self.create_publisher(Path, path_topic, 10)

        self.path_msg = Path()
        self.path_msg.header.frame_id = self.frame_id

        self.get_logger().info("✅ Dead Reckoning started and listening for TwistStamped")

    def cmd_callback(self, msg: TwistStamped):
        # Використовуємо час із заголовка повідомлення для точності
        now_msg = rclpy.time.Time.from_msg(msg.header.stamp)

        if self.last_time is None:
            self.last_time = now_msg
            return

        dt = (now_msg - self.last_time).nanoseconds / 1e9
        self.last_time = now_msg

        if dt <= 0: return
        dt = min(dt, 0.2)

        # Звертаємося через msg.twist 
        v = msg.twist.linear.x
        w = msg.twist.angular.z

        # Оновлюємо орієнтацію та позицію
        self.th += w * dt
        self.x += v * math.cos(self.th) * dt
        self.y += v * math.sin(self.th) * dt

        # Публікація Path
        pose = PoseStamped()
        pose.header.stamp = now_msg.to_msg()
        pose.header.frame_id = self.frame_id
        pose.pose.position.x = self.x
        pose.pose.position.y = self.y
        pose.pose.orientation.z = math.sin(self.th / 2.0)
        pose.pose.orientation.w = math.cos(self.th / 2.0)

        self.path_msg.header.stamp = now_msg.to_msg()
        self.path_msg.poses.append(pose)

        if len(self.path_msg.poses) > self.max_poses:
            self.path_msg.poses.pop(0)

        self.pub_path.publish(self.path_msg)

def main(args=None):
    rclpy.init(args=args)
    node = DeadReckoningNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
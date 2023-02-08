import rclpy
from rclpy.node import Node

class MinimalPublisher(Node):
  def __init__(self):
    super().__init__('minimal_publisher')
    self.get_logger().info("Starting minimal_publisher")


  def __del__(self):
    self.get_logger().info("Stopping minimal_publisher")


def main(args=None):
  rclpy.init(args=args)

  minimal_publisher = MinimalPublisher()

  rclpy.spin(minimal_publisher)

  minimal_publisher.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()

import socket
import json

import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist

class CmdBridge(Node):
  def __init__(self):
    super().__init__('cmd_bridge')
    self.get_logger().info("Starting cmd_bridge node...")

    self.declare_parameter('host', 'localhost')
    self.declare_parameter('port', 5000)

    self.open_server()

    self.publisher_ = self.create_publisher(Twist, 'cmd_vel', 10)

    # Thread to listen incoming connections and messages
    self.create_timer(0.1, self.listen)


  def listen(self):
    self.get_logger().info('waiting for a connection')
    connection, client_address = self.sock.accept()

    try:
      self.get_logger().info(f'connection from {client_address}')

      # While the connection is open
      while True:
        data = connection.recv(1024)
        # If there is no data, the connection is closed
        if not data: break
        
        try: data = json.loads(data)
        except ValueError:
          continue

        msg = Twist()
        msg.linear.x = data['linear']['x']
        msg.linear.y = data['linear']['y']
        msg.linear.z = data['linear']['z']
        msg.angular.x = data['angular']['x']
        msg.angular.y = data['angular']['y']
        msg.angular.z = data['angular']['z']

        self.publisher_.publish(msg)

    finally:
      connection.close()


  def open_server(self):
    host = self.get_parameter('host').value
    port = self.get_parameter('port').value

    # Create a TCP/IP socket
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the port
    self.get_logger().info(f'Starting up on {host}:{port}')
    self.sock.bind((host, port))

    # Listen for incoming connections
    self.sock.listen(1)


def main(args=None):
  rclpy.init(args=args)
  minimal_publisher = CmdBridge()
  rclpy.spin(minimal_publisher)
  minimal_publisher.destroy_node()
  rclpy.shutdown()


if __name__ == '__main__':
  main()

#!/usr/bin/env python

import socket
import json

import rospy
from geometry_msgs.msg import Twist


class Bridge:
  def __init__(self):
    self.server_ip = rospy.get_param('~server_ip', 'localhost')
    self.server_port = rospy.get_param('~server_port', 5000)

    # Wait until the server is up
    while not rospy.is_shutdown():
      try:
        self.connect()
        break
      except socket.error:
        rospy.logwarn('Could not connect to the server, retrying...')
        rospy.sleep(1)
    
    if rospy.is_shutdown():
      return
    
    self.subscriber = rospy.Subscriber('cmd_vel', Twist, self.callback)


  def callback(self, data):
    # create a dictionary to send to the server
    data = {
      'linear': {
        'x': data.linear.x,
        'y': data.linear.y,
        'z': data.linear.z,
      },
      'angular': {
        'x': data.angular.x,
        'y': data.angular.y,
        'z': data.angular.z,
      }
    }

    # Transform the dictionary to a string json
    data = json.dumps(data)
    self.send(data)


  def connect(self):
    rospy.loginfo_throttle(1,'Trying to connect to the server at %s:%d', self.server_ip, self.server_port)
    self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    self.client_socket.connect((self.server_ip, self.server_port))

    rospy.loginfo('Connected to the server')


  def send(self, data):
    try:
      self.client_socket.send(data.encode())

    except socket.error:
      self.client_socket.close()
      try:
        self.connect()
        self.client_socket.send(data.encode())

      except socket.error:
        rospy.logwarn_throttle(1, 'Could not connect to the server, message lost')
        pass

  def __del__(self):
    self.client_socket.close()


if __name__ == '__main__':
  rospy.init_node('bridge')
  bridge = Bridge()
  rospy.spin()

#!/usr/bin/env python

# Open a socket to listen messages from port 5000
import socket
import json

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 5000)
print('starting up on {} port {}'.format(*server_address))

sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
  # Wait for a connection
  print('waiting for a connection')
  connection, client_address = sock.accept()
  try:
    print('connection from', client_address)

    # While the connection is open
    while True:
      data = connection.recv(1024)

      # If there is no data, the connection is closed
      if not data:
        break
      
      try:
        # Transform the string json to a dictionary
        data = json.loads(data)
      except ValueError:
        continue

      print('linear:  x: {}, y: {}, z: {}'.format(data['linear']['x'], data['linear']['y'], data['linear']['z']))
      print('angular: x: {}, y: {}, z: {}'.format(data['angular']['x'], data['angular']['y'], data['angular']['z']))

  finally:
      # Clean up the connection
      connection.close()

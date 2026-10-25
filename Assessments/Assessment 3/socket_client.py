"""
Program: socket_client.py
Requires: Python 3.10 or higher (tested on Python 3.14.3)
Description: Demonstrates Python data structures use:
    - Part C:   
    Create a socket object after importing the socket library. 
    Connects to the server to the local host address (127.0.0.1)
    and IPv4 port 1234 and recieves data then closes the connection.
Author: Michael Webb
Student ID: 20172813
Date: 2026-10-25
Version: 1.0
"""
import socket 

server = '127.0.0.1'
port = 1234
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the server
client_socket.connect((server, port))
print(f"Connected to {server}:{port}")

# Recieve data from the server (buffer size 1024)
data = client_socket.recv(1024).decode()
print(f"Received data from the server: {data}")
# Close the connection
client_socket.close()



"""
Program: socket_server.py
Requires: Python 3.10 or higher (tested on Python 3.14.3)
Description: Demonstrates Python data structures use:
    - Part C:   
    Create a socket object after importing the socket library. 
    Uses the bind() method to bind the server to the local host address (127.0.0.1)
    and IPv4 port 1234.
Author: Michael Webb
Student ID: 20172813
Date: 2026-10-25
Version: 1.0
"""
import socket 

def start_server():
    """Initializes the server, binds to localhost:1234, and listens for connections."""
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'
    port = 1234

    # Bind the socket to the address and port
    server_socket.bind((host, port))
    
    # Put the server into listening mode
    server_socket.listen(1)
    print(f"Server is listening on {host}:{port}...")

    while True:
        # Accept the incoming connection
        client_socket, address = server_socket.accept()
        print(f"Connection established with {address}")
        
        # Send a confirmation message to the client
        message = "Connection successful. Welcome to the network management server."
        client_socket.send(message.encode())
        
        # Close the connection
        client_socket.close()
        break  # Exiting after one connection for testing purposes

if __name__ == "__main__":
    start_server()

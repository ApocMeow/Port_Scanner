# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 20:35:41 2016

@author: jhuss

This is a simple program to scan for all open ports, in a user specified range,
on a remote host. It will then return a success or error code for each port.
Finally we print the full list of open ports we have found.
"""

# Import the socket module
import socket                                         

# Host we are targetting for scanning
host = 'localhost'                          

# Start of port range for scanning                                      
start_port = 1

# End of port range for scanning
end_port = 1000

# This list will hold all of the ports we have found to be open
open_list =[]

# First we set up our range for scanning
for port in range(start_port,end_port + 1):
    # Create a socket object
    remote_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set the timeout for the socket
    remote_socket.settimeout(2)
    
    # Variable for the result of our connection test
    connect_result = remote_socket.connect_ex((host, port))
    
    #Logic for printing and storing the result of our connection test
    if connect_result == 0:
        print('Port {} is open!'.format (port))
        open_list.append(port)
        remote_socket.close()
    else:
        print('Port {} is closed! Returned: {}'.format (port, connect_result))
       
print('Port scanning complete on host: {}'.format (host))
print('The following ports are open on {}: {}'.format (host, open_list))
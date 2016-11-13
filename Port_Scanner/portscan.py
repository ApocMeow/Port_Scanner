# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 20:35:41 2016

@author: jhuss

This is a simple program to scan for all open ports, in a user specified range,
on a remote host. It will then return a success or error code for each port.
Finally we print the full list of open ports we have found.
"""

# Import the necessary modules
import socket    
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        master.title("Port Scanner")
        master.geometry('700x500')
        master.wm_iconbitmap('favicon.ico')

    def create_widgets(self):       
               
        # Label for Host/IP entry box
        self.host_label = tk.Label(self)
        self.host_label['text'] = 'Host Name: '
        self.host_label.grid(row=1, column=0, sticky='W')
        
        # Label for start of port range entry box
        self.start_label = tk.Label(self)
        self.start_label['text'] = 'Starting port: '
        self.start_label.grid(row=2, column=0, sticky='W')
        
        # Label for end of port range entry box
        self.end_label = tk.Label(self)
        self.end_label['text'] = 'Ending port: '
        self.end_label.grid(row=3, column=0, sticky='W')        
        
        # Text entry for Target Host/IP
        self.host_name = tk.Entry(self)
        self.host_name["textvariable"] = ''
        self.host_name.grid(row=1, column=1, sticky='W')
        
        # Text entry for start of port range
        self.start_port = tk.Entry(self)
        self.start_port["textvariable"] = ''
        self.start_port.grid(row=2, column=1, sticky='W')
        
        # Text entry for end of port range
        self.end_port = tk.Entry(self)
        self.end_port["textvariable"] = ''
        self.end_port.grid(row=3, column=1, sticky='W')
        
        # Text box for our scanning results
        self.out_text = tk.Text(self)
        self.out_text.grid(row=4, column=0, columnspan=2, sticky='W')
        
        # Button to start scanning procedure
        self.start_scan = tk.Button(self)
        self.start_scan["text"] = "Start Scanning"
        self.start_scan["command"] = self.port_scan
        self.start_scan.grid(row=5, column=0)
        
        # Button to exit application
        self.quit = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit.grid(row=5, column=1)
           
    def port_scan(self):
        # Host we are targetting for scanning
        host = self.host_name.get()                          

        # Start of port range for scanning                                      
        start_port = int(self.start_port.get())

        # End of port range for scanning
        end_port = int(self.end_port.get())

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
               self.out_text.insert(tk.END, str('Port {} is open!\n'.format (port)))
               self.update_idletasks()
               open_list.append(port)
               remote_socket.close()
            else:
               self.out_text.insert(tk.END, str('Port {} is closed! Returned: {}\n'.format (port, connect_result)))
               self.update_idletasks()
       
        self.out_text.insert(tk.END, str('Port scanning complete on host: {}\n'.format (host)))
        self.out_text.insert(tk.END, str('The following ports are open on {}: {}\n'.format (host, open_list)))
        

root = tk.Tk()
app = Application(master=root)
app.mainloop()                                     


# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:26:51 2016

@author: james.hussey
"""
#import the tkinter module
import tkinter

# Create a new window
window = tkinter.Tk()

# Set the window title
window.title ('Port Scanner')

# Set the window size
window.geometry('300x400')

# Set the window icon
window.wm_iconbitmap('favicon.ico')

# Create a label widget for the Application title
title_label = tkinter.Label(window, text='Port Scanner')

# Create a text entry box for the starting point range
start_port_ent = tkinter.Entry(window)

# Create a button widget to start scanning
start_scan_btn = tkinter.Button(window, text='Start Scan')

# Pack (add) widgets to main window
title_label.pack()
start_port_ent.pack()
start_scan_btn.pack()

# Draw the window and start our application
window.mainloop()
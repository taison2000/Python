#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Python GUI using grid method
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time
#import tkinter as tk  # import module tkinter, reference it as tk
from tkinter import *

##-----------------------------------------------------------------------------
# Events
#  * <Button-1> - 
#  * <Button-2> - 
#  * <Button-3> - 
#  * <Button-4> - 
#  * <Button-5> - 
#  * <ButtonRelease> - 
#  * <Configure> - 
#  * <Deactivate>
#  * <Destroy> -
#  * <Enter> - 
#  * <Expose> -
#  * <FocusIn> -
#  * <FocusOut> -
#  * <KeyPress> -
#  * <KeyRelease> -
#  * <Leave> 
#  * <Map>
#  * <Motion>
#  * <MouseWheel>
#  * <Unmap>
#  * <Visibility>


# NOTE:
# - Use "unbind" to remove?


##-----------------------------------------------------------------------------
root = Tk()

screen_width = root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
root.geometry("550x250+%d+%d" % (screen_width/2-275, screen_height/2-125))
#root.geometry('500x300')
#root.geometry('500x300+0+0')  # Top Left
#root.geometry('500x300+0-0')  # Buttom Left
#root.geometry('500x300-0+0')  # Top Right
#root.geometry('500x300-0-0')  # Buttom Right

root.configure( background='gold' )
#root.lift()

root.title('tkinter App')

## ----- Functions -----
def ButtonClick_01(event):
  print ("Button 1 is clicked (Left)")
def ButtonClick_02(event):
  print ("Button 2 is clicked (Middle)")
def ButtonClick_03(event):
  print ("Button 3 is clicked (Right)")
def ButtonClick_04(event):
  print ("Button 4 is clicked (Wheel Roll Up)")
def ButtonClick_05(event):
  print ("Button 5 is clicked (Wheel Roll Down)")
def ButtonClick_06(event):
  print ("Button 6 is clicked (  )")

def Event_FocusIn(event):
  print ("Button In Focus")
  
btnClickMe = Button(root, text="Click Me")
btnClickMe.bind("<Button-1>", ButtonClick_01) # Left button
btnClickMe.bind("<Button-2>", ButtonClick_02) # Middle Click Wheel
btnClickMe.bind("<Button-3>", ButtonClick_03) # Rigth button
btnClickMe.bind("<Button-4>", ButtonClick_04) # Wheel Roll Up
btnClickMe.bind("<Button-5>", ButtonClick_05) # Wheel Roll Down
#btnClickMe.bind("<Button-6>", ButtonClick_06) # No such yet?
btnClickMe.bind("<FocusIn>", Event_FocusIn)   # FocusIn
btnClickMe.grid()

root.mainloop()

##-----------------------------------------------------------------------------
"""
Source:
 tkinter 8.5 Reference: a GUI for Python

"""

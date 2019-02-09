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

global Show
Show=True

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
root.lift()

root.title('tkinter App')

## ----- Function run alongside with mainloop -----
def runFunc():
  global Show
  
  if Show==True:
    root.lift()
    Show=False
    #root.configure( background='gold' )
    root.configure( background='#00ff00' )
  else:
    root.lower()
    Show=True
    root.configure( background='lightblue' )
    
  root.after(2000, runFunc)  # <- call the function again

  return


root.after(2000, runFunc)

root.mainloop()

##-----------------------------------------------------------------------------
"""
Source:
http://stackoverflow.com/questions/8683217/when-do-i-need-to-call-mainloop-in-a-tkinter-application
"""

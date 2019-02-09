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

class Application(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.master.title("Grid Multi Frames")
    
    for r in range(6):
      self.master.rowconfigure(r, weight=1)
    for c in range(5):
      self.master.columnconfigure(c, weight=1)
      Button(master, text="Button {0}".format(c)).grid(row=6, column=c, sticky=E+W)
      
    Frame1 = Frame(master, bg='red')
    Frame1.grid(row=0, column=0, rowspan=3, columnspan=2, sticky=W+E+N+S)
    Frame2 = Frame(master, bg='blue')
    Frame2.grid(row=3, column=0, rowspan=3, columnspan=2, sticky=W+E+N+S)
    Frame3 = Frame(master, bg='green')
    Frame3.grid(row=0, column=2, rowspan=6, columnspan=3, sticky=W+E+N+S)

##-----------------------------------------------------------------------------
root = Tk()
#root.geometry('500x300-0+30')
#root.geometry('500x300+0+0')  # Top Left
#root.geometry('500x300+0-0')  # Buttom Left
#root.geometry('500x300-0+0')  # Top Right
root.geometry('500x300-0-0')  # Buttom Right

app = Application(master=root)
app.master.title('tkinter grid Temp')
app.mainloop()

##-----------------------------------------------------------------------------
"""
Source:
http://stackoverflow.com/questions/8683217/when-do-i-need-to-call-mainloop-in-a-tkinter-application
"""

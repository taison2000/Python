#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Scrollbar
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time
#import tkinter as tk  # import module tkinter, reference it as tk
from tkinter import *

class DpWin(object):
  def run(self):
    root = Tk()
    root.geometry('768x612')
    title="Scrollbar"
    root.title(title)
    #self.master.title("Scrollbar")
    
    f = Frame(root)
    f.pack()
    
    # Horizontal  
    xScrollBar = Scrollbar(f, orient=HORIZONTAL)
    xScrollBar.grid(row=1, column=0, sticky=N+W+E+S)
    # Vertical
    yScrollBar = Scrollbar(f)
    yScrollBar.grid(row=0, column=1, sticky=N+W+E+S)
    
    # Text
    text = Text(f, wrap=NONE,
                xscrollcommand=xScrollBar.set,
                yscrollcommand=yScrollBar.set)
    text.grid(row=0, column=0)
    
    xScrollBar.config(command=text.xview)
    yScrollBar.config(command=text.yview)
    
    text.insert(END, 'A'*999)
    
    mainloop()
    
  def start(self):
    self.b_start.config(state=DISABLED)
    self.b_stop.config(state=ACTIVE)
    
  def stop(self):
    self.b_stop.config(state=DISABLED)
    self.b_start.config(state=ACTIVE)
    
if __name__=='__main__':
  win = DpWin()
  win.run()

##-----------------------------------------------------------------------------
"""
Source:
  http://stackoverflow.com/questions/12388604/the-horizontal-scrollbar-didnt-work-in-tkinter

"""


##-----------------------------------------------------------------------------
## tkinter Widgets:
"""
  - Button
  - Canvas
  - Checkbutton
  - Entry
  - Frame
  - Label
  - LabelFrame
  - Listbox
  - Menubutton
  - Menu
  - Message
  - messagebox (v2.x -> tkMessageBox)
  - PaneWindow
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
#------------------------------------------------------------------------------
"""

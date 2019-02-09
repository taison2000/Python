#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Python GUI using grid method
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time

##-----------------------------------------------------------------------------
"""
import tkinter as tk  # import module tkinter, reference it as tk
class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.CreateWidgets()
  
  def CreateWidgets (self):
    # ----- Button -----
    #self.quitButton = tk.Button(self, text='Quit', command=self.quit)
    self.quitButton = tk.Button(self, text='Quit', command=self.destroy)
    self.quitButton.grid(row=0, column=1)
    
    # ----- Menubutton -----
    self.BtnMenu = tk.Menubutton(self, text='Menu Button', bg="gray", relief='raised')
    self.BtnMenu.grid()
    
app = Application()
app.master.title('tkinter grid Temp')
app.mainloop()

"""

from tkinter import *

##-----------------------------------------------------------------------------
class GuiApp(Frame):
  def __init__(self, master=None):
    Frame.__init__( self, master )
    #self.grid()
    self.pack()
    self.CreateWidgets()

  def CreateWidgets( self ):
    #self.m1 = PanedWindow(relief=RAISED)
    self.m1 = PanedWindow(relief=GROOVE)
    self.m1.pack(fill=BOTH, expand=1)

    self.leftLabel = Label(self.m1, text="left pane")
    self.m1.add(self.leftLabel)

    self.m2 = PanedWindow(self.m1, orient=VERTICAL, relief=SUNKEN)
    self.m1.add(self.m2)

    self.topLabel = Label(self.m2, text="top pane")
    self.m2.add(self.topLabel)

    self.bottomLabel = Label(self.m2, text="bottom pane")
    self.m2.add(self.bottomLabel)
  
app = GuiApp()
app.master.title('PanedWindow Demo')
app.mainloop() 

"""
m1 = PanedWindow(relief=RAISED)
m1.pack(fill=BOTH, expand=1)

leftLabel = Label(m1, text="left pane")
m1.add(leftLabel)

m2 = PanedWindow(m1, orient=VERTICAL, relief=SUNKEN)
m1.add(m2)

topLabel = Label(m2, text="top pane")
m2.add(topLabel)

bottomLabel = Label(m2, text="bottom pane")
m2.add(bottomLabel)

mainloop()
"""

"""
def main():
# This is the main function
#          range(start, stop[, step])
  for i in range(0, 1000, 20):
    print("Current Num : %d" % i)
    time.sleep(1)
      
if __name__ == "__main__":
	main()
  #msg = main()
  #print(msg)
  #mainloop()
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

##-----------------------------------------------------------------------------
"""
Resource:
 - http://effbot.org/tkinterbook/panedwindow.htm
 
 - http://www.tkdocs.com/tutorial/windows.html#dialogs

"""


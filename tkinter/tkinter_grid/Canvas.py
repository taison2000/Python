#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Canvas
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time
import tkinter as tk  # import module tkinter, reference it as tk

##-----------------------------------------------------------------------------
class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.CreateWidgets()
  
  def CreateWidgets (self):
    # ----- Canvas -----
    canvas = tk.Canvas( self, width=200, height=100 )
    canvas.grid( row=0, column=0 )
    
    # ----- Line -----
    self.blackline = canvas.create_line( 0, 0, 200, 50) # (x_pos, y_pos, x_length, y_length)
    self.redline = canvas.create_line( 0, 100, 200, 50, fill='red' )
    
    # Delete canvas
    canvas.delete( self.redline )
    canvas.delete( "all" )
    self.redline = canvas.create_line( 0, 100, 200, 50, fill='red' )
    
app = Application()
app.master.title('Canvas')
app.mainloop()

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
"""
Resource:
 - https://www.youtube.com/watch?v=O12aT42okYE

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
  - OptionMenu
  - PaneWindow
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
#------------------------------------------------------------------------------
"""



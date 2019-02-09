#!/usr/bin/python
# Comment start with #
## double "pound" sign has different color

## Example location:
# http://stackoverflow.com/questions/21958534/setting-the-window-to-a-fixed-size-with-tkinter

from tkinter import *

class App:
  def __init__(self, master):
    self.var = IntVar()
    frame = Frame(master)
    frame.grid()
    f2 = Frame(master, width=600, height=100)
    f2.grid(row=0, column=1)
    button = Checkbutton(frame, text='show', variable=self.var, command=self.fx)
    button.grid(row=0, column=0)
    msg2="""I feel bound to give them full satisfaction on this point"""
    self.v = Message(f2, text=msg2)
    
  def fx(self):
    if self.var.get():
      self.v.grid(column=1, row=0, sticky=N)
    else:
      self.v.grid_remove()



top = Tk()
top.title('Frame widget')

app = App(top)

top.mainloop()



# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html
#

# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
#
#

##-----------------------------------------------------------------------------
# Notes:
#  1. A frame is basically just a container for other widgets.
#
#!/usr/bin/python
# Comment start with #




import time
from tkinter import *
import tkinter.messagebox as msgBox



##-----------------------------------------------------------------------------

import tkinter as tk

class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.createWidgets()
    
  def createWidgets(self):
    self.hi_there = tk.Button(self)
    self.hi_there["text"] = "Hello World\n(click me)"
    self.hi_there["command"] = self.say_hi
    self.hi_there.grid()
    
    self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
    self.QUIT['width'] = 40
    self.QUIT['height'] = 5
    #self.QUIT['relief'] = "sunken"  # <-- Work
    #self.QUIT['relief'] = tk.SUNKEN  # <-- Work tkinter.(SUNKEN/FLAT/RAISED/GROOVE/RIDGE)
    #self.QUIT['relief'] = tk.RAISED
    self.QUIT['relief'] = tk.RIDGE
    
    self.QUIT.grid(row=0, column=1)
    
  def say_hi(self):
    print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)

app.mainloop()



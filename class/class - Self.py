#!/usr/bin/python
# Comment start with #




import time
from tkinter import *
import tkinter.messagebox as msgBox



##-----------------------------------------------------------------------------
## self - Not really tie to python. You can use anthing.
## It refer to the class object itself.
##-----------------------------------------------------------------------------

import tkinter as tk

class Application(tk.Frame):
  def __init__( MySelf, master=None ):  ## Use "MySelf", don't have to be "self"
    tk.Frame.__init__( MySelf, master )
    MySelf.grid()
    MySelf.createWidgets()
    
  def createWidgets( MySelf ):
    MySelf.hi_there = tk.Button( MySelf )
    MySelf.hi_there["text"] = "Hello World\n(click me)"
    MySelf.hi_there["command"] = MySelf.say_hi
    MySelf.hi_there.grid()
    
    MySelf.QUIT = tk.Button( MySelf, text="QUIT", fg="red", command=root.destroy )
    MySelf.QUIT['width'] = 40
    MySelf.QUIT['height'] = 5
    #MySelf.QUIT['relief'] = "sunken"  # <-- Work
    #MySelf.QUIT['relief'] = tk.SUNKEN  # <-- Work tkinter.(SUNKEN/FLAT/RAISED/GROOVE/RIDGE)
    #MySelf.QUIT['relief'] = tk.RAISED
    MySelf.QUIT['relief'] = tk.RIDGE
    
    MySelf.QUIT.grid(row=0, column=1)
    
  def say_hi( MySelf ):
    print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)

app.mainloop()



## ----------------------------------------------------------------------------
## Resource:
"""
 - http://stackoverflow.com/questions/2709821/what-is-the-purpose-of-self-in-python
 - http://stackoverflow.com/questions/7554738/python-self-no-self-and-cls?rq=1
 
"""


##-----------------------------------------------------------------------------
## Terminology
##-----------------------------------------------------------------------------
"""
 - Attributes : These are the values an object has.
 - Methods : These are the functions attached to the object.
 - Instance : Whenever make a new object, it's called an "instance"
 - Class : The blueprint for an object.
 - Subclass : Base a new class off an existing class.
 
"""



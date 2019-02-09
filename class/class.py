#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/Python34

# Comment start with #


import time
from tkinter import *
import tkinter.messagebox as msgBox
import tkinter as tk


##-----------------------------------------------------------------------------
class Pair:
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def __repr__(self):
		return 'Pair({0.x!r}, {0.y!r})'.format(self)
	def __str__(self):
		return '({0.x!s}, {0.y!s})'.format(self)
    def display(self):
        print(x)
        print(y)
        
# p = Pair(3, 4) => Pair(3, 4)
# print( P ) => (3, 4)

def get_class_name_of_instance():
# https://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance?rq=1
    pv = Pair(23, "hello world")
    print(type(pv).__name__)    #-> "Pair"
    print(pv.__class__.__name__)
    
def another_way_to_implement_class_name():
    class A(object):
        def class_name(self):
            return type(self).__name__
            
    a = A()
    className = a.class_name()
    print(className)
    
##-----------------------------------------------------------------------------
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
    
    self.QUIT = tk.Button(self, text="QUIT", fg="GREEN", command=root.destroy)
    self.QUIT['width'] = 40
    self.QUIT['height'] = 5
    #self.QUIT['relief'] = "sunken"  # <-- Work
    self.QUIT['relief'] = tk.SUNKEN  # <-- Work tkinter.(SUNKEN/FLAT/RAISED/GROOVE/RIDGE)
    #self.QUIT['relief'] = tk.RAISED
    #self.QUIT['relief'] = tk.RIDGE
    #self.QUIT['relief'] = tk.GROOVE
    
    self.QUIT.grid(row=0, column=1)
    
  def say_hi(self):
    print("hi there, everyone!")


root = tk.Tk()
app = Application(master=root)

app.mainloop()


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



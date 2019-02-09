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

"""
def btnClick():
    app.Frame1.grid()
    app.Frame2.grid_remove()
    app.Frame3.grid_remove()

class Application(Frame):
 
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.master.title("Grid Multi Frames")
    
    for r in range(6):
      self.master.rowconfigure(r, weight=1)

    for c in range(5):
      self.master.columnconfigure(c, weight=1)
      Button(master, text="Button {0}".format(c), command=).grid(row=6, column=c, sticky=E+W)

    self.master.columnconfigure(1, weight=1)
    btn1 = Button(master, text="Button1", command=btnClick).grid(row=6, column=1, sticky=E+W)
    self.master.columnconfigure(2, weight=1)
    btn2 = Button(master, text="Button1", command=btnClick).grid(row=6, column=2, sticky=E+W)
    self.master.columnconfigure(3, weight=1)
    btn3 = Button(master, text="Button1", command=btnClick).grid(row=6, column=3, sticky=E+W)    
    
    Frame1 = Frame(master, bg='red')
    Frame1.grid(row=0, column=0, rowspan=6, columnspan=6, sticky=W+E+N+S)
    Frame2 = Frame(master, bg='blue')
    Frame2.grid(row=0, column=0, rowspan=6, columnspan=6, sticky=W+E+N+S)
    Frame3 = Frame(master, bg='green')
    Frame3.grid(row=0, column=0, rowspan=6, columnspan=6, sticky=W+E+N+S)


root = Tk()
#root.geometry('500x300-0+30')
#root.geometry('500x300+0+0')  # Top Left
#root.geometry('500x300+0-0')  # Buttom Left
#root.geometry('500x300-0+0')  # Top Right
root.geometry('500x300-0-0')  # Buttom Right

app = Application(master=root)
app.master.title('tkinter grid Temp')
app.mainloop()
"""

##-----------------------------------------------------------------------------

top = Tk()

top.geometry('500x300-500-200') # Start from right buttom, move left 500, up 200
#top.geometry('500x300+0+0') # Start from 'Left' 'Top'
#top.geometry('500x300+0-0') # Start from 'Left' 'Bottom'
#top.geometry('500x300-0+0') # Start from 'Right' 'Top'
#top.geometry('500x300-0-0') # Start from 'Right' 'Bottom'

top.title("Multiple Frame")

for r in range(6):
  top.rowconfigure(r, weight=1)

def btn1click():
  Frame1.grid()
  Frame2.grid_remove()
  Frame3.grid_remove()
  top.rowconfigure(6, weight=1)
def btn2click():
  Frame1.grid_remove()
  Frame2.grid()
  Frame3.grid_remove()
  top.rowconfigure(6, weight=0)
def btn3click():
  Frame1.grid_remove()
  Frame2.grid_remove()
  Frame3.grid()
  top.rowconfigure(6, weight=0)

## top.rowconfigure(6, weight=1) # Try this to see

## Try different weight on columns
top.columnconfigure(1, weight=3)
top.columnconfigure(2, weight=2)
top.columnconfigure(3, weight=1)
"""
top.columnconfigure(1, weight=1)
top.columnconfigure(2, weight=1)
top.columnconfigure(3, weight=1)
"""

btn1 = Button(top, text="Red", command=btn1click).grid(row=6, column=1, sticky=E+W)
btn2 = Button(top, text="Green", command=btn2click).grid(row=6, column=2, sticky=E+W)
btn3 = Button(top, text="Blue", command=btn3click).grid(row=6, column=3, sticky=E+W)

## The buttons can expand vertically:
'''
top.rowconfigure(6, weight=1)
btn1 = Button(top, text="Red", command=btn1click).grid(row=6, column=1, sticky=E+W+N+S)
btn2 = Button(top, text="Green", command=btn2click).grid(row=6, column=2, sticky=E+W+N+S)
btn3 = Button(top, text="Blue", command=btn3click).grid(row=6, column=3, sticky=E+W+N+S)
'''

Frame1 = Frame(top, bg='red')
Frame1.grid(row=0, column=0, rowspan=6, columnspan=6, sticky=W+E+N+S)
Frame2 = Frame(top, bg='green')
Frame2.grid(row=0, column=0, rowspan=6, columnspan=6, sticky=W+E+N+S)
Frame3 = Frame(top, bg='blue')
Frame3.grid(row=0, column=0, rowspan=6, columnspan=6, sticky=W+E+N+S)

"""
Source:
http://stackoverflow.com/questions/8683217/when-do-i-need-to-call-mainloop-in-a-tkinter-application

"""

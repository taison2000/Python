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

##-----------------------------------------------------------------------------
class BuckyButton:
  def __init__(self, master):
    frameMain = Frame(master)
    frameMain.grid()
    
    #self.PrintButton = Button(frameMain, text="Print Message", command=PrintMessage) #-> Not working, missing "self"
    self.PrintButton = Button(frameMain, text="Print Message", command=self.PrintMessage)
    self.PrintButton.grid(row=0, column=0)

    self.QuitButton = Button(frameMain, text="Quit", command=frameMain.quit)
    self.QuitButton.grid(row=0, column=1)
    
    
  def PrintMessage(self):
    print( "Wow! This actually worked!" )
  
  
  
  
  
##-----------------------------------------------------------------------------
root = Tk()
#root.geometry('500x300')
# ------ root.geometry('500x300+0+0')  # Top Left
#root.geometry('500x300+0-0')  # Buttom Left
#root.geometry('500x300-0+0')  # Top Right
#root.geometry('500x300-0-0')  # Buttom Right


root.title('tkinter Class')

## ----- Create the class object -----
App = BuckyButton(root)

root.mainloop()

##-----------------------------------------------------------------------------
"""
Source:
 - https://www.youtube.com/watch?v=IYHJRnVOFlw

"""

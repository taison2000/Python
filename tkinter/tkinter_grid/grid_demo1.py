#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Python GUI using grid method
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  Demonstration of tkinter and the grid placement method.
"""

## --- grid placement options ---
#   -column -columnspan -in -ipadx -ipady -padx -pady -row -rowspan -sticky


import os
import time
from tkinter import *
#import tkinter as tk  # import module tkinter, reference it as tk


class demoGUI(Frame):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    #self.grid()
    self.grid(sticky=W)
    self.CreateWidgets()
  
  def CreateWidgets (self):
    # get top-level frame reference
    top=self.winfo_toplevel()
    
    # set the start location in the window manager
    top.wm_geometry('+50+100')
    
    # Set window title
    self.master.title("Grid GUI demo")
    
    # configure the global grid behavior
    self.master.rowconfigure(0, weight=1)
    self.master.columnconfigure(0, weight=1)
    self.grid(sticky = W+E+N+S)
    
    # create string objects for use with label widgets
    self.var1 = StringVar()
    self.var1.set("")
    self.var2 = StringVar()
    self.var2.set("")
    
    # output state toggle flags
    self.toggle1 = 0
    self.toggle2 = 0
    
    # create three buttons and three label widgets, one of which is
    # a dummy placeholder (for now)
    
    # bind button 1 and 2 to event handlers
    
    # the two active label widgets will display green text on abs
    # black background
    
    self.button1 = Button (self, text="Button 1", width = 10)
    self.button1.grid (row=0, column=0)
    self.button1.bind("<Button-1>", self.button1_Click)
    
    self.text1 = Label(self, text="", width=10, relief=SUNKEN, bg="black", fg="green", textvariable=self.var1)
    self.text1.grid(row=0, column=10)
    
    self.button2 = Button(self, text="Button 2", width=10)
    self.button2.grid(row=1, column=0)
    self.button2.bind("<Button-1>", self.button2_Click)
    self.button2.bind("<Button-2>", self.button2_MiddleClick)
    self.button2.bind("<Button-3>", self.button2_RightClick)
    
    self.text2 = Label(self, text="", width=10, relief=SUNKEN, bg="black", fg="green", textvariable=self.var2)
    self.text2.grid(row=1, column=10)
    
    self.button3 = Button(self, text="Quit", width=10, command=self.quit)
    self.button3.grid(row=2, column=0)
    
    # dummy space filler
    # you could modify this to display something
    self.text3 = Label(self, text="", width=10)
    self.text3.grid(row=2, column=10)
    
  def button1_Click(self, event):
    if self.toggle1 == 0:
      self.var1.set("0000")
      self.toggle1=1
    else:
      self.var1.set("1111")
      self.toggle1=0
        
    print ("Button 1")
    
  def button2_Click(self, event):
    if self.toggle2 == 0:
      self.var2.set("00_LeftClick")
      self.toggle2=1
    else:
      self.var2.set("11_LeftClick")
      self.toggle2=0
        
    print ("Button 2 Left Click")
    
  def button2_MiddleClick(self, event):
    if self.toggle2 == 0:
      self.var2.set("00_MiddleClick")
      self.toggle2=1
    else:
      self.var2.set("11_MiddleClick")
      self.toggle2=0
        
    print ("Button 2 Middle Click")
  
  def button2_RightClick(self, event):
    if self.toggle2 == 0:
      self.var2.set("00_RightClick")
      self.toggle2=1
    else:
      self.var2.set("11_RightClick")
      self.toggle2=0
        
    print ("Button 2 Right Click")
      
 
  """
    # ----- Button -----
    self.quitButton = tk.Button(self, text='Quit', command=self.quit)
    self.quitButton.grid()
    
    # ----- Menubutton -----
    self.BtnMenu = tk.Menubutton(self, text='Menu Button', bg="gray", relief='raised')
    self.BtnMenu.grid()
  """
    
app = demoGUI()
#app.master.title('Sample application')
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

"""
column

"""

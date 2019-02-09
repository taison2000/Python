#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Python GUI using grid method
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time
import tkinter as tk  # import module tkinter, reference it as tk

##-----------------------------------------------------------------------------
class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    #self.geometry("500x300")
    self.grid()
    self.CreateWidgets()
    
  
  def CreateWidgets (self):
    btnWidth=15
    btnHeight=5
    # ----- Button -----
    #self.B1 = tk.Button(self, text='FLAT', relief="FLAT")
    """
    self.B1 = tk.Button(self, text='FLAT', width=10, height=2, relief='flat')
    self.B1.grid(row=0, column=1)
    self.B2 = tk.Button(self, text='RAISED', width=10, height=2, relief='raised')
    self.B2.grid(row=1, column=1)
    self.B3 = tk.Button(self, text='SUNKEN', width=10, height=2, relief='sunken')
    self.B3.grid(row=2, column=1)
    self.B4 = tk.Button(self, text='GROOVE', width=10, height=2, relief="groove")
    self.B4.grid(row=3, column=1)
    self.B5 = tk.Button(self, text='RIDGE', width=10, height=2, relief="ridge")
    self.B5.grid(row=4, column=1)
    """
    
    #B1 = tk.Button(self, text='FLAT',   width=btnWidth, height=btnHeight, relief=FLAT)
    B1 = tk.Button(self, text='FLAT',   width=btnWidth, height=btnHeight, relief='flat')
    B1.grid(row=0, column=1)
    B2 = tk.Button(self, text='RAISED', width=btnWidth, height=btnHeight, relief='raised')
    B2.grid(row=1, column=1)
    B3 = tk.Button(self, text='SUNKEN', width=btnWidth, height=btnHeight, relief='sunken')
    B3.grid(row=2, column=1)
    B4 = tk.Button(self, text='GROOVE', width=btnWidth, height=btnHeight, relief="groove")
    B4.grid(row=3, column=1)
    B5 = tk.Button(self, text='RIDGE',  width=btnWidth, height=btnHeight, relief="ridge")
    B5.grid(row=4, column=1)
    B6 = tk.Button(self, text='SOLID',  width=btnWidth, height=btnHeight, relief="solid")
    B6.grid(row=5, column=1)

    # ----- Menubutton -----
    """
    self.BtnMenu = tk.Menubutton(self, text='Menu Button', bg="gray", relief='raised')
    self.BtnMenu.grid()
    """
    
app = Application()
app.master.title('tkinter grid Temp')
app.master.geometry("200x550")
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

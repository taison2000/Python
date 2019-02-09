#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  widget.columnconfigure( column#, option=value, ... )
  -----------------------------------------------------------------------------
    option == minsize; pad; weight

"""

import os
import time
import tkinter as tk  # import module tkinter, reference it as tk

##-----------------------------------------------------------------------------
class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.columnconfigure(0, weight=1)
    self.grid()
    self.CreateWidgets()
  
  def CreateWidgets (self):
    # ----- Button -----
    self.quitButton = tk.Button(self, text='Quit', command=self.destroy)
    self.quitButton.grid(row=0, column=1)
    self.quitButton.columnconfigure(1, weight=1)  # w.columnconfigure( 1, weight=1 ) => column=1
    
    # ----- Menubutton -----
    self.BtnMenu = tk.Menubutton(self, text='Menu Button', bg="gray", relief='raised')
    self.BtnMenu.columnconfigure(0, weight=1)
    self.BtnMenu.grid()
    
app = Application()
app.master.title('columnconfigure')
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

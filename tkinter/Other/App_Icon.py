#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  Application Icon
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
    # ----- Button -----
    #self.quitButton = tk.Button(self, text='Quit', command=self.quit)
    self.quitButton = tk.Button(self, text='Quit', command=self.destroy)
    self.quitButton.grid(row=0, column=1)
    
    # ----- Menubutton -----
    self.BtnMenu = tk.Menubutton(self, text='Menu Button', bg="gray", relief='raised')
    self.BtnMenu.grid()

'''
app = Application(root)
app.master.title('Application Icon')
app.mainloop()
'''
root = tk.Tk()
root.title("Application Icon")


#iconImg = tk.PhotoImage( file='Coffee.gif' )
#iconImg = tk.PhotoImage( file='tomcat.gif' )
#iconImg = tk.PhotoImage( file='kenyan-flag-large.gif' )
iconImg = tk.PhotoImage( file='homer.gif' )

## --- App Icon ---
root.tk.call('wm', 'iconphoto', root._w, iconImg )

root.mainloop()

##-----------------------------------------------------------------------------
"""
Resource:
 - http://stackoverflow.com/questions/11176638/python-setting-application-icon
 - 
"""

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


##-----------------------------------------------------------------------------
"""
Resource:
 - http://www.tkdocs.com/tutorial/windows.html#dialogs

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
  - PaneWindow
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
#------------------------------------------------------------------------------
"""




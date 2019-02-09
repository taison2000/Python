#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
    Python GUI using grid method
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time
import tkinter as tk  # import module tkinter, reference it as tk

##-----------------------------------------------------------------------------
class Application( tk.Frame ):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.CreateWidgets()
  
  def CreateWidgets (self):
    # ----- Button -----
    #self.quitButton = tk.Button(self, text='Quit', command=self.quit)
    self.quitButton = tk.Button(self, text='Quit', command=self.destroy)
    self.quitButton.grid(row=0, column=0)
    
    # ----- Menubutton -----
    self.BtnMenu = tk.Menubutton(self, text='Menu Button', bg="gray", relief='raised')
    self.BtnMenu.grid()
    
    # ----- OptionMenu -----
    optionList = ( 'train', 'plane', 'boat' )
    self.val = tk.StringVar()
    self.val.set( optionList[0] )
    self.opmu = tk.OptionMenu( self, self.val, *optionList )
    self.opmu.grid()
    
app = Application()
app.master.title('tkinter grid Temp')
app.mainloop()

##-----------------------------------------------------------------------------
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
  - OptionMenu
  - PaneWindow
  - Radiobutton
  - Scale
  - Scrollbar
  - Spinbox
  - Text
  - Toplevel
#------------------------------------------------------------------------------
"""

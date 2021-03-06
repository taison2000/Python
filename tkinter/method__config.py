#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
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
    
    # ----- Label -----
    self.lblName = tk.Label(self, text="Default Label Name")
    self.lblName.grid()
    
    # ----- Button and Entry -----
    #self.entryText = tk.Entry(self, )
    self.btnChangeText = tk.Button(self, text="Update label", command=self.ConfigLabelText)
    self.btnChangeText.grid()
    
  def ConfigLabelText( self ):
    ## config == configure ??
    self.lblName.config( text="New text" )
    self.lblName.configure( text="Configure" )  # should be same as above
  
app = Application()
app.master.title('tkinter grid Temp')
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

##-----------------------------------------------------------------------------
"""
Resource:
 - http://www.tkdocs.com/tutorial/windows.html#dialogs

"""

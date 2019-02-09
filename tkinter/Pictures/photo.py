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
from tkinter import *

##-----------------------------------------------------------------------------
class Application( Frame ):
  def __init__(self, master=None):
    Frame.__init__(self, master)
    self.grid()
    self.CreateWidgets()
    
  
  def CreateWidgets( self ):
    # ----- PhotoImage -----
    #photo = PhotoImage( file=r"Frame.png" )
    #photo = PhotoImage( file=r"Green_LED.png" )
    #photo = hotoImage( file=r'.\ttkFrame.PNG' )
    photo = PhotoImage( file=r"Frame.png" )
    
    # ----- Label -----
    #self.PhotoLabel = Label(self, image=photo, width=500, height=530, relief='raised' )
    self.PhotoLabel = Label(self, image=photo, bg="gray", relief='raised')
    #self.PhotoLabel = Label(self, text="Label", bg="gray", relief='raised')
    self.PhotoLabel.image = photo # need to keep a PhotoImage reference
    #self.PhotoLabel.config( image=photo )
    self.PhotoLabel.grid()



def main():
# This is the main function
  
  app = Application()
  app.master.title('PhotoImage')
  app.mainloop()
  return;
  
if __name__ == "__main__":
  main()
  
"""

##-----------------------------------------------------------------------------
root = Tk()
frame = Frame( root )
frame.grid()
#photo = PhotoImage( file=r"Green_LED.png")
photo = PhotoImage( file=r".\ttkFrame.PNG" )
#photo = PhotoImage( file=r".\Frame.png")

# ----- Label -----
PhotoLabel = Label(frame, image=photo, width=500, height=500, relief='raised' )
#PhotoLabel = Label(frame, text="photo", width=10, height=30, relief='raised' )
#PhotoLabel = Label(frame, image=photo, bg="gray", relief='raised')
#PhotoLabel = Label(frame, text="Label", bg="gray", relief='raised')
#PhotoLabel.image = photo # need to keep a PhotoImage reference
PhotoLabel.config( image=photo )
PhotoLabel.grid()

root.mainloop()
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
 - http://tkinter.unpythonic.net/wiki/
"""

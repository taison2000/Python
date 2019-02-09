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
''' File Dialog Module '''
from tkinter import filedialog


##-----------------------------------------------------------------------------
class Application(tk.Frame):
  def __init__(self, master=None):
    tk.Frame.__init__(self, master)
    self.grid()
    self.CreateWidgets()
  
  def FileOpen(self):
    # ----- File Open -----
    self.fileopen = filedialog.askopenfilename()
  
  def FileSaveAs(self):
    # ----- File Save As -----
    self.fileSaveAs = filedialog.asksaveasfilename()
    return;
  
  def Directory(self):
    # ----- directory -----
    self.dirName = filedialog.askdirectory()
  
  def CreateWidgets (self):
    # ----- Open File Button -----
    self.OpenFileButton = tk.Button(self, text='Open...', command=self.FileOpen)
    self.OpenFileButton.grid(row=0, column=1)
    self.OpenFileButton.rowconfigure(0, weight=1)
    self.OpenFileButton.columnconfigure(1, weight=1)
    
    # ----- File Save As Button -----
    self.FileSaveAsButton = tk.Button(self, text='Save As...', command=self.FileSaveAs)
    self.FileSaveAsButton.grid(row=0, column=2)
    
    # ----- Directory Button -----
    self.DirectoryButton = tk.Button(self, text='Directory', command=self.Directory)
    self.DirectoryButton.grid(row=0, column=3)
    
    
    
app = Application()
app.master.title('File Dialog')
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

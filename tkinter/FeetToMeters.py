#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  widget.columnconfigure( column#, option=value, ... )
  -----------------------------------------------------------------------------
    option == minsize; pad; weight

"""

import os
import time
#import tkinter as tk  # import module tkinter, reference it as tk
from tkinter import *
from tkinter import ttk

##-----------------------------------------------------------------------------
root = Tk()
root.title("Feet To Meters")

mainframe = ttk.Frame( root, padding=(3, 3, 12, 12) )
mainframe.grid( column=0, row=0, sticky=(N, W, E,S) )

root.columnconfigure( 0, weight=1 )
root.rowconfigure( 0, weight=1 )

# Step 4
feet = StringVar()
feet_entry = ttk.Entry( mainframe, width=7, textvariable=feet )
feet_entry.grid( column=1, row=0, sticky=(W, E) )

# Step 5
meters = StringVar()
ttk.Label( mainframe, textvariable=meters ).grid( column=1, row=1, sticky=(W, E) )

# Step 6
ttk.Label( mainframe, text='feet' ).grid( column=2, row=0, sticky=W )
ttk.Label( mainframe, text='is equivalent to' ).grid( column=0, row=1, sticky=E )
ttk.Label( mainframe, text='meters' ).grid( column=2, row=1, sticky=W )

# Step 7
def calculate( *args ):
  try:
    value = float( feet.get() )
    meters.set( 0.3048*value )
  except ValueError:
    pass
  return;

# Step 8 : The Go Button
ttk.Button( mainframe, text='Calculate', command=calculate ).grid( column=2, row=2, sticky=W )
root.bind('<Return>', calculate )

# Step 9
for child in mainframe.winfo_children():
  child.grid_configure( padx=5, pady=5 )

feet_entry.focus()
mainframe.columnconfigure( 1, weight=1 )
    
root.mainloop()

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
# https://www.youtube.com/watch?v=yI7NYgP54sw


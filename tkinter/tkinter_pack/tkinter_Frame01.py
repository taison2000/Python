#!/usr/bin/python
# Comment start with #
## double "pound" sign has different color



import tkinter as tk


root = tk.Tk()
root.title('Frame widget')

frame = Frame(root, width=8, height=1)
frame.pack()



root.mainloop()



# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html
#

# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
#
#

##-----------------------------------------------------------------------------
# Notes:
#  1. A frame is basically just a container for other widgets.
#
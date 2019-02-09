#!/usr/bin/python
# Comment start with #



import sys
import tkinter as tk
#from tkinter import messagebox as msgBox  #import tkMessageBox

top = tk.Tk()

lbl1 = tk.Label(None, text='This is a label #1')
lbl2 = tk.Label(None, text=' label #2', bg="light green", width=50, height=1)
lbl3 = tk.Label (None, text='ABCDEFHJIJKLMNOPQRSTUVWXYZ', bg="gray", height=3, width=30, \
         font=("Algerian", 35), fg="green", cursor='man', underline=(15))


lbl1.pack()
lbl2.pack()
lbl3.pack()

top.mainloop()



# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# https://docs.python.org/3.4/tutorial/modules.html
# http://www.tutorialspoint.com/python/tk_label.htm <-- Label
# http://effbot.org/tkinterbook/label.htm  <-- Label
#
# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
# Cursor
#
# # "arrow"
# # "circle"
# # "clock"
# # "cross"
# # "dotbox"
# # "exchange"
# # "fleur"
# # "heart"
# # "heart"
# # "man"
# # "mouse"
# # "pirate"
# # "plus"
# # "shuttle"
# # "sizing"
# # "spider"
# # "spraycan"
# # "star"
# # "target"
# # "tcross"
# # "trek"
# # "watch"




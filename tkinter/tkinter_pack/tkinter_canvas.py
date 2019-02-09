#!/usr/bin/python

# Comment start with #
# No multiple line comment

   
import tkinter as tkWin
from tkinter import messagebox as msgBox  #import tkMessageBox

top = tkWin.Tk()

Cvas = tkWin.Canvas (top, bg="blue", height=250, width=300) 

coord = 10, 10, 240, 210
arc = Cvas.create_arc(coord, start=90, extent=350, fill="red")

Cvas.pack()

top.mainloop()


# NOTE:
# https://mail.python.org/pipermail//tkinter-discuss/2011-August/002916.html
#  - tkMessageBox has been renamed to messagebox in Python 3.x.
#  - Module is not available in tkinter
#  - code : from tkinter import messagebox

# http://www.tutorialspoint.com/python/tk_canvas.htm     # Canvas
# http://www.tutorialspoint.com/python/python_gui_programming.htm    # GUI Programming
#

# Canvas support these standard items.
#  - arc     
#     arc = canvas.create_arc (coord, start=0, extent=150, fill="blue")
#  - image   
#     filename = PhotoImage (file = "sunshire.gif")
#     image = canvas.create_image (50, 50, anchor=NE, image=filename)
#  - line
#     line = canvas.create_line(x0, y0, x1, y1, ..., xn, yn, option)
#  - oval
#     oval = canvas.create_oval(x0, y0, x1, y1, option)
#  - polygon
#     oval = canvas.create_polygon (x0, y0, x1, y1, ... xn, yn, option)
#

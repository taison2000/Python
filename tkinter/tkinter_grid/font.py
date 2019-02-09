#!/usr/bin/python
# Comment start with #



import sys
import tkinter as tk

'''===== font ====='''
from tkinter import font

top = tk.Tk()

def listOfAllSystemFonst():
  allFonts = font.families()  ## allFonts : Tuple of all system fonts
  for f in allFonts:
    print( f )
  return

listOfAllSystemFonst()

lbl1 = tk.Label( None, text='Font=Cooper Size=40', font=("Cooper", 40) )
lbl2 = tk.Label( None, text=' Font=Engravers MT Expanded Medium Size=20', bg="light green", font=("Engravers MT Expanded Medium", 20) )
lbl3 = tk.Label( None, text='ABCDEFHJIJKLMNOPQRSTUVWXYZ', bg="gray", height=3, width=30, \
         font=("Harlow", 35), fg="green", cursor='cross', underline=(15) )


lbl1.grid()
lbl2.grid()
lbl3.grid()

top.mainloop()

#from tkinter import messagebox as msgBox  
## tkMessageBox (v2.x) ==> messagebox (v3.x)


# -----------------------------------------------------------------------------
# Resources
# http://www.tutorialspoint.com/python/python_gui_programming.htm
# 
# https://docs.python.org/3.4/tutorial/modules.html

# http://www.tutorialspoint.com/python/tk_label.htm <-- Label
# http://www.tutorialspoint.com/python/tk_cursors.htm <-- cursor names
# http://effbot.org/tkinterbook/label.htm  <-- Label
#
# Windows - Font
#  - "Control Panel" -> "Appearance and Personalization" -> "Fonts"
#  - "Control Panel" -> "Fonts"
#
#     * Arial
#     * Forte
#     * Forte
#     * Gungsuh
#     * Harrington
#

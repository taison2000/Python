

##-----------------------------------------------------------------------------
## PanedWindow
#   is a container widget that may contain any number of panes, 
#   arranged horizontally or vertically.
#
#   Each pane contains one widget and each pair of panes is separated by 
#   a moveable (via mouse movements) sash. Moving a sash causes the widgets 
#   on either side of the sash to be resized.
#


##-----------------------------------------------------------------------------
## Syntax
"""
## PanedWindowWidget = PanedWindow( master, option, ... )
"""
# master : This represents the parent window.
#
# Option	Description
# -----------------------------------------------------------------------------
#  bg            The color of the slider and arrowheads when the mouse is not over them.
#  bd            The width of the 3-d borders around the entire perimeter of the trough, and also the width of the 3-d effects on the arrowheads and slider. Default is no border around the trough, and a 2-pixel border around the arrowheads and slider.
#  borderwidth   Default is 2.
#  cursor        The cursor that appears when the mouse is over the window.
#  handlepad     Default is 8.
#  handlesize    Default is 8.
#  height        No default value.
#  orient        Default is HORIZONTAL.
#  relief        Default is FLAT.
#  sashcursor    No default value.
#  sashrelief    Default is RAISED.
#  sashwidth     Default is 2.
#  showhandle    No default value
#  width         No default value.


"""
## Methods
"""
# -----------------------------------------------------------------------------
# add( child, options )
#   Adds a child window to the paned window.
#
# get( startindex [,endindex] )
#   This method returns a specific character or a range of text.
#
# config( options )
#   Modifies one or more widget options. If no options are given, 
#   the method returns a dictionary containing all current option values.


## --- help("tkinter.PanedWindow")


##-----------------------------------------------------------------------------
from tkinter import *

#Pane = PanedWindow()
#Pane = PanedWindow(showhandle=True)
#Pane = PanedWindow(orient=VERTICAL) # Default : orient=HORIZONTAL?
#Pane = PanedWindow( orient=VERTICAL, relief=SUNKEN, bg="red")
Pane = PanedWindow( orient=VERTICAL, relief=RAISED, bg="red")
#Pane = PanedWindow( orient=HORIZONTAL)
Pane.pack(fill=BOTH, expand=1)

print( "PanedWindow configure options")
paneConfig = Pane.config()
for option in paneConfig:
    #print("%-15s"%option," : ", type(option) )
    print("%-15s"%option," : ", paneConfig[option] )
paneConfigure = Pane.configure()
if paneConfig == paneConfigure:
    print("config == configure")
else:
    print("config != configure")
    
label1 = Label(Pane, text="Label One")
Pane.add( label1 )

label2 = Label(Pane, text="Label Two")
Pane.add( label2 )

label3 = Label(Pane, text="Label Three")
Pane.add( label3 )

label4 = Label(Pane, text="Label Four")
Pane.add( label4 )

label5 = Label(Pane, text="Label Five")
Pane.add( label5 )


mainloop()


##-----------------------------------------------------------------------------
"""
Resource:
 - http://www.tutorialspoint.com/python/tk_panedwindow.htm
 - http://www.tkdocs.com/tutorial/windows.html#dialogs
 - http://tkinter.unpythonic.net/wiki/
"""

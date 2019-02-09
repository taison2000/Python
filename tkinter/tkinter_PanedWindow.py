

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

#Pane1 = PanedWindow()
Pane1 = PanedWindow(showhandle=True)
#Pane1 = PanedWindow(orient=VERTICAL) # Default : orient=HORIZONTAL?
Pane1.pack(fill=BOTH, expand=1)

left = Label(Pane1, text="left pane")
Pane1.add( left )

left2 = Label(Pane1, text="left pane 2")
Pane1.add( left2 )

# Pane2 is inside Pane1 ?
#Pane2 = PanedWindow( Pane1 )
Pane2 = PanedWindow(Pane1, orient=VERTICAL, relief=SUNKEN, bg="red")
#Pane2 = PanedWindow(Pane1, orient=HORIZONTAL)
Pane1.add(Pane2)

top = Label(Pane2, text="top pane")
Pane2.add(top)

bottom = Label(Pane2, text="bottom pane")
Pane2.add(bottom)

mainloop()


##-----------------------------------------------------------------------------
"""
Resource:
 - http://www.tutorialspoint.com/python/tk_panedwindow.htm
 - http://www.tkdocs.com/tutorial/windows.html#dialogs
 - http://tkinter.unpythonic.net/wiki/
"""

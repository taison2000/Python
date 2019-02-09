#!c:\Python35\python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Module - pyautogui
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - installation : "pip install pyautogui"

"""
## ----------------------------------------------------------------------------

import os
import time
import pyautogui

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - pyautogui.
 - pyautogui.
 - pyautogui.center
 - pyautogui.click
 - pyautogui.
 - pyautogui.dragRel
 - pyautogui.dragTo
 - pyautogui.doubleClick
 - pyautogui.hotkey
 - pyautogui.
 - pyautogui.keyDown
 - pyautogui.keyUp
 - pyautogui.locateOnScreen
 - pyautogui.middleClick
 - pyautogui.mouseDown
 - pyautogui.mouseUp
 - pyautogui.
 - pyautogui.moveRel
 - pyautogui.moveTo
 - pyautogui.position
 - pyautogui.press
 - pyautogui.
 - pyautogui.rightClick
 - pyautogui.screenshot
 - pyautogui.scroll
 - pyautogui.size
 - pyautogui.
 - pyautogui.typewrite
 - pyautogui.
 - pyautogui.
 
"""

## ----------------------------------------------------------------------------
# << Automate The Boring Stuff With Python >> Page:430
# --- Group By Function ---
# pyautogui.moveTo()
# pyautogui.moveRel()
# pyautogui.dragTo()
# pyautogui.dragRel()
# pyautogui.click()
# pyautogui.rightClick()
# pyautogui.middleClick()
# pyautogui.doubleClick()
# pyautogui.mouseDown()
# pyautogui.mouseUp()
# pyautogui.scroll()
# pyautogui.typewrite()
# pyautogui.press()
# pyautogui.keyDown()
# pyautogui.keyUp()
# pyautogui.hotkey()
# pyautogui.size() 
# pyautogui.screenshot()
# pyautogui.locateOnScreen()
# pyautogui.locateCenterOnScreen()
# pyautogui.center()
# pyautogui.position()


## ----------------------------------------------------------------------------
""" 
# --- Group By Function ---
# .moveTo( x, y )
# .moveRel( xOffset, yOffset )
# .dragTo( x, y )
# .dragRel( xOffset, yOffset )
# .click( x, y, button )
# .rightClick()
# .middleClick()
# .doubleClick()
# .mouseDown()
# .mouseUp()
# .position()
# .scroll( units )
# .typewrite( message )
# .typewrite( [key1, key2, key3] )
# .press( key )
# .keyDown( key )
# .keyUp( key )
# .hotkey( [key1, key2, key3] )
# .size() 
# .screenshot()
# .locateCenterOnScreen( path_and_name_of_image )
# .locateOnScreen( path_and_name_of_image )
# .
"""

## ----------------------------------------------------------------------------
"""
Names:
-button : 'left', 'right', 'middle' (p420)
"""

## ----------------------------------------------------------------------------
## Display message box
#  - pyautogui.alert("pyautogui alert message")   => Return: 
#  - pyautogui.confirm('Shall I proceed?')       => Return: 'OK', 'Cancel'
#  - pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])  => Return: 'A' 'B' 'C'
#  - pyautogui.prompt('What is your name?')       => Return : User Input
#  - pyautogui.password('Enter password (text will be hidden)')   => Return : User Input


## ----------------------------------------------------------------------------
def method_MethodName():
    """
    Put a module method here
    """
    pass
    return


## ----------------------------------------------------------------------------
def method_click():
    """
    click a mouse button
    """

    ## These two are same
    pyautogui.click(500, 500, button='right')
    pyautogui.rightClick(500, 500)

    pyautogui.click(500, 500, button='left')
    pyautogui.click(500, 500)

    pyautogui.doubleClick(500, 500)

    return;


## ----------------------------------------------------------------------------
def method_locateOnScreen():
    """
    locateOnScreen : 
        if found - return a tuple (x-cor, y-cor, width, height)
        Not found - return 'None'
    """

    Location = pyautogui.locateOnScreen(r'C:\Users\Sam\Programming\Python\Images\up.png')
    # Location == ( x-cor, y-cor, width, height)
    # Location == None ( not found image )


    # get center
    xyCenterCor = pyautogui.center( Location )
    pyautogui.click( xyCenterCor )

    Home = pag.locateOnScreen(r'.\Images\Home.png')  # ( x-cor, y-cor, width, height)

    # Only look at the specific region.
    Loction  = pyautogui.locateOnScreen( "screen_0_0_300_400.png", region=(0, 0, 400, 500) )

    return;


## ----------------------------------------------------------------------------
def method_moveTo():

    # Takes 2.5 seconds from current position move to the specified location
    pyautogui.moveTo( 100, 100, duration=2.5 ) 

    return;

## ----------------------------------------------------------------------------
def method_position():
    """
    get current mouse position, return tuple (x-cord, y-cord)
    """
    pos = pyautogui.position() # (789, 92)


## ----------------------------------------------------------------------------
def method_screenshot():
    """
    ss = pyautogui.screenShot(imageFilename=None, region=None)
    """
    ss = pyautogui.screenShot()
    ss = pyautogui.screenShot("MyScreenCapture.png")
    ss = pyautogui.screenshot(r"c:\Temp\myScreenCapture.png")

    return

## --- pyautogui.size() ---
def pyautogui_size():
    width, height = pyautogui.size()

    return (width, height)

## ----------------------------------------------------------------------------
def method_typewrite():
    """
    Keyboard key string         Meaning
    'enter'                      Enter
    'esc'                        ESC
    'shiftleft', 'shiftrigtht'   left and right SHIFT
    'altleft', 'altright'        left and right ALT
    'ctrlleft', 'ctrlright'      left and right CTRL
    'tab' or '\t'                TAB
    'backspace', 'delete'        BACKSPACE, DELETE
    'pageup', 'pagedown'         PAGE UP, PAGE DOWN
    'home', 'end'                HOME, END
    'up', 'down', 'left', 'right'
    'f1', 'f2', ... 'f12'        Functios keys
    'volumemute', 'volumeup', 'volumedown'
    'pause'                      PAUSE
    'capslock', 'numlock', 'scrolllock'
    'insert'                     INSERT, INS
    'printscreen'                PRINT SCREEN
    'winleft', 'winright'        left and right WIN keys (Windows)
    'command'                    command key (OS X)
    'option'                     OPTION (OS X)
    """
    
    pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'])   # 'XYab'

    
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    module_method()

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------      
if __name__ == "__main__":
    main()


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))


"""


## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 - Book: Automate the Boring Stuff With Pytthon - CH 18 ()
 - https://pyautogui.readthedocs.org/en/latest/
 - http://pyautogui.readthedocs.org/en/latest/screenshot.html
  
"""


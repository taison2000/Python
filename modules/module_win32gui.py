#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - pyautogui
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - download pywin32 and install it
"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - win32gui.()
 - win32gui.()
 - win32gui.()
 - win32gui.()
 - win32gui.()
 - win32gui.()
 - 
 - 
 - 
 - 
 - 
 - 
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : win32gui.Attribute
 - .BASIC_FORMAT
 - .CRITICAL
 - .DEBUG
 - .ERROR
 - .FATAL
 - .INFO
 - .NOTSET
 - .WARN
 - .WARNING
"""

## ----------------------------------------------------------------------------
import os
import time
import module_name

## ----------------------------------------------------------------------------
def method_Name():
    """
    Put a module method here
    """
    pass
    return


## ----------------------------------------------------------------------------
## use callback to scan through all Windows??
def callback(hwnd, extra):
	print(type(hwnd))
	print(hwnd)
	time.sleep(2)
	      
	rect = win32gui.GetWindowRect(hwnd)
	x = rect[0]
	y = rect[1]
	w = rect[2] - x
	h = rect[3] - y
	print("Window %s:" % win32gui.GetWindowText(hwnd))
	print("\tLocation: (%d, %d)" % (x, y))
	print("\t    Size: (%d, %d)" % (w, h))
    
## here is how to run the 'callback' function
win32gui.EnumWindows(callback, None)


## ----------------------------------------------------------------------------
def how_to_scan_windows_title():
    import win32gui
    tempWindowName=win32gui.GetWindowText (win32gui.GetForegroundWindow())
    import time
    while True:
        if (tempWindowName==win32gui.GetWindowText (win32gui.GetForegroundWindow()))
            pass
        else
            tempWindowName=win32gui.GetWindowText (win32gui.GetForegroundWindow())
            #do what you want
        time.sleep(0.1)

def win32gui_summary():
    className = win32gui.GetClassName(1640416)
    print(className)

    # find window handle from class named "gdkWindowToplevel"
    hwnd = win32gui.FindWindow("gdkWindowToplevel", None)   # hwnd == 5182414
    print(hwnd) # window handle (integer, or 0 if not valid)
    
    WindowName=win32gui.GetWindowText(hwnd)
    print(hwnd) # 'ACC 2.0 Power Module v1.03.000 Instance 1'
    
    rect = win32gui.GetWindowRect(hwnd)
    print(rect) # (619, 7, 1225, 535) == (h_pos, v_pos, h_size, v_size)
    # or (x, y, w, h)
    
    ## get window handle by window title "Windows Task Manager" in this case
    hwnd = win32gui.FindWindow(None, "Windows Task Manager")
    # hwnd == 6952660

    ## get foreground window handle
    window = win32gui.GetForegroundWindow()
    
    ## get desktop window
    win32gui.GetDesktopWindow()
    
    ## get window's title from handle
    WindowText = win32gui.GetWindowText(hwnd)   # 'ACC 2.0 Power Module v1.03.000 Instance 1'
    
def find_child_windows():
    import win32gui

    MAIN_HWND = 0

    def is_win_ok(hwnd, starttext):
        s = win32gui.GetWindowText(hwnd)
        if s.startswith(starttext):
            print(s)
            global MAIN_HWND
            MAIN_HWND = hwnd
            return None
        return 1

    def find_main_window(starttxt):
        global MAIN_HWND
        win32gui.EnumChildWindows(0, is_win_ok, starttxt)
        return MAIN_HWND

    def winfun(hwnd, lparam):
        s = win32gui.GetWindowText(hwnd)
        if len(s) > 3:
            print("winfun, child_hwnd: %d   txt: %s" % (hwnd, s))
        return 1

    def main():
        ## main window with this name
        main_app = 'EditPlus'
        main_app = 'ACC 2.0 ACM Module v1.02.000 Instance 1'
        
        hwnd = win32gui.FindWindow(None, main_app)
        print(hwnd)
        if hwnd < 1:
            hwnd = find_main_window(main_app)
        print(hwnd)
        if hwnd:
            win32gui.EnumChildWindows(hwnd, winfun, None)

    main()

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    method_Name()
    return

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()



## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 - http://timgolden.me.uk/pywin32-docs/contents.html
 - http://docs.activestate.com/activepython/3.1/pywin32/win32gui.html
  
"""

## ----------------------------------------------------------------------------
"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))



"""


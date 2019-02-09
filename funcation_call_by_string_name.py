#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

def Function_Install():
    print( "This Function called by installation" )
    return



'''
Base on string name to call functions.
'''
if __name__ == "__main__":

    # Function to run
    method_name = 'Function_Install' ##<- function name string

    # Setup a Dictionary
    myDict = globals().copy()
    myDict.update( locals() )

    # get function from dictionary
    method = myDict.get( method_name )

    if not method:
        raise Exception("Method %s not implemented" % method_name)

    method()


## ----------------------------------------------------------------------------
## Resource:
"""
 - http://stackoverflow.com/questions/7936572/python-call-a-function-from-string-name
 - https://docs.python.org/3/library/functions.html#globals
 - 
"""

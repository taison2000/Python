#!/Python34/python
#!/usr/bin/python

def Function_01():
    print( "Function #01" )
    return

def Function_02():
    print( "Function #02" )
    return

def Function_03():
    print( "Function #03" )
    return


'''
Use dictionary to call functions.
'''
methods = { 
  'Func_01': Function_01,
  'Func_02': Function_02,
  'Func_03': Function_03,
}


if __name__ == "__main__":

    # Function to run
    method_name = 'Func_03' # set by the command line options

    if method_name in methods:
        methods[method_name]() # + argument list of course
    else:
        raise Exception("Method %s not implemented" % method_name)
    #return
else:
    pass
    #return


## ----------------------------------------------------------------------------
## Resource:
"""
 - http://stackoverflow.com/questions/7936572/python-call-a-function-from-string-name
 
"""

# -*- coding: utf-8 -*-
"""
try:
except:

"""
##-----------------------------------------------------------------------------
## Built-in Exceptions
"""
Source: https://docs.python.org/3/library/exceptions.html#bltin-exceptions

- SyntaxError
- NameError
- TypeError
- ValueError
- ZeroDivisionError
"""

##-----------------------------------------------------------------------------
def Spam(divideBy):
    return 42/divideBy

def runSpam():
    try:
        print(spam(2))
        print(spam(12))
        print(spam(0))
        print(spam(5))
        print(spam(7))
        print(spam(222))
    except Exception as e:
        print(type (e)) # <class 'ZeroDivisionError'>
        print(e)        # division by zero
    finally:  # this will executed regardless 'try' success or not.
        print("end")
    return

##-----------------------------------------------------------------------------
def exception_test():
    """
    Source location:
      http://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occured
    """
    try:
        ser = serial.Serial(1)
    except Exception as ex:
        template = "Critical Telnet Error of type {0} occurred. Arguments:\n{1!r}"
        message = template.format( type(ex).__name__, ex.args )
        print( message )
    return
    
def exception_test01():
    """
    Source location:
      http://stackoverflow.com/questions/9823936/python-how-do-i-know-what-type-of-exception-occured
        
    """
    try:
        ser = serial.Serial(1)
    except Exception as ex:
        eMsg = ex.args[0]
        print( eMsg )
    return
    
def division_by_zero_exception():
    try:
        a=1
        a=a/0
    except Exception as e:
        print( "Exception happened" )
        print( e )  ## 'division by zero'
        type( e )   ## <class 'ZeroDivisionError'

    return

def try_except_else():
    # if try without any error, else block will be executed.
    try:
        fo = open("license.txt", 'r')
    except Exception as error:
        print(error)
    else:
        print("what about else?")
    return
    
# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------
if __name__ == '__main__':
    exception_test()


##-----------------------------------------------------------------------------
"""
Resources:
 - 
 - 

"""

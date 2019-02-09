##-----------------------------------------------------------------------------
"""
# Properties:
#  - portstr : ser.portstr => 'COM1'
#  - 
#  - 
#  - 
#  - 
#  - 
#
#
# Methods:
# * Data Buffer
#  - flushInput()
#  - flushOutput()
#  - inWaiting()
#  - outWaiting()
#  - 
#  - close()  : ser.close() => Close serial port
#  - isOpen() : ser.isOpen => True, False
#  - 
#  - open()   : ser.open()
#  - 
#  - 
#  - 
#
# Others:
#  - 
#  - 
#  - 
#  - 
#  - 
#  - 
"""


import sys
import time
import serial

global ser

def OpenComPort(ComNum):
    global ser
    ser = serial.Serial(ComNum-1) 
    # NOTE: no baudrate, nor timeout

def method__isOpen():
    ser1 = serial.Serial(0) # Open COM1
    if ser1.isOpen() == True:
        print ('Yes, comport is opened')
    else:
        print ('No, comport is not opened')
    
def opencom(COMPort):
	"""
	Open the serial port with 4800 bps
	"""
	import serial
	global ser
	ser=serial.Serial(COMPort-1,4800,timeout=1)

def closecom():
	"""
	Close serial port
	"""
	global ser
	ser.close()

def ListAllComports():
    l = []
    for i in rang(30):
        try:
            ser=serial.Serial(i)
            l.append(i+1)
        except:
            print("Not able to open com port")

def ComPortOpenError():
    try:
        ser = serial.Serial(22)
    except Exception as ex:
        template = "An exception of type {0} occured. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print (message)
    
def CatchSerialExceptions():
    l=[]
    for i in range(31):
        try:
            ser = serial.Serial(i)
            ser.close()
            l.append(i+1)
        except Exception as ex:
            err = ex.args[0]
            if 'FileNotFoundError' in err:
                print ("COM port is not present")
            elif 'PermissionError' in err:
                print ('COM port is opened by other program')
                l.append(i+1)
            else:
                print ('open error')
        finally:
            print("close comport")

    return (l)




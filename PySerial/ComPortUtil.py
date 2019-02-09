# -----------------------------------------------------------------------------
# 			Hunter Industries
#
# updated       Description
# ---------------------------------------------
# 05/27/2015   	 Initial Release
#
# -----------------------------------------------------------------------------

##-----------------------------------------------------------------------------

import sys
import time
from collections import OrderedDict
import crc16pure as crc
from funcByteArray import stripResponsePreamble, ByteToInt, printByteArray
from fileLogUtil import TestLog, DebugLog, CloseTestLog, CloseDebugLog, PrintAndLogAll, CloseAllLogFile

global ser, comPort
ser=None
comPort=7

## --- CONSTANTS ---
CONST_PREAMBLE = b'\xFF\xFF\x3C\xC3'

#enablePrint = True
enablePrint = False



def openCom(COMPort):
    """
    Open the serial port with 4800 bps
    """
    import serial
    global ser
    #ser=serial.Serial(COMPort-1,4800,timeout=1)
    try:
        ser=serial.Serial(COMPort-1,4800,timeout=1)
    #except PermissionError:
    except :
        print("  ***> Not able to open COM port")
        print("  ***> Maybe COM port is opened by other program")
        sys.exit(1) # exit()

def closeCom():
	"""
	Close serial port
	"""
	global ser
	ser.close()

def initComPort():
	"""
	Initialize com port
	"""
	import time
	
	try:
		openCom(SystemConfig1021.ComPort)
	except:
		print ("COM port is open")
	else:
		print ("COM port is open")


def executeCommand (cmdByteArray):
    global ser, comPort
    if ser==None:
        openCom(comPort)
        print("open com from executeCommand")
    ser.flushInput()  #<- clear input buffer
    ser.write(cmdByteArray) 

def clearReadBuffer():
    global ser, comPort
    if ser==None:
        openCom(comPort)
        print("open com from clearReadBuffer")
    data = ser.read(300)


def readResponse (Length):
    global ser
    data = ser.read(Length) # Note: data is in byte format (b'\xff\xff\x3c\xc3\x...')
    return data


##-----------------------------------------------------------------------------  
def main():
    openCom(7)

    closeCom()


if __name__ == "__main__":
    main()


#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
# ------------------------------------------------------------------------------
   Mightex LED driver controller
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ------------------------------------------------------------------------------

  Device Mode:
    0 - Disable
    1 - Normal
    2 - Strobe
    3 - Trigger
    
  Commands:
    * Set mode 
      Command : MODE CHx mode
      Example : MOCE 1 2    ; Set channel 1 to mode 2
    * Query mode
      Command : ?MODE CHx
      Example : ?MODE 2     ; Query channel 2 mode
      
   Normal Mode
    * Set NORMAL mode
      Command : NORMAL CHx Imax Iset
      Example : NORMAL 2 900 400   ; Set channel 2 max current to 900 mA, Working current to 400 mA                                   ; (Note: seems there is bug, does not really turn on the Iset)
    * Set NORMAL mode working current
      Command : CURRENT CHx Iset
      Example : CURRENT 3 350      ; Set channel 3 working current to 350 mA
    * Query Normal mode current
      Command : ?CURRENT CHx
      Example : ?CURRENT 2         ; The last number of the response is CURRENT setting, the second to last is Imax
                                   ; Typical Response : #27 103 496 989 1487 1986 130 10 9216 16 888 389
                                                                                                  ^   ^
                                                                                                 Imax Iset
   Strobe Mode
    * Set strobe mode
      Command: STROBE CHx Imax Repeat
      Example :
    * Get strobe mode parameters
      Command : ?STROBE CHx
      Example : ?STROBE 2
    * Set strobe profile
      Command : STRP CHx Step Iset Tset
      Example : STRP 1 0 500 2000   ; Channel_1, step 0, 500 mA, 2000 uS
    * Get strobe mode profile
      Command : ?STRP CHx
      Example : ?STRP 2   ; Return : "#Iset1 Test1
                                      Iset2 Test2
                                       ....."

   Trigger Mode
    * Set Trigger Mode Parameter
      Command : TRIGGER CHx Imax Polarity(0=Rising edge trigger, 1=Falling)
      Example : TRIGGER 2 1000 0  ; Set channel 2 to 1000 mA max current, rising edge trigger
    * Get Trigger Mode parameter
      Command : ?TRIGGER CHx
      Example : ?TRIGGER 2
    * Set Trigger Profile
      Command : TRIGP CHx Step Iset Test
      Example : TRIGP 1 0 500 2000  ; Channel 1, 0 step, 500 mA, 2000 uS
    * Get Trigger Mode profile
      Command : ?TRIGP CHx
      Example : ?TRIGP 2    ;
      
  Other commands:
    * Get channel load voltage
      Command : LoadVoltage CHx
      Example : LOADVOLTAGE 2     ; Return in mV. Example : #2:11996 (channel_2, 11.996 volts)
    * Reset device
      Command : RESET
    * Restore Factory Default
      Command : RESTOREDEF
    * Store all settings to NV memory
      Command : STORE
    * Device Info
      Command : DEVICEINFO

  Response:
    ## - command exec OK
    #! - Command valid, but error in exec
    #? - invalid command
    #"ASCII String" - device response from last command
  
"""


# CH1=Green CH2=Blue CH3=Red

# ------------------------------------------------------------------------------
# Package Import
# ------------------------------------------------------------------------------
import visa
import time
import sys

comMightexString = "COM5"

# ------------------------------------------------------------------------------
# Connect VISA Resource Manager
# ------------------------------------------------------------------------------
def connectVisaRM():
  rm = visa.ResourceManager()
  print ("List all VISA resources:")
  print (rm.list_resources())
  
  print ("\nDisplay connected equipment on GPIB0::14")
  # Need some re to process if GPIB0::14 exists 
  gpib0_14 = rm.open_resource('GPIB0::14::INSTR')
  print (gpib0_14.query('*idn?'))
  # need re to process the result
  
  print("Current GPIB session: ")
  print( gpib0_14.session )
  gpib0_14.close()
  

# ------------------------------------------------------------------------------
# Analysis if string is '\r\n'
# ------------------------------------------------------------------------------
def analysisLR (strData):
  if strData == '\r\n':
    return True
  elif strData == '\n\r':
    return True
  else:
    return False
  
  
# ------------------------------------------------------------------------------
# Open the comport for Mightex
# ------------------------------------------------------------------------------
def openCom():
  global com5
  rm = visa.ResourceManager()
  com5 = rm.open_resource(comMightexString)

# ------------------------------------------------------------------------------
# Close the comport for Mightex
# ------------------------------------------------------------------------------
def closeCom():
  global com5
  #close com port session
  print ("COM session: ")
  print(com5.session)
  print("Close COM port")
  time.sleep(1)
  com5.close()
  

# ------------------------------------------------------------------------------
# Query with ASCII
# ------------------------------------------------------------------------------ 
def openCom_ascii_query():
  
  comData=com5.query_ascii_values ("deviceinfo", "s")
  print ("\nDevice Info: ")
  print (comData)
  
  comData=com5.query_ascii_values ("?mode 1", "s") 
  print ("CH1 Mode: ")
  print (comData)

  comData=com5.query_ascii_values ("?mode 2", "s")
  print ("CH2 Mode: ")
  print (comData)

  comData=com5.query_ascii_values ("?mode 3", "s")
  print ("CH3 Mode: ")
  time.sleep(2)
  print (comData)

  comData=com5.query_ascii_values ("?mode 4", "s")
  print ("CH4 Mode: ")
  print (comData)

  # Set Mode 1
  print("Set Mightex LED mode to NORMAL")
  com5.write("NORMAL 1 1000 500")
  com5.write("NORMAL 2 1000 500")
  com5.write("NORMAL 3 1000 500")
  
  #change current
  #for i=0 range
  #set working current
  # range(start, stop[, step])
  """
  for i in range(0, 1000, 20):
    com5.write("CURRENT 1 %d" % i)
    time.sleep(1)
  """
  

def comInfo():
  print("baud rate: ", com5.baud_rate)
  print("bytes_in_buffer: ", com5.bytes_in_buffer)
  """
  com5.data_bits
  com5.flush
  com5.parity
  com5.stop_bits
  com5.xon_char
  """


# ------------------------------------------------------------------------------
# Get DeviceInfo
# ------------------------------------------------------------------------------
def getDeviceInfo():  
  print ("Device Info: ")
  com5.write ("deviceinfo")
  comData = com5.read()   # '\r\n' print(len(comData))
  comData = com5.read()
  print (comData)
  

# ------------------------------------------------------------------------------
# Get Mightex channel mode
# ------------------------------------------------------------------------------
def getChannelMode(channel):
  com5.write ("?mode %d" % channel)
  comData = com5.read() # '\r\n'  #print(len(comData)) == 2
  comData = com5.read()
  print ("CH%d Mode: " % channel)
  print (comData)
  return comData

# ------------------------------------------------------------------------------
# Set Mightex channel mode
#   com5.write("MODE 1 2")  ; channel 1, strobe mode
#   com5.write("MODE 2 1")  ; channel 2, normal mode
#   com5.write("MODE 2 3")  ; channel 2, trigger mode
# ------------------------------------------------------------------------------
def setChannelMode(comPort, Channel, Mode):
  comPort.write("MODE %d %d" % (Channel, Mode))
  comData = com5.read() # '\r\n'  print(len(comData)) == 2
  comData = com5.read()
  return 


# ------------------------------------------------------------------------------
# Configure Mightex normal mode operation
#   com5.write("NORMAL 1 1000 500") ; 
#   com5.write("NORMAL 2 1000 500")
#   com5.write("NORMAL 3 1000 500")
# ------------------------------------------------------------------------------
def configNormalModePara (comPort, Channel, Imax, Iset):
  comPort.write("NORMAL %d %d %d" % (Channel, Imax, Iset))
  comData = comPort.read()  # Read '\r\n'
  return

def setNormalCurrent (comPort, Channel, Iset):
  comPort.write("CURRENT %d %d" % (Channel, Iset))
  comData = comPort.read()  # Read '\r\n'
  return

def initMightex ():
  print ("Set channel mode ")
  setChannelMode(com5, 1, 3)
  setChannelMode(com5, 2, 3)
  setChannelMode(com5, 3, 2)
  setChannelMode(com5, 4, 2)

  print ("Get channel mode ")
  getChannelMode(1)
  getChannelMode(2)
  getChannelMode(3)
  getChannelMode(4)

  time.sleep(0.5)
  
  setChannelMode(com5, 1, 1)
  setChannelMode(com5, 2, 1)
  setChannelMode(com5, 3, 1)
  setChannelMode(com5, 4, 0)

  # Set NORMAL mode parameters
  configNormalModePara (com5, 1, 1000, 500)
  configNormalModePara (com5, 2, 1000, 500)
  configNormalModePara (com5, 3, 1000, 500)
  configNormalModePara (com5, 4, 1000, 500)
  time.sleep(1)

  com5.write("NORMAL 1 1000 0")
  com5.write("NORMAL 2 1000 0")
  com5.write("NORMAL 3 1000 0")
  time.sleep(1)
  


# ------------------------------------------------------------------------------
# Mightex operation
# ------------------------------------------------------------------------------
def runMightex():
  delay = 1
  channel = 3
  
  getDeviceInfo()
  
  initMightex ()

  # set working current
  #  range(start, stop[, step])
  for i in range(0, 1000, 50):
    com5.write("CURRENT %d %d" % (channel, i))
    print ("Ch:%d Current : %d" %(channel, i))
    time.sleep(1)

  channel=1
  for i in range(0, 1000, 50):
    com5.write("CURRENT %d %d" % (channel, i))
    print ("Ch:%d Current : %d" %(channel, i))
    time.sleep(1)

  channel=2
  for i in range(0, 1000, 50):
    com5.write("CURRENT %d %d" % (channel, i))
    print ("Ch:%d Current : %d" %(channel, i))
    time.sleep(1)

  # Turn off LEDs
  setNormalCurrent (com5, 1, 0)
  time.sleep(1)
  setNormalCurrent (com5, 2, 0)
  time.sleep(1)
  setNormalCurrent (com5, 3, 0)
  time.sleep(1)



# ------------------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------------------
def main():
  # VISA Resource Manager
  connectVisaRM()
  
  #open a com port
  openCom()
  #openCom_ascii_query()
  runMightex()
  closeCom();
  

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------ 
if __name__ == "__main__":
	main()
  #msg = main()
  #print(msg)
  #mainloop()



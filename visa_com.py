#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    pyvisa.visa
    ~~~~~~~~~~~

    Module to provide an import shortcut for the most common VISA operations.

    This file is part of PyVISA.

    :copyright: 2014 by PyVISA Authors, see AUTHORS for more details.
    :license: MIT, see COPYING for more details.
"""

"""
from __future__ import division, unicode_literals, print_function, absolute_import

from pyvisa import logger, __version__, log_to_screen, constants
from pyvisa.highlevel import ResourceManager
from pyvisa.errors import (Error, VisaIOError, VisaIOWarning, VisaTypeError,
                           UnknownHandler, OSNotSupported, InvalidBinaryFormat,
                           InvalidSession, LibraryError)
# This is needed to registry all resources.
from pyvisa.resources import Resource
"""

# CH1=Green CH1= CH2=

import visa
import time

def openCom_ascii_query():
  rm = visa.ResourceManager()
  com5 = rm.open_resource("COM5")
  
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
  
  #close com port session
  print ("COM session: ")
  print(com5.session)
  print("Close COM port")
  time.sleep(1)
  com5.close()
 
def openCom():
  rm = visa.ResourceManager()
  com5 = rm.open_resource("COM5")
  
  com5.write ("deviceinfo")
  print ("\nDevice Info: ")
  time.sleep(3)
  comData = com5.read()
  print (comData)
  
  com5.write ("?mode 1") 
  print ("CH1 Mode: ")
  time.sleep(2)
  comData = com5.read()
  print (comData)

  com5.write ("?mode 2")
  print ("CH2 Mode: ")
  time.sleep(2)
  comData = com5.read()
  print (comData)

  com5.write ("?mode 3")
  print ("CH3 Mode: ")
  time.sleep(2)
  comData = com5.read()
  print (comData)

  com5.write ("?mode 4")
  print ("CH4 Mode: ")
  time.sleep(2)
  comData = com5.read()
  print (comData)

  # Set Mode 1
  com5.write("MODE 1 1")
  time.sleep(1)
  com5.write("MODE 2 1")
  time.sleep(1)
  com5.write("MODE 3 1")
  time.sleep(1)

  com5.write("NORMAL 1 1000 500")
  time.sleep(1)
  com5.write("NORMAL 2 1000 500")
  time.sleep(1)
  com5.write("NORMAL 3 1000 500")
  time.sleep(3)

  com5.write("NORMAL 1 1000 0")
  time.sleep(1)
  com5.write("NORMAL 2 1000 0")
  time.sleep(1)
  com5.write("NORMAL 3 1000 0")
  time.sleep(3)

  com5.write("CURRENT 1  0")
  time.sleep(1)
  com5.write("CURRENT 2  0")
  time.sleep(1)
  com5.write("CURRENT 3  0")
  time.sleep(3)
    
  com5.write ("CURRENT 1 10")
  time.sleep(3)
  com5.write ("CURRENT 1 50")
  time.sleep(3)
  com5.write ("CURRENT 1 100")
  time.sleep(3)
  com5.write ("CURRENT 1 150")
  time.sleep(3)
  com5.write ("CURRENT 1 200")
  time.sleep(3)
  com5.write ("CURRENT 1 250")
  time.sleep(3)
  com5.write ("CURRENT 1 300")
  time.sleep(3)
  com5.write ("CURRENT 1 350")
  time.sleep(3)
  com5.write ("CURRENT 1 400")
  time.sleep(3)
  com5.write ("CURRENT 1 450")
  time.sleep(3)
  com5.write ("CURRENT 1 500")
  time.sleep(3)
  com5.write ("CURRENT 1 550")
  time.sleep(3)
  com5.write ("CURRENT 1 600")
  time.sleep(3)
  com5.write ("CURRENT 1 650")
  time.sleep(3)
  com5.write ("CURRENT 1 700")
  time.sleep(3)
  com5.write ("CURRENT 1 750")
  time.sleep(3)
  com5.write ("CURRENT 1 800")
  time.sleep(3)
  com5.write ("CURRENT 1 850")
  time.sleep(3)

  #set working current
  # range(start, stop[, step])
  """
  for i in range(0, 1000, 20):
    com5.write("CURRENT 1 %d" % i)
    time.sleep(1)
  """
  
  #close com port session
  print ("COM session: ")
  print(com5.session)
  print("Close COM port")
  time.sleep(1)
  com5.close()
 
  
def main():
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
  
  #open a com port
  openCom()
  #openCom_ascii_query()
  
if __name__ == "__main__":
	main()
  #msg = main()
  #print(msg)
  #mainloop()


"""
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='PyVISA command-line utilities')
    subparsers = parser.add_subparsers(title='command', dest='command')

    info_parser = subparsers.add_parser('info', help='print information to diagnose PyVISA')

    console_parser = subparsers.add_parser('shell', help='start the PyVISA console')

    args = parser.parse_args()
    if args.command == 'info':
        from pyvisa import util
        util.get_debug_info()
    elif args.command == 'shell':
        from pyvisa import shell
        shell.main()
"""

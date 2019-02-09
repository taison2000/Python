#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Module - logging
  ~~~~~~~~~~~~~~~~~~~~~~
"""
## --- Methods ---
"""
#------------------------------------------------------------------------------
 - logging.BufferingFormatter.format()
 - logging.BufferingFormatter.formatFooter()
 - logging.BufferingFormatter.formatHeader()
 - logging.FileHandler()
 - logging.Filter()
 - logging.Filter.filter()
 - logging.Formatter()
 - logging.Handler()
 - logging.LogRecord()
 - logging.LogRecord.getMessage()
 - logging.Logger()
 - logging.LoggerAdapter()
 - logging.NullHandler(()
 - logging.StreamHandler()
 - logging.addLevelName()
 - logging.basicConfig()
 - logging.captureWarnings
 - logging.critical()
 - logging.debug()
 - logging.disable()
 - logging.error()
 - logging.exception()
 - logging.fatal()
 - logging.getLevelName()
 - logging.getLogRecordFactory.
 - logging.getLogger()
 - logging.getLoggerClass.
 - logging.info()
 - logging.lastResort.
 - logging.log()
 - logging.makeLogRecord()
 - logging.setLogRecordFactory()
 - logging.setLoggerClass()
 - logging.warn()
 - logging.warning()
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : logging.Attribute
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
# Logging Function    Level     Description
# -----------------------------------------------------------------------------
# logging.debug()     DEBUG     Lowest level
# logging.info()      INFO      General information
# logging.warning()   WARNING   Indicate potential problem
# logging.error()     ERROR     Failed
# logging.critical()  CRITICAL  Highest level.
# 

import os
import time
import logging

## logging.basicConfig only run once at the very biginning
#logging.basicConfig( filename=r'c:\temp\myProgramLog.txt', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s' )
logging.basicConfig( level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s' )

logging.debug( 'Start of program' )
logging.info( "Information logging")

##-----------------------------------------------------------------------------
## disable logging
#logging.disable( logging.CRITICAL )
#logging.disable( logging.DEBUG )
#logging.disable( logging.ERROR )
#logging.disable( logging.INFO )
#logging.disable( logging.WARNING )

##-----------------------------------------------------------------------------
## logging level 
# from least to most important
#   DEBUG 
#   INFO  
#   WARNING 
#   ERROR 
#   CRITICAL
#
# Level     Value
# ------------------
# CRITICAL  50
# ERROR     40
# WARNING   30
# INFO      20
# DEBUG     10
# UNSET     0
#
# For example, if logging level is set to WARNING.
#  logging.debug() and logging.info() 
#  

##-----------------------------------------------------------------------------
## Configure logging level
def change_logging_level():
    myLogHandle = logging.getLogger( "myLogger" )

    # set logging level
    myLogHandle.setLevel( logging.WARNING )
    
    ## ----- set logging level -----
    myLogHandle.setLevel( logging.ERROR )   # only log CRITICAL and ERROR
    
    myLogHandle.warning("warning log")    # No Log
    myLogHandle.error("error log")        # 2016-02-04 16:52:55,405 - ERROR - error log
    myLogHandle.critical("critical log")  # 2016-02-04 16:53:11,958 - CRITICAL - cti log
    myLogHandle.info("info log")          # No Log
    myLogHandle.debug("debug log")        # No Log

    ## ----- set logging level -----
    myLogHandle.setLevel( logging.INFO )    # log CRITICAL, ERROR, WARNING and INFO.
    
    myLogHandle.info("info log")          # 2016-02-04 16:53:51,181 - INFO - info log
    myLogHandle.debug("debug log")        # No Log

    return

##-----------------------------------------------------------------------------
def multiLogger():
    """
    Start with multiple loggers to serve different purpose.
    """

    myLog01 = logging.getLogger( "myLogger_01" )
    myLog02 = logging.getLogger( "myLogger_02" )

    myLog01.setLevel( logging.ERROR )
    myLog02.setLevel( logging.INFO )

    myLog01.info("info log")        ## No log - below "ERROR" level
    myLog01.error("error log")      # 2016-02-05 09:52:08,772 - ERROR - error log
    myLog01.warning("warning log")  ## No log - below "ERROR" level

    myLog02.info("info log")    # 2016-02-05 09:52:17,620 - INFO - info log
    myLog02.error("error log")  # 2016-02-05 09:52:25,788 - ERROR - error log
    myLog02.debug("debug log")  ## No log - below "INFO" level
    myLog02.warning("warning log")  # 2016-02-05 09:52:53,297 - WARNING - warning log

    return

##-----------------------------------------------------------------------------
## Logging to a File
def setup_logging_file():
    logging.basicConfig( filename=r'c:\temp\myProgramLog.txt', \
        level=logging.DEBUG, \
        format=' %(asctime)s - %(levelname)s - %(message)s')

    return

def factorial(n):
    logging.debug('Start of factorial(%s%%)' % (n) )
    total = 1
    for i in range(n+1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total) )
    logging.debug( 'End of factorial(%s%%)' %(n) )
    return total
    
def how_to_change_log_file_name():
    """
    http://stackoverflow.com/questions/13839554/how-to-change-filehandle-with-python-logging-on-the-fly-with-different-classes-a
    """
    
    # get root logger
    log = logging.getLogger()
    
    # remove log handlers
     for hdlr in log.handlers[:]:
        log.removeHandler(hdlr)
        
    # add log handler
    log.addHandler(logging.FileHandler(r'c:\temp\newlog.txt')
    
    # now can write data to new log file
    log.info("new log info")
    log.critical("new log critical")
    
    return
    
    
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    print( factorial(5) )
    logging.debug( 'End of program' )

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()



##-----------------------------------------------------------------------------
"""
Resources:
 - https://pymotw.com/2/logging/
 - https://docs.python.org/3/library/logging.html

"""


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))
"""





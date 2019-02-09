#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

import telnetlib

## ----------------------------------------------------------------------------
"""
  Module - telnetlib
  ~~~~~~~~~~~~~~~~~~~~~~
"""

## ----------------------------------------------------------------------------
# Telnet Methods      Description
# -----------------------------------------------------------------------------
# Telnet.close()      Close the connection
# Telnet.expect()     Read until one from a list of a regular expressions matches. 
# Telnet.fileno()     Return the fileno() of the socket object used internally.
# Telnet.fill_rawq()       
# Telnet.get_socket()  
# Telnet.interact()
# Telnet.listener()   
# Telnet.msg()      
# Telnet.mt_interact()  
# Telnet.open()       
# Telnet.process_rawq() 
# Telnet.rawq_getchar() 
# Telnet.read_all()     
# Telnet.read_eager() 
# Telnet.read_lazy()  
# Telnet.read_sb_data() 
# Telnet.read_some()    
# Telnet.read_until()   
# Telnet.read_very_eager()  
# Telnet.read_very_lazy()
# Telnet.set_debuglevel() 
# Telnet.set_option_negotiation_callback()  
# Telnet.sock_avail()   
# Telnet.write()    
# 

## ----------------------------------------------------------------------------
# Telnet Attributes    Data Type    Description
# -----------------------------------------------------------------------------
# 
# Telnet.cookedq      'bytes'       
# Telnet.debuglevel   'int'         Indicate debug level, higher number with more outputs
# Telnet.eof          'int'         End-Of-File
# Telnet.host         'str'         
# Telnet.iacseq       'bytes'       
# Telnet.irawq        'int'         
# Telnet.option_callback
# Telnet.port         'int'         
# Telnet.rawq         'bytes'       
# Telnet.sb           'int'         
# Telnet.sbdataq      'bytes'       
# Telnet.sock    'socket.socket'  Whole lot of methods and attributes
# Telnet.timeout      'object'    



##-----------------------------------------------------------------------------
global ip, lh, portNumber
global gTelnetConn

gTelnetConn=None
localHostIp = "127.0.0.1"
localHost = "localhost"
portNumber = 3357

##-----------------------------------------------------------------------------
cmdGetGlobal = b'\xFF\xFF\xFF\x3C\xC3\x88\x00\xA9\x01\x00\x01\x00\x02\xF7\xB2'
cmdManualStartStation2 = b'\xFF\xFF\xFF\x3C\xC3\x82\x00\xA9\x01\x00\x05\x00\x5C\x01\x00\x02\x00\x48\x37'


def Telnet_expect(list, timeout=None):
  """
  telnet_expect(list, timeout=None)
    Read until one from a list of a regular expressions matches. 
  """
  
  return;
  
def Telnet__get_socket():
  """
  <socket.socket fd=160, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 52453), raddr=('127.0.0.1', 23)>
  """

  return;

##-----------------------------------------------------------------------------
##  Open Telnet Port
##-----------------------------------------------------------------------------
def OpenTelnet( ip=localHostIp, port=portNumber ):
  try:
    gTelnetConn = telnetlib.Telnet( ip, port )
  except TimeoutError:
    print( "Timeout Error : Not able to connect" )
    sys.exit( 1 )
  return;

def PortWrite( data ):
  """
  Write to Telnet Port
  """
  global gTelnetConn
  if gTelnetConn == None:
    OpenTelnet()
    
  gTelnetConn.write( data )
  
  return;

def PortRead():
  """
  Read from Telnet Port
  """
  global gTelnetConn
  if gTelnetConn == None:
    OpenTelnet()
 
  data = gTelnetConn.read()
  return data;
  
if __name__ == "__main__":
  gTelnetConn.write( cmdManualStartStation2 )
  
  
##-----------------------------------------------------------------------------
## --- Resources: ---
"""
 - http://www.pythonforbeginners.com/code-snippets-source-code/python-using-telnet
 - http://tools.ietf.org/html/rfc854.html
"""

##-----------------------------------------------------------------------------
## Notes:
#
# - Cooked data definition
#    Cooked data is raw data after it has been processed - 
#    that is, extracted, organized, and perhaps analyzed and 
#    presented - for further use.
# - help( telnetlib )
# - c:\\Python34\\Lib\\telnetlib.py
#
# 

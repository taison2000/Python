#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Module - socket
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - socket.AF_APPLETALK.bit_length()
 - socket.AF_APPLETALK.conjugate()
 - socket.AF_APPLETALK.from_bytes()
 - socket.AF_APPLETALK.to_bytes()
 - socket.AF_DECnet.
 - socket.AF_INET.
 - socket.AddressFamily()
 - socket...
 - socket.
 - socket.
 - socket.
 - socket.
 - socket.create_connection()
 - socket.dup()
 - socket.error()
 - socket.
 - socket.
 - socket.getdefaulttimeout()
 - socket.
 - socket.
 - socket.
 - socket.setdefaulttimeout()
 - socket.socket
 - socket.
 - socket.
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : socket.Attribute
 - .AF_APPLETALK.denominator
 - .AF_APPLETALK.imag
 - .AF_APPLETALK.name
 - .AF_APPLETALK.numerator
 - .AF_APPLETALK.real
 - .AF_APPLETALK.value
 - .errorTab
 - .
 - .
 - .
 - .
 - .
 - .
 - .
 - .
 - .
 - .
 - .
"""


## ----------------------------------------------------------------------------
import os
import time
import socket

## ----------------------------------------------------------------------------
def socket_connect():
  import socket
  s = socket.socket()
  host = '192.168.1.4'
  port = 80
  s.connect((host, port)) # Notice (host, port) is a tuple, connect only take 1 argument
  print (s) 
  ## s == <socket.socket fd=160, family=AddressFamily.AF_INET, 
  ## type=SocketKind.SOCK_STREAM, proto=0, laddr=('192.168.1.13', 49535), 
  ## raddr=('192.168.1.4', 80)>
  
  return;
  

def socket_gethostbyname():
  ip_google = socket.gethostbyname('www.google.com')
  ## => ip_google=='64,233,187.105'
  print (ip_google)
  return;

  
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  # range(start, stop[, step])
  for i in range(0, 1000, 20):
    print("Current Num : %d" % i)
    time.sleep(1)

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------      
if __name__ == "__main__":
	main()


## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 - https://docs.python.org/3.5/library/socket.html#socket.socket.settimeout
  
  
"""


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""




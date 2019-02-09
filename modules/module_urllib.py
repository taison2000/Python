#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Python
  ~~~~~~~~~~~

"""
## ----------------------------------------------------------------------------

import os
import time
import urllib # No 'urllib2' which in v2.x?

## ----------------------------------------------------------------------------
def urllib_request_urlopen():
  import urllib
  response = urllib.request.urlopen('http://www.google.com')
  html = response.read()
  print (html)
  
  ## another example
  response = urllib.request.urlopen('http://192.168.1.4')
  html = response.read()
  print (html)
  
  return;
  
def urllib_parse():
  url = 'http://pythonprogramming.net'
  values = {'s':'basic',
            'submit':'search'}
  data = urllib.parse.urlencode(values)
  print (data) # 's=basic&submit=search'
  data = data.encode('utf-8') # b's=basic&submit=search'
  req = urllib.request.Request(url, data)
  resp = urllib.request.urlopen( req )
  respData = resp.read()
  print( respData )
  
  return 
  
def urllib_request_google_fail():
  """
  This code will fail. Google would block program access instead of human typing access
  Response : 'HTTP Error 403: Forbidden'
  """
  try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print (x.read())
  except Exception as e:
    print (str(e))
    
  return;
  
def urllib_request_google_good():
  """
  
  """
  try:
    url = 'https://www.google.com/search?q=test'
    #x = urllib.request.urlopen('https://www.google.com/search?q=test')
  
    headers = {}
    # 'User-Agent' describe of what you use. Otherwise would be Python, google will block
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    req = urllib.request.Request( url, headers=headers )
    resp = urllib.request.urlopen( req )
    respData = resp.read()
    
    # Save result, too big to print
    saveFile = open('GoogleSearchWithHeaders.txt', 'w')
    saveFile.write( str(respData) )
    saveFile.close()
    
  except Exception as e:
    print (str(e))
    
  return;
  

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  urllib_request_urlopen()
  return;

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------      
if __name__ == "__main__":
  main()



"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""


## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""

  
  
"""

def urllib_request_Luxor_Json():
  """
  
  """
  import urllib, json
  try:
    url = 'http://192.168.1.4/IlluminateGroup.json'
    #url = 'http://192.168.1.4/'

    headers = {}
    # 'User-Agent' describe of what you use. Otherwise would be Python, google will block
    #headers['POST'] = "http://192.168.1.4/IlluminateGroup.json"
    #headers['POST'] = "IlluminateGroup.json"
    headers['Content-Type'] = "application/json"

    Data=b'{"GroupNumber":1, "Intensity":50}' # Data has to be in byte
    #Data = Data.encode('utf-8')
    
    req = urllib.request.Request( url, data=Data, headers=headers)
    print (req.headers)
    resp = urllib.request.urlopen( req )

    respData = resp.read()
    print (respData)
  except Exception as e:
    print (str(e))

  return;
  

#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
#!/usr/bin/env python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python : Google drive api
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    - pip install oauth2client
    
"""

from __future__ import print_function

import os
import time

from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/drive.file'
store = file.Storage('storage.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
    creds = tools.run_flow(flow, store, flags) \
            if flags else tools.run(flow, store)
DRIVE = build('drive', 'v2', http=creds.authorize(Http()))

FILES = (
    ('hello.txt', False),
    ('hello.txt', True),
)

for filename, convert in FILES:
    metadata = {'title': filename}
    res = DRIVE.files().insert(convert=convert, body=metadata,
            media_body=filename, fields='mimeType,exportLinks').execute()
    if res:
        print('Uploaded "%s" (%s)' % (filename, res['mimeType']))

if res:
    MIMETYPE = 'application/pdf'
    res, data = DRIVE._http.request(res['exportLinks'][MIMETYPE])
    if data:
        fn = '%s.pdf' % os.path.splitext(filename)[0]
        with open(fn, 'wb') as fh:
            fh.write(data)
        print('Downloaded "%s" (%s)' % (fn, MIMETYPE))
        
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    - range()
    """
    pass

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
else:
    """
    Called by other module
    """
    pass

##-----------------------------------------------------------------------------
## Python source code
# - https://www.python.org/downloads/source/

##-----------------------------------------------------------------------------
"""
Resources:

 - http://wescpy.blogspot.com/2015/12/google-drive-uploading-downloading.html
 - http://wescpy.blogspot.com/search/label/oauth2client

"""

##-----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Note: 
# -----------------------------------------------------------------------------
"""

  - No ++ or --, use a+=1 or a-=1 
  - print ("Variable %d", %Val)
    print ("Variable %d %d", % (Val1, Val2))
  - Syntax Tip : line breaks are ignored inside pairs of [], {}, or ().
    So building multiline lists, liscomps, genexps, dictionaries and the like no need
    no need to use \ for line continuation escape
  - 
"""

'''
3 single quote string
'''


## Example location: 
# YouTube: https://www.youtube.com/watch?v=zJVCKvXtHtE
# Code: http://goo.gl/dxuuB

## install Google API
#  pip install --upgrade google-api-python-client (preferred)
# easy_install --upgrade google-api-python-client

## create credentials
# code.google.com/apis/console
# project ID: hazel-mote-212820
# Client ID:  816468430834-jcrdb3fm95sif3d8iek346c1958p2q5n.apps.googleusercontent.com
# client_secret: -Fv-TWGZ8GsEDeoLvjPlAXRM


## Code: http://goo.gl/dxuuB
#!/usr/bin/python

import httplib2
import pprint

from apiclient.discovery import build
from apiclient.http import MediaFileUpload
from oauth2client.client import OAuth2WebServerFlow


# Copy your credentials from the APIs Console
#CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_ID = '816468430834-jcrdb3fm95sif3d8iek346c1958p2q5n.apps.googleusercontent.com'
#CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
CLIENT_SECRET = '-Fv-TWGZ8GsEDeoLvjPlAXRM'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Path to the file to upload
FILENAME = 'document.txt'

# Run through the OAuth flow and retrieve credentials
##flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE) ## ValueError: The value of redirect_uri must not be None
flow = OAuth2WebServerFlow(CLIENT_ID, CLIENT_SECRET, OAUTH_SCOPE, redirect_uri="urn:ietf:wg:oauth:2.0:oob")
authorize_url = flow.step1_get_authorize_url() # need to go to this link to allow access and get verification code
print('Go to the following link in your browser: ' + authorize_url)
#code = raw_input('Enter verification code: ').strip() # raw_input has been renamed to input in Python 3
code = input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

# Create an httplib2.Http object and authorize it with our credentials
http = httplib2.Http()
http = credentials.authorize(http)

drive_service = build('drive', 'v2', http=http)

# Insert a file
media_body = MediaFileUpload(FILENAME, mimetype='text/plain', resumable=True)
body = {
 'title': 'My_upload_document',
 'description': 'A test document',
 'mimeType': 'text/plain'
}

file = drive_service.files().insert(body=body, media_body=media_body).execute()
pprint.pprint(file)


##-----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Note: 
# -----------------------------------------------------------------------------
"""
 Error:
  - ModuleNotFoundError: No module named 'oauth2client'
    pip install --upgrade oauth2client
  
  - 
  
"""

##-----------------------------------------------------------------------------
"""
Resources:

 - https://developers.google.com/drive/
 - 

"""
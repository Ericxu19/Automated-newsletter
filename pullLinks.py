from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def pullLinks():
    links = []
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('tokenG.pickle'):
        with open('tokenG.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentialsGmail.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('tokenG.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)
    intro = ''
    # Call the Gmail API
    messageList = service.users().messages().list(userId='me').execute()
    messageList = messageList['messages']
    for message in messageList:
        m = service.users().messages().get(userId = 'me', id = message["id"],format="metadata").execute()
        for dic in m['payload']['headers']:
            if dic['name'] == 'Subject':
                # 
                if dic['value'] == "link"+ "8":
                    links.append(m['snippet'])
                if dic['value'] == "intro"+ "8":
                    intro= ""

                    
    return [intro, links]

# pip install --upgrade google-api-python-client
# pip install --upgrade google-auth-oauthlib google-auth-httplib2

api_key ='AIzaSyA_3DvwpZGL8vzNvuVdbpruzgtRRKgoWBo'
chanel_id = 'UCJQJAI7IjbLcpsjWdSzYz0Q'  #ThuvuData Analyst
api_service_name = 'youtube'
api_service_version ='v3'



from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import json
import configparser


config= configparser.ConfigParser()
config.read('config.ini')
api_key = config.get('GOOGLE_API','api_key')
print(api_key)
# # Set the scopes for the YouTube Data API
# SCOPES = ["https://www.googleapis.com/auth/youtube.readonly"]

# # Create an InstalledAppFlow object
# flow = InstalledAppFlow.from_client_secrets_file(
#     "client_secret.json", scopes=SCOPES
# )


# # Run the authorization flow
# credentials = flow.run_local_server()

# Create a YouTube Data API service instance
# youtube = build("youtube", "v3", credentials=credentials)
youtube = build("youtube", "v3", developerKey=api_key)


# Use the service instance to make API requests
def get_chanel_statistic(youtube,chanel_id):
    request = youtube.channels().list(
        part="snippet,contentDetails,statistics",
        id = chanel_id 
        )
    response = request.execute()

    return response

data = get_chanel_statistic(youtube,chanel_id)
chanel_data = data['items'][0]
with open("chanel_statistic.json","w+") as file:
    json.dump(chanel_data ,file, indent=4)
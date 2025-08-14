import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SP_CLIENT")
client_secret = os.getenv("SP_SECRET")

if client_secret and client_id:

    cred = requests.post(url="https://accounts.spotify.com/api/token", 
                     headers={"Content-Type": "application/x-www-form-urlencoded"},
                     data={'grant_type':'client_credentials'},
                     auth=(client_id, client_secret))
    
    access_token = cred.json()['access_token']
    
    print(cred.json())
    print(access_token)

    playlist_id = '37i9dQZEVXbMDoHDwVN2tF'

    response = requests.get(url=f'https://api.spotify.com/v1/playlists/{playlist_id}',
                            headers={'Authorization': f'Bearer {access_token}'}).json()
    
    
    if 'error' not in response:
        artist_names = []
        for item in response['tracks']['items']:
            for artist in item['track']['artists']:
                artist_names.append(artist['name'])

        print(artist_names)
    else:
        e = response['error']['status']
        m = response['error']['message']
        print(f'{e}: {m}')

    
else:
    print("No id or secret")
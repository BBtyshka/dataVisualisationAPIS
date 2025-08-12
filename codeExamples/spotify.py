import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'your_client_id'
client_secret = 'your_client_secret'

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlist_id = '37i9dQZF1DXcBWIGoYBM5M'  # Today's Top Hits playlist ID

results = sp.playlist_tracks(playlist_id)
for item in results['items']:
    track = item['track']
    print(f"{track['name']} by {track['artists'][0]['name']} - Popularity: {track['popularity']}")

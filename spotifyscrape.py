import requests
import pandas as pd

# Your Client ID and Client Secret
client_id = '112013e3093d468a9b35a46d6d550298'
client_secret = 'cda32ed03e604f67b6f6f4b41af68e90'

# Function to get OAuth token
def get_access_token(client_id, client_secret):
    url = 'https://accounts.spotify.com/api/token'
    payload = {'grant_type': 'client_credentials'}
    response = requests.post(url, auth=(client_id, client_secret), data=payload)
    if response.status_code == 200:
        return response.json()['access_token']
    else:
        raise Exception("Could not authenticate with Spotify")

# Function to get playlist tracks
def get_playlist_tracks(access_token, playlist_id):
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return [(item['track']['name'], item['track']['artists'][0]['name']) for item in response.json()['tracks']['items']]
    else:
        raise Exception("Could not fetch playlist tracks")

# Main process
access_token = get_access_token(client_id, client_secret)
# Assuming you have a file called 'playlists.txt' with one playlist ID per line
with open('playlists.txt', 'r') as file:
    playlist_ids = file.read().splitlines()

info = []
for i in range(0, len(playlist_ids)-1, 2):
    genre = playlist_ids[i]
    tracks = get_playlist_tracks(access_token, playlist_ids[i+1])
    for track, artist in tracks:
        info.append({"track": track, "artist": artist, "genre": genre, "lyrics": None})

pd.DataFrame(info).to_csv('songs.csv', index=False)
        


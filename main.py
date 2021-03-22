
import requests
import config
import psycopg2
import psycopg2.extras

artist = input('Enter artist name:')
params_artist = {'format':'json','callback':'callback','q_artist':artist,'page_size':10, 'apikey':config.API_KEY}

artist_url = 'https://api.musixmatch.com/ws/1.1/artist.search'
artist_response = requests.get(artist_url, params=params_artist)
artist_json = artist_response.json()
artist_dict = artist_json['message']['body']['artist_list']
# json_response = response.json()
print(artist_dict)

#TODO: Output the list of artists in web app
i = 1
artist_temp={}
print('Select artist:')
for artist in artist_dict:
    print(i, artist['artist']['artist_name'])
    artist_temp[i] = artist['artist']['artist_id']
    i+=1

#TODO: Input in web app the artist (from the list above) to run analysis on.

# artist = artist_temp[1]
# lyrics = 'this is the end'
artist = artist_temp[int(input('Enter the Artist ID:'))]
lyrics = input('Enter words in the song:')
params_tracks = {'format':'json', 'callback':'callback', 'f_artist_id':artist, 'q_lyrics':lyrics, 'quorum_factor':1, 'page_size':50, 'apikey':config.API_KEY}
track_url = 'https://api.musixmatch.com/ws/1.1/track.search'
tracks_response = requests.get(track_url, params=params_tracks)
tracks_json = tracks_response.json()
tracks_dict = tracks_json['message']['body']['track_list']

i = 1
track_temp={}
print('Select track:')
for track in tracks_dict:
    print(i, track['track']['track_id'], track['track']['track_name'])
    track_temp[i] = track['track']['track_id']
    i+=1


track = track_temp[int(input('>'))]
params_lyrics = {'format':'json', 'callback':'callback', 'track_id':track, 'apikey':config.API_KEY}
lyrics_url = 'https://api.musixmatch.com/ws/1.1/track.lyrics.get'
lyrics_response = requests.get(lyrics_url, params=params_lyrics)
lyrics_json = lyrics_response.json()
lyrics_dict = lyrics_json['message']['body']['lyrics']

print(lyrics_dict['lyrics_body'])

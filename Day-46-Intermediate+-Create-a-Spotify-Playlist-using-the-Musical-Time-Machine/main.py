from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import pprint


load_dotenv("/mnt/c/Users/VISIONESS/Projects/100DaysOfPython/keys.env")

sp_oauth = SpotifyOAuth(
        client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
        client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
        redirect_uri="http://example.com",
        scope="playlist-modify-private",
        cache_path="token.txt",
        show_dialog=True,
    )
sp = spotipy.Spotify(
    auth_manager=sp_oauth
)
user_id = sp.current_user()["id"]
print(user_id)

pp = pprint.PrettyPrinter(indent=4)


### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###
date = input("Which year do you want to travel to?"
             "Type the date in this format YYYY-MM-DD:\n")
year, month, day = date.split("-")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
content = response.text

soup = BeautifulSoup(content, "html.parser")
song_tags = soup.select("li ul li h3")

song_names = [tag.getText().strip() for tag in song_tags]
#print(song_names)


### - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ###
playlist_tracks = []
for song in song_names:
    results = sp.search(q=f"track: {song} year: {year}", type="track", limit=1)
    try:
        track_uri = results["tracks"]["items"][0]["uri"]
        playlist_tracks.append(track_uri)
    except IndexError:
        print(f"No tracks found named {song}\n")
        continue

new_playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False, description=f"{date} - Top 100 Songs of the week")
#print(new_playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=new_playlist["id"], tracks=playlist_tracks)

playlists = sp.user_playlists(user=user_id, limit=20)
#pp.pprint(playlists)
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import os

date = input("Which year do you want to travel to?\nType the date in this format YYYY-MM-DD: ")
URL = "https://www.billboard.com/charts/hot-100/"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=os.environ['Spotify_ClientID'],
        client_secret=os.environ['Spotify_ClientSecret'],
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

request_URL = URL+date
print(request_URL)
response = requests.get(request_URL)
chart_webpage = response.text
# print(chart_webpage)
soup = BeautifulSoup(chart_webpage, "html.parser")
# print(soup.prettify())
#charts > div > div.chart-list__wrapper > div > ol > li:nth-child(1) > button > span.chart-element__information > span.chart-element__information__song.text--truncate.color--primary
song_tags = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
song_title = [tag.text for tag in song_tags]
print(song_title)

song_uris = []
year = date.split("-")[0]
for song in song_title:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
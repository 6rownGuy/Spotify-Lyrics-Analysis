from spotify_credentials import *
import spotipy
from spotipy import SpotifyOAuth
import json
import requests
from bs4 import BeautifulSoup
import re


def get_song_lyrics(url):
    response = requests.request("GET", url)
    if response.ok:
        soup = BeautifulSoup(response.text, "html.parser")
        lyrics = soup.find(name="p", class_="lyrics-body").get_text()
        return lyrics

    return "Lyrics not found."


# def get_uri(spotify_object):
#     now_playing_data = spotify_object.current_user_playing_track()
#     return now_playing_data["item"]["uri"]


def get_track_details(spotify_object):
    now_playing_data = spotify_object.current_user_playing_track()
    track_name = now_playing_data["item"]["name"]
    artist_name = now_playing_data["item"]["album"]["artists"][0]["name"]
    track_uri = now_playing_data["item"]["uri"]
    return [track_name, artist_name, track_uri]


def generate_url(track_details):
    track_name_dirty = track_details[0].lower()
    artist_name_dirty = track_details[1].lower()
    punctuation = r"""!()-[]{};:'"\,<>./?@#$%^&*_~"""
    track_name = ""
    artist_name = ""

    for char in track_name_dirty:
        if char not in punctuation:
            track_name = track_name + char

    for char in artist_name_dirty:
        if char not in punctuation:
            artist_name = artist_name + char

    song_param = "-".join(track_name.split())
    artist_param = "-".join(artist_name.split())

    song_url = f"https://www.metrolyrics.com/printlyric/{song_param}-lyrics-{artist_param}.html"

    return song_url


def write_to_file(lyrics, track_details):
    f = open(f"lyrics//{track_details[0].lower()} lyrics.txt", "w+")
    f.write(lyrics)
    f.close()


def generate_object():
    scope = (
        "playlist-modify-public user-read-currently-playing user-read-playback-state"
    )
    token = SpotifyOAuth(
        client_id=client_id,
        client_secret=client_sectet,
        redirect_uri=redirect_uri,
        scope=scope,
        username=username,
    )
    spotify_object = spotipy.Spotify(auth_manager=token)

    return spotify_object


def anchor(spotify_object):

    track_details = get_track_details(spotify_object=spotify_object)
    track_lyrics_url = generate_url(track_details)
    lyrics = get_song_lyrics(track_lyrics_url)
    write_to_file(lyrics, track_details)

    return track_details

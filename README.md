# Spotify Live Song Analysis

A simple python program to display live analysis of the currently playing music on your Spotify.

## Features
- Displays track name, artist name.
- A **Vibe Check** meter that analyses the lyrics of the currently playing sing and displays its vibe, ranging from *dark* to *happy*.
- A **Groove Check** meter that displays the grooviness of the currently playing track (uses the `Spotify API`).
- A **Skip or Keep** meter that displays the probablity of the user liking the currently playing song, based on a machine learning model.
- Displays the lyrics

## Note
- The lyrics is being fetched from MetroLyrics, so it's availabilty deoends on whether it's available on their servers or not.
- Currently the ML model trains on a fixed dataset of songs, so the SKIP OR KEEP meter might not be wholly accurate.
I am planning to add the funtionality to train on user's liked songs.

## Instructions
- A spotify account.
- Go [here]('developer.spotify.com') and log in or sign up to Spotify.
- Create an app and get your client ID, client secret, your Spotify username and the redirect URL.
- Place all that data in the `credentials.py` file.

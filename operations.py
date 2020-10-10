from lyrics import generate_object, anchor
import os
from lyrics_score import sentiment_meter as meter

spotify_object = generate_object()


def print_details(track_details):
    os.system("cls" if os.name == "nt" else "clear")
    f = open(f"lyrics//{track_details[0].lower()} lyrics.txt", "r")

    print("\nTrack Name: ", track_details[0])
    print("\nArtist Name: ", track_details[1])
    print("\nVibe check: ", meter(track_details[0].lower()))

    print("\nLYRICS\n\n")
    lyrics = f.read()
    print(lyrics)


if __name__ == "__main__":
    np = ""
    ctr = 0

    while True:
        if spotify_object.current_playback == None:
            break
        if ctr == 0:
            track_details = anchor(spotify_object)
            print_details(track_details)
            ctr = ctr + 1
            continue

        if track_details[0] == anchor(spotify_object)[0]:
            continue
        else:
            track_details = anchor(spotify_object)
            print_details(track_details)

    print("The playback has stopped.")

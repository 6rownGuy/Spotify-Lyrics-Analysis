import os
import numpy.random as random
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

random.seed(101)


def process_lyrics_data(track_name):
    with open(f"lyrics//{track_name} lyrics.txt", "r") as file:
        lyrics = file.read()
        file.close()
    if lyrics.lower() == "lyrics not found":
        return ""
    lyrics = lyrics.split(sep="\n")
    lyrics = clean_lyrics(lyrics)

    return lyrics


def clean_lyrics(lyrics):

    sentences_and_words = []
    for sentence in lyrics:
        words = sentence.split()
        sentences_and_words.append(words)

    cleaned_lyrics = ""

    for s in sentences_and_words:
        words = " ".join(map(str, s))
        cleaned_lyrics = cleaned_lyrics + words + "\n"

    cleaned_lyrics = re.sub(r"[\(\[].*?[\)\]]", "", cleaned_lyrics)
    # Cleaning sentences with combined words
    for sentence in cleaned_lyrics:
        for word in sentence:
            for letter in word:
                if letter == word[0]:
                    continue
                if letter.isupper():
                    if is_abbr(word):
                        continue
                    i = word.index(letter)
                    a, b = word[:i], word[i:]
                    i = sentence.index(word)
                    sentence.insert(i, a)
                    sentence.insert(i + 1, b)
                    sentence.remove(word)

                    continue

    cleaned_lyrics = os.linesep.join([s for s in cleaned_lyrics.splitlines() if s])

    return cleaned_lyrics


def is_abbr(word):
    if word.isupper():
        return True
    return False


def calculate_score(lyrics):

    vader = SentimentIntensityAnalyzer()
    scores = []

    for sentence in lyrics.split("\n"):
        scores.append(vader.polarity_scores(sentence)["compound"])

    tot_score = 0
    for i in scores:
        tot_score += i

    return tot_score


def set_meter(score):
    multiplier = 0
    if score < 0:
        multiplier = random.randint(1, 3)
    if score > 0:
        multiplier = random.randint(4, 10)

    return " ".join(["[", "|" * multiplier, "." * (10 - multiplier), "]"])


def sentiment_meter(track_name):

    lyrics = process_lyrics_data(track_name)
    score = calculate_score(lyrics)
    meter = set_meter(score)

    return meter

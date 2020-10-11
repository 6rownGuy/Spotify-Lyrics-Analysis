from lyrics import generate_object, get_track_details
import pickle
import numpy.random as random
import pandas as pd


def meters(groove, choice):
    groove_meter = " ".join(["[", "|" * groove, "." * (10 - groove), "]"])
    choice_meter = " ".join(["[", "|" * choice, "." * (10 - choice), "]"])

    return groove_meter, choice_meter


def analyse(details, obj):

    id = details[2]

    sa = dict(obj.audio_features(id)[0])
    for i in ["type", "id", "uri", "track_href", "analysis_url"]:
        del sa[i]

    return sa


def groove_calculator(analysis):

    groove_multiplier = round(analysis["danceability"] + (analysis["tempo"] / 10) / 2)
    return groove_multiplier


def choice_calculator(analysis):

    analysis = dict_to_df(analysis)
    pkl_filename = "song_choice_pred.pkl"
    with open(pkl_filename, "rb") as file:
        predictor = pickle.load(file)
    pred_value = predictor.predict(analysis)
    choice_multiplier = 0

    if pred_value == 0:
        choice_multiplier = random.randint(1, 3)
    else:
        choice_multiplier = random.randint(5, 10)

    return choice_multiplier


def dict_to_df(my_dict):
    columns = [i for i in my_dict.keys()]
    df = pd.DataFrame(list(my_dict.values()))
    df = df.transpose()
    df.columns = columns
    df = df.sort_index(axis=1)
    return df


def return_meters(details, obj, option):
    analysis = analyse(details, obj)
    groove = groove_calculator(analysis)
    choice = choice_calculator(analysis)
    groove_meter, choice_meter = meters(groove, choice)

    if option == 1:
        return groove_meter
    else:
        return choice_meter

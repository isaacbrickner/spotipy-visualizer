import spotipy
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint
import logging
import numpy as np
import pandas as pd
import requests
import os
from dotenv import load_dotenv

load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET'),
        redirect_uri=os.getenv('REDIRECT_URI'),
        scope=os.getenv('SCOPE'),
    )
)
results = sp.current_user_saved_tracks()
top_tracks = sp.artist_top_tracks("0oSGxfWSnnOXhD2fKuz2Gy", "US")
results = sp.current_user_top_artists(time_range="short_term", limit=20)
top_artists = sp.current_user_top_artists(20, 0, "medium_term")
queue = sp.queue()
analysis = sp.audio_analysis(
    "https://open.spotify.com/track/13T8SvWHczyBPzOemKtEe7?si=21d4eefb66184d0d"
)

pp = pprint.PrettyPrinter(indent=4)


logger = logging.getLogger("examples.artist_recommendations")
logging.basicConfig(level="INFO")


def main():
    # print("Program has run. see csv files.", datetime.datetime.now())
    # get_top_tracks()
    # get_track_name()
    # pp.pprint(get_top_artists())
    # song_features()
    # get_user_info()
    # genre_seeds()
    # generate_recommendations()
    # get_playlists()
    # listening_stats()
    # average_energy()
    # average_tempo()
    avg_danceability()
    avg_tempo()
    avg_energy()
    pass

def avg_danceability():
    song_data = requests.get("http://localhost:5000/songFeatures")
    song_data = song_data.json()
    # pp.pprint(data.json())
    if not song_data:
        return None
    danceability_values = [entry['danceability'] for entry in song_data]
    average_danceability = sum(danceability_values) / len(danceability_values)
    print(f"Average Danceability: {average_danceability}")
    return average_danceability
   
def avg_tempo():
    song_data = requests.get("http://localhost:5000/songFeatures")
    song_data = song_data.json()
    # pp.pprint(data.json())
    if not song_data:
        return None
    tempo_values = [entry['tempo'] for entry in song_data]
    average_tempo = sum(tempo_values) / len(tempo_values)
    print(f"Average Tempo: {average_tempo}")
    return average_tempo

def avg_energy():
    song_data = requests.get("http://localhost:5000/songFeatures")
    song_data = song_data.json()
    # pp.pprint(data.json())
    if not song_data:
        return None
    energy_values = [entry['energy'] for entry in song_data]
    average_energy = sum(energy_values) / len(energy_values)
    print(f"Average Energy: {average_energy}")
    return average_energy


def create_data_for_song_features(tracks):
    artist_ids = []
    for i in range(len(tracks)):
        id = tracks[i]["uri"]
        artist_ids.append(id)
    return artist_ids


def get_playlists():
    results = sp.current_user_playlists(limit=20)
    playlist = []
    playlist_ids = {}
    for i, item in enumerate(results["items"]):
        playlist_ids = {
            "name": item["name"],
            "pid": item["uri"],
            "length": item["tracks"]["total"],
            "tracks_reference": item["tracks"]["href"],
        }
        playlist.append(playlist_ids)
        return playlist_ids
        # df = pd.DataFrame(playlist)
        # df.to_csv(r"Data/top_playlist_data.csv", index=False, header=True)


def genre_seeds():
    genre_data = sp.recommendation_genre_seeds()
    genres = genre_data["genres"]


def generate_recommendations():
    try:
        data = pd.read_csv("Data/top_artists_data.csv")
        top_five_artists = data["aid"].to_list()
        recommendations = sp.recommendations(
            [
                top_five_artists[0],
                top_five_artists[1],
                top_five_artists[2],
                top_five_artists[3],
                top_five_artists[4],
            ],
            limit=20,
        )
        rec_list = []
        for i, item in enumerate(recommendations["tracks"]):
            rec_Dict = {
                "aid": item["album"]["artists"][0]["uri"],
                "artist_name": item["album"]["artists"][0]["name"],
                "track_name": item["name"],
            }
            rec_list.append(rec_Dict)
            df = pd.DataFrame(rec_list)
            df.to_csv(r"Data/recommendations_data.csv", index=False, header=True)
    except:
        FileNotFoundError
        pass


def get_user_info():
    user_info = sp.me()
    user_data = {
        "name": user_info["display_name"],
        "id": user_info["id"],
        "uri": user_info["uri"],
        "followers": user_info["followers"]["total"],
    }
    df = pd.DataFrame(user_data, index=[0])
    df.to_csv(r"Data/user_data.csv", index=False, header=True)


def sp_search():
    print("hello please search for an artist")
    search_query = input()
    search_result = sp.search(search_query, 1, 0, "track")
    pp.pprint(search_result)


def get_top_tracks():
    results = sp.current_user_top_tracks(time_range="short_term", limit=20)
    top_track_array = []
    top_tracks_ids = {}
    for i, item in enumerate(results["items"]):
        top_tracks_ids = {
            "tid": item["artists"][0]["id"],
            "song_name": item["name"],
            "artist_name": item["artists"][0]["name"],
            "url": item["artists"][0]["external_urls"],
            "uri": item["uri"],
        }
        top_track_array.append(top_tracks_ids)
    # df = pd.DataFrame(top_track_array)
    # df.to_csv(r"Data/top_tracks_data.csv", index=False, header=True)
    return top_track_array


def get_top_artists():
    results = sp.current_user_top_artists(time_range="short_term", limit=20)
    artists = []
    artists_ids = {}

    for i, item in enumerate(results["items"]):
        artists_ids = {
            "name": item["name"],
            "aid": item["uri"],
            "genre": item["genres"],
            "uri": item,
        }
        artists.append(artists_ids)
    return artists


def get_track_name(ids):
    results = sp.tracks(ids)
    track_array = []
    tracks_ids = {}
    for i, item in enumerate(results["tracks"]):
        tracks_ids = {
            "song_name": item["name"],
            "artist_name": item["artists"][0]["name"],
        }
        track_array.append(tracks_ids)

    print(track_array)
    return track_array


def get_song_features(top_tracks):
    features = sp.audio_features(top_tracks)
    return features


def tracks_keys():
    print(top_tracks.keys())
    print("\n")


def get_queue():
    pp.pprint(queue)
    print("\n")


def change_volume(percent=0):
    while True:
        try:
            print("enter value to change volume")
            vol_change = int(input())
            sp.volume(vol_change)
        except ValueError:
            print("Not an integer! Please enter an integer.")
            continue


def get_danceability(features):
    for feature in range(len(features)):
        features_dict = features[feature]


def _top_artist_for_stats():
    get_top_artist = pd.read_csv("Data/top_artists_data.csv")
    top_artist = get_top_artist["name"][0]
    print(top_artist)
    return top_artist


def _top_track_for_stats():
    get_top_track = pd.read_csv("Data/top_tracks_data.csv")
    top_song = get_top_track["song_name"][0]
    top_songs_artist = get_top_track["artist_name"][0]
    top_song_string = str(top_song) + " by " + str(top_songs_artist)
    print(top_song_string)
    return str(top_song_string)


def _top_tid_for_stats():
    get_top_track = pd.read_csv("Data/top_tracks_data.csv")
    top_track_id = get_top_track["tid"][0]
    print(top_track_id)
    return top_track_id


def listening_stats():
    listening_stats = {}
    top_artist = _top_artist_for_stats()
    top_song = _top_track_for_stats()
    top_track_id = _top_tid_for_stats()
    avg_energy = average_energy()
    avg_tempo = average_tempo()
    avg_dance = average_danceability()
    listening_stats = {
        "top_artist": top_artist,
        "top_track": top_song,
        "top_tid": top_track_id,
        "average_energy": avg_energy,
        "average_tempo": avg_tempo,
        "average_danceability": avg_dance,
    }
    df = pd.DataFrame(listening_stats, index=[0])
    df.to_csv(r"Data/listening_stats.csv", index=False, header=True)


def average_danceability(song_feat):
    get_danceability = song_feat
    avg_danceability = []
    for i, item in enumerate(get_danceability["danceability"]):
        tempo_val = get_danceability["danceability"][i]
        avg_danceability.append(tempo_val)
    _avg = round(average(avg_danceability), 3)
    print("danceability avg: ", _avg)
    return _avg


def average_tempo(song_feat):
    get_tempo = song_feat
    avg_tempo = []
    for i, item in enumerate(get_tempo["tempo"]):
        tempo_val = get_tempo["tempo"][i]
        avg_tempo.append(tempo_val)
    _avg = round(average(avg_tempo), 3)
    print("tempo avg: ", _avg)
    return _avg


def average_energy(song_feat):
    get_energy = song_feat
    avg_energy = []
    for i, item in enumerate(get_energy["energy"]):
        energy_val = get_energy["energy"][i]
        avg_energy.append(energy_val)
    _avg = round(average(avg_energy), 3)
    print("energy average: ", _avg)
    return _avg


def average(lst):
    res = np.mean(lst)
    return res


if __name__ == "__main__":
    """This is executed when run from the command line"""
    main()


# def song_features(top_tracks):
#     try:
#         features = sp.audio_features(tracks=[])
#         data = top_tracks
#         uri_list = data["uri"].to_list()
#         name_list = data["song_name"].to_list()
#         features = sp.audio_features(uri_list)
#         # df = pd.DataFrame(features)
#         # df.to_csv(r"Data/song_features_data.csv", index=False, header=True)
#         return features
#     except:
#         pass

from flask import Flask, jsonify, render_template, request, url_for, redirect
from services import *
import json
import asyncio
import pprint
import os


app = Flask(__name__)

# TODO: https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# TODO: https://developer.spotify.com/documentation/web-api/reference/get-several-audio-features
# TODO: fix services for getting Spotify API data
# TODO: create database and models
# TODO: get services from spotify API to return appropriate data
# TODO: each time we query spotify ensure to add a datetime so that each entry(s) are different


@app.route("/songFeatures")
def create_data():
    artists = get_top_tracks()
    ids = create_data_for_song_features(artists)
    names = get_track_name(ids)
    features = get_song_features(ids)
    for i in range(len(features)):
        features[i].update(names[i])
    return jsonify(features)


@app.route("/topTracks")
def top_tracks():
    return jsonify(get_top_tracks())


@app.route("/getPlaylist")
def show_playlists():
    return jsonify(get_playlists())


@app.route("/topArtists")
def top_artists():
    return jsonify(get_top_artists())


if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=8801)

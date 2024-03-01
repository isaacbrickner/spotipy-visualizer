from flask import Flask, jsonify, render_template, request
from pprint import *
from flask_cors import CORS, cross_origin
from services import *
import json


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = (
    "Content-Type",
    "Access-Control-Allow-Private-Network: true",
)

# TODO: https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# TODO: https://developer.spotify.com/documentation/web-api/reference/get-several-audio-features
# TODO: fix services for getting Spotify API data
# TODO: create database and models 
# TODO: get services from spotify API to return appropriate data
# TODO: each time we query spotify ensure to add a datetime so that each entry(s) are different


@app.route("/")
def index():
    return render_template("client/index.html")


# @app.route("/songFeatures", methods=["GET"])
# def create_data():
#     return jsonify(find_song_features())


@app.route("/danceability", methods=["GET"])
def show_danceability():
    return jsonify(find_danceability())


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
    app.run(host="localhost", debug=True)

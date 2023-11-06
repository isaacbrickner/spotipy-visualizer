import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import json

# this is the front end!


def get_top_tracks():
    response = requests.get("http://localhost:5000/topTracks")
    if response.ok:
        display_json_in_frame(response.json())
    else:
        messagebox.showerror(
            "Error", f"Unable to fetch top tracks: {response.status_code}"
        )


def display_json_in_frame(json_data):
    top = tk.Toplevel()
    top.title("JSON Data")

    text_area = scrolledtext.ScrolledText(top, wrap=tk.WORD, state="normal")
    text_area.pack(fill=tk.BOTH, expand=True)

    pretty_json = json.dumps(json_data, indent=4)

    text_area.insert(tk.INSERT, pretty_json)
    text_area.config(state="disabled")


def get_top_artists():
    response = requests.get("http://localhost:5000/topArtists")
    if response.ok:
        display_json_in_frame(response.json())
    else:
        messagebox.showerror(
            "Error", f"Unable to fetch top artists: {response.status_code}"
        )


root = tk.Tk()
root.title("API Control Panel")
root.geometry("800x600")

top_tracks_button = tk.Button(root, text="Top Tracks", command=get_top_tracks)
top_artists_button = tk.Button(root, text="Top Artists", command=get_top_artists)

top_tracks_button.pack(fill=tk.X, expand=True)
top_artists_button.pack(fill=tk.X, expand=True)

root.mainloop()

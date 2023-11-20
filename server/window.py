import tkinter as tk
from tkinter import messagebox, scrolledtext
import requests
import json

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

def get_song_features():
    response = requests.get("http://localhost:5000/songFeatures")
    if response.ok:
        display_json_in_frame(response.json())
    else:
        messagebox.showerror(
            "Error", f"Unable to fetch song features: {response.status_code}"
        )

root = tk.Tk()
root.title("API Control Panel")
root.geometry("800x600")

# Create a frame at the bottom to contain the buttons
button_frame = tk.Frame(root)
button_frame.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

# Set uniform size for all buttons
button_width = 15

top_tracks_button = tk.Button(button_frame, text="Top Tracks", command=get_top_tracks, width=button_width)
top_artists_button = tk.Button(button_frame, text="Top Artists", command=get_top_artists, width=button_width)
top_song_features = tk.Button(button_frame, text="Song Features", command=get_song_features, width=button_width)

title_label = tk.Label(root, text="Spotify Top Song Features Visualizer", font=("Helvetica", 16))
title_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

# Pack buttons side by side with uniform width
top_tracks_button.pack(side=tk.LEFT, padx=5)
top_artists_button.pack(side=tk.LEFT, padx=5)
top_song_features.pack(side=tk.LEFT, padx=5)

root.mainloop()

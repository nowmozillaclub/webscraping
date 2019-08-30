# Song lyrics finder by Urmil Shroff

import bs4
import requests

song_name = input("Enter name of the song: ")
song_artist = input("Enter name of the artist: ")

print("Fetching lyrics...")

song_name = song_name.replace(" ", "-") # just to fix the link in genius's format
song_artist = song_artist.replace(" ", "-")
song_link = "https://genius.com/" + song_artist + "-" + song_name + "-lyrics" # creates url

res = requests.get(song_link)
soup = bs4.BeautifulSoup(res.text, "lxml")

lyrics = soup.select("p")[0].text # lyrics are in a para tag lol

print(lyrics)

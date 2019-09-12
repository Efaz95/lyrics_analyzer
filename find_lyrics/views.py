import requests
import json
from django.shortcuts import render
from bs4 import BeautifulSoup

# Create your views here.


def home(request):
	return render(request, 'find_lyrics/home.html')


def display_lyrics(request):

	song = request.GET['song'] 
	f_song = song.replace(" ", "")
	artist = request.GET['artist']
	f_artist = artist.replace(" ", "")

	url = f"https://www.azlyrics.com/lyrics/{f_artist}/{f_song}.html"

	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	lyrics = soup.find_all('div')[21].text
	f_lyrics = lyrics.replace('\n', '<br>')

	return render(request, 'find_lyrics/lyrics.html', {'song':song.capitalize() , 'artist':artist.capitalize() , 'lyrics':f_lyrics})






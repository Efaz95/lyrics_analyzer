import requests
import json
from bs4 import BeautifulSoup

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
# import matplotlib.pyplot as pt

stop_words=set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r'\w+')


#this function takes artist and song and returns the lyrics
def search_ly(artist, song):
	f_song = song.replace(" ", "")
	f_artist = artist.replace(" ", "")
	url = f"https://www.azlyrics.com/lyrics/{f_artist}/{f_song}.html"

	response = requests.get(url)
	soup = BeautifulSoup(response.content, "html.parser")
	lyrics = soup.find_all('div')[21].text

	return lyrics

lyrics_1 = search_ly("ariana grande", "god is a woman")
lyrics_2 = search_ly("ariana grande", "boyfriend")
lyrics_3 = search_ly("ariana grande", "into you")


#this function returns 10 most used words in a song
def word_freq(lyrics):
	filtered_sent=[]
	for w in tokenizer.tokenize(lyrics):
	    if w not in stop_words and (len(w)>1):
	        filtered_sent.append(w)

	fdist = FreqDist(filtered_sent)
	return fdist.most_common(10)

wfreq = word_freq(lyrics_1)

#this function plots a words frequency graph
def word_freq_graph(lyrics):
	filtered_sent=[]
	for w in tokenizer.tokenize(lyrics):
	    if w not in stop_words and (len(w)>1):
	        filtered_sent.append(w)

	fdist = FreqDist(filtered_sent)
	fdist.plot(30,cumulative=False)




word_freq_graph(lyrics_2)


#this function returns words that are shared between 3 songs
def shared_words(lyrics1, lyrics2, lyrics3):
	shared_words_set = set()
	list1 = tokenizer.tokenize(lyrics1)
	list2 = tokenizer.tokenize(lyrics2)
	list3 = tokenizer.tokenize(lyrics3)

	for w in list1:
		if w in list2 and w in list3 and len(w)>1:	
			shared_words_set.add(w.lower())

	return shared_words_set


#print(shared_words(lyrics_1, lyrics_2, lyrics_3))













import requests
import json
from bs4 import BeautifulSoup

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist

stop_words=set(stopwords.words("english"))
tokenizer = RegexpTokenizer(r'\w+')


class lyrics_analysis:
	def __init__(self, artist, song):
		self.artist = artist
		self.song = song
		self.lyrics = "" # We will be storing the lyrics to the song for faster access

	#this method searches the lyrics of the song
	def search_ly(self):
		f_song = self.song.replace(" ", "")
		f_artist = self.artist.replace(" ", "")
		url = f"https://www.azlyrics.com/lyrics/{f_artist}/{f_song}.html"

		response = requests.get(url)
		soup = BeautifulSoup(response.content, "html.parser")
		lyrics = soup.find_all('div')[19].text
		
		self.lyrics = lyrics  # Storing the lyrics
		return lyrics

	#this method returns 10 most common words in a song
	def word_freq(self):
		filtered=[]
		for w in tokenizer.tokenize(self.lyrics if self.lyrics != "" else self.search_ly()):
		    if w not in stop_words and (len(w)>1):
		        filtered.append(w)

		fdist = FreqDist(filtered)
		return fdist.most_common(10)


	#this method plots a words frequency graph
	def word_freq_graph(self):
		filtered=[]
		for w in tokenizer.tokenize(self.lyrics if self.lyrics != "" else self.search_ly()):
		    if w not in stop_words and (len(w)>1):
		        filtered.append(w)

		fdist = FreqDist(filtered)
		fdist.plot(30,cumulative=False)



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




lyrics1 = lyrics_analysis("cold play", "fix you")
# fix_you_ly = lyrics1.search_ly()
# lyrics1.word_freq_graph()
lyrics2 = lyrics_analysis("ariana grande", "god is a woman")
lyrics3 = lyrics_analysis("ariana grande", "boyfriend")
shared = shared_words(lyrics1.search_ly(), lyrics2.search_ly(), lyrics3.search_ly())
print(shared)


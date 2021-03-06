#this file will fetch some comments and do sentiment analysis on those
import os
import requests
import json
from bs4 import BeautifulSoup
from textblob import TextBlob

genius_api_token = os.environ['GENIUS_API']

artist = "justin beiber".strip()
song = "baby".strip()

#getting song id using the api
api_url = f"https://api.genius.com/search?q={artist}%20{song}&access_token={genius_api_token}"
api_response = requests.get(api_url)
id = api_response.json()['response']['hits'][0]['result']['id']

#getting song comments
url = f"https://genius.com/api/songs/{id}/comments?page=1&text_format=html,markdown"
response = requests.get(url)
comments = response.json()['response']['comments']

comment_list = []
#prints top 10 user comments
for i,comment in enumerate(comments,1):
	comment_list.append(comment['body']['markdown'])
	print(TextBlob(comment['body']['markdown']).sentiment.polarity, comment['body']['markdown'])
	# print(comment['body']['markdown'])
	# print(f"{i}. {comment['body']['markdown']}")

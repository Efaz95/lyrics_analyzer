import requests
import json
from bs4 import BeautifulSoup

artist = "taylor swift"
song = "love story"

api_url = f"https://api.genius.com/search?q={artist}%20{song}&access_token=auvWU1kHsvKA2i7_bxEanYUEM5qyXi-mMVvDr1UVkPon0rrw8__AsH2dXqPjFvKY"
api_response = requests.get(api_url)
id = api_response.json()['response']['hits'][0]['result']['id']


url = f"https://genius.com/api/songs/{id}/comments?page=1&text_format=html,markdown"
response = requests.get(url)
comments = response.json()['response']['comments']
for i,comment in enumerate(comments,1):
	print(f"{i}. {comment['body']['markdown']}")

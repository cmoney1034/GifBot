import requests
import json 
import random
import urllib
import webbrowser

q = "angry"

def getGif(query):
    api_key = "szq7jGYSNk7o9nHttekOuD6busT5MmKs"
    numberOfResults = 5
    
    response = requests.get("http://api.giphy.com/v1/gifs/search?q=" + query + "&api_key=" + api_key + "&limit=" + str(numberOfResults))
    
    if response.status_code != 200:
        print("Request went wrong :/")
    else: 
        data = json.loads(response.content)
        index = random.randint(0,numberOfResults - 1)
        gifLocation = data['data'][index]['embed_url']
        webbrowser.open(gifLocation)


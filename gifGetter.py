import requests
import json 
import random

#api_key = "szq7jGYSNk7o9nHttekOuD6busT5MmKs"
#query = "angry"
#numberOfResults = 5
#
#response = requests.get("http://api.giphy.com/v1/gifs/search?q=" + query + "&api_key=" + api_key + "&limit=" + str(numberOfResults))
#
#if response.status_code != 200:
#    print("Request went wrong :/")
#else: 
#    data = json.loads(response.content)
#    print(json.dumps(data, sort_keys=True, indent=4))
#    print(data['data'][1]['url'])

print(random.randint(0,numberOfResults))

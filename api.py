import http.client, urllib.request, urllib.parse, urllib.error, base64, json, operator

gifImage = "http://40.114.15.125/image.png"
gifKey = '070f887148c6400ca1bf9c7532ad1aa5'

def APIRequest(imageLocation, APIKey):
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': APIKey,
    }
    
    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'false',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion',
    })
    
    body = json.dumps({"url": imageLocation })
    print(body)
    
    try:
        conn = http.client.HTTPSConnection('eastus.api.cognitive.microsoft.com')
        conn.request("POST", "/face/v1.0/detect?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
        return data
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def parseJSON(jsonText):

    info = json.loads(jsonText)

    emotionDict = info[0]['faceAttributes']['emotion']

    return max(emotionDict, key=emotionDict.get)

#Used for debugging purposes
#APIRequest(sampleImage, sampleKey)
#print(parseJSON(APIRequest(gifImage, gifKey)))

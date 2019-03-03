import http.client, urllib.request, urllib.parse, urllib.error, base64, json, operator

sampleImage = "http://40.114.15.125/image.png"
sampleKey = '070f887148c6400ca1bf9c7532ad1aa5'

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

#sampleJSON is declared for debugging purposes
sampleJSON = '[{"faceRectangle":{"top":99,"left":140,"width":120,"height":120},"faceAttributes":{"emotion":{"anger":0.0,"contempt":0.0,"disgust":0.0,"fear":0.0,"happiness":1.0,"neutral":0.0,"sadness":0.0,"surprise":0.0}}}]'
def parseJSON(jsonText):
    data = json.loads(jsonText)

    emotionDict = data[0]['faceAttributes']['emotion']

    return max(emotionDict, key=emotionDict.get)

#Used for debugging purposes
#APIRequest(sampleImage, sampleKey)
print(parseJSON(APIRequest(sampleImage, sampleKey)))

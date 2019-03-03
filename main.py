import gifGetter
import api
import newCamTest


count = 0
while True:

    newCamTest.CamTest(count)

    ashuzeOutput = api.APIRequest("http://40.114.15.125/" + str(count) + "image.jpg", api.gifKey)
    
    emotion = api.parseJSON(ashuzeOutput)
    
    gifGetter.getGif(emotion)

    count += 1

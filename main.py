import gifGetter
import api
import newCamTest

newCamTest.CamTest()

ashuzeOutput = api.APIRequest(api.gifImage, api.gifKey)

emotion = api.parseJSON(ashuzeOutput)

gifGetter.getGif(emotion)

from cv2 import *
import os

def CamTest():
    stream=cv2.VideoCapture(1)
    while True:

        ret, frame=stream.read()
    
        cv2.imshow('video',frame)
    
        if cv2.waitKey(1) & 0xFF== ord('q'):
            if ret:    # frame captured without any errors
                imwrite("filename.jpg",frame) #save image
                destroyWindow("cam-test")
                os.system('scp ~/Projects/GifBot/filename.jpg azureuser@40.114.15.125:/var/www/html/image.png')
                break  
   
    stream.release()
    cv2.destroyAllWindows() 

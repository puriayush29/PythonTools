import requests
import numpy as np
import cv2

while True:
    images=requests.get("http://IPAddress:Port/shot.jpg") #MoM Server IP Address
    #images=requests.get("http://100.91.236.144:8080/shot.jpg") #Dad Server IP Address
    video=np.array(bytearray(images.content),dtype=np.uint8)
    render = cv2.imdecode(video,-1)
    cv2.imshow('frame',render)
    if(cv2.waitKey(1) and 0xFF==ord('q')):
        break

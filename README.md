# Face detecting video player
The goal of this application is pretty clear: we have to detect if the person in front of the cameras wears headphones and control the chosen media player depending on the presence/absence of the person and of his/her headphones.The goal, thus, can be divided in two different parts. The computer vision part dedicated to image processing and understanding, and the media player part dedicated to the control of the media player given the output of the computer vision analysis.

## Software Requirement
1.Python/n
2.Open CV
3.Tkinter
4.Casscade classifier
4.V.L.C Media player

## Installation
Our project is totally based on PYTHON interface,and you can use as little as Tkinter as you need:
1.Install V.L.C media player
2.Install PYTHON (3.11 64-bit)
3.Run the code in your system which is given below.



## Examples
We have several example of our project on these following website.
1.https://pgaleone.eu/tensorflow/opencv/playerctl/2020/03/26/facectrl-control-media-player-face
2.https://www.researchgate.net/publication/354303600_Face_and_Hand_Gesture_Recognition_System_for_Controlling_VLC_Media_Player
3.https://www.toptal.com/angular-js/angular-video-player-videogular
import cv2
import vlc
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()


file_path = filedialog.askopenfilename()
cam=cv2.VideoCapture(0)
m=vlc.MediaPlayer(rf'{file_path}')
#m=vlc.MediaPlayer(r'C:\Users\himan\OneDrive\Desktop\mini-project\New folder (2)\file.mp4')

fd=cv2.CascadeClassifier(r'C:\Users\himan\AppData\Local\Programs\Python\Python310\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')
flag=1 
while True:
    r,i=cam.read()
    j=cv2.cvtColor(i,cv2.COLOR_BGR2GRAY)
    face=fd.detectMultiScale(j,1.3,7)
    
    l=len(face)
    w=0
    for (x,y,w,h) in face:
        cv2.rectangle(i,(x,y),(x+w,y+h),(0,255,255),5)
        total=w*h
        
    if(l>0):
        
        m.play()
        flag=0
        m.audio_set_volume(100-int(total/1000))
        
    elif(flag==0):
        
        m.pause()
        flag=1
    #cv2.imshow('image',i)
    
    k=cv2.waitKey(5)
    if(k==ord('c')):
        r,back=cam.read()
        #cv2.imshow('my image',back)
    if(k==ord('x')):
        cv2.destroyAllWindows()
        break


## Support

For support, email jayneeshprajapati@gmail.com.


## License

[MIT](https://choosealicense.com/licenses/mit/)

# Import some necessary library.
import cv2 
import vlc
import tkinter as tk
from tkinter import filedialog
root = tk.Tk()
root.withdraw()


file_path = filedialog.askopenfilename()
cam=cv2.VideoCapture(0)
m=vlc.MediaPlayer(rf'{file_path}')
# When you intend to execute a specific video, you should opt for this method.
#m=vlc.MediaPlayer(r'C:\Users\himan\OneDrive\Desktop\mini-project\New folder (2)\file.mp4')

# This method involves specifying a directory location, from which you are provided with the option to select any video from the existing ones.
fd=cv2.CascadeClassifier(r'C:\Users\himan\AppData\Local\Programs\Python\Python310\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml')

# The primary execution of the program begins at this point.
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


import cv2
import numpy as np
import os 
import pytesseract

try:
    if not os.path.exists('krish'):
        os.makedirs('krish')
# if not created then raise error
except OSError:
    print('Error: Creating directory of data')

numberPlateCascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
plat_detector =  cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_russian_plate_number.xml")
video = cv2.VideoCapture('C:/Users/ELCOT/Downloads/vid.mp4')
i=0
if(video.isOpened()==False):
    print('Error Reading Video')

while True:
    ret,frame = video.read()    
    #i=0
    gray_video = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    plate = plat_detector.detectMultiScale(gray_video,scaleFactor=1.2,minNeighbors=5,minSize=(25,25))
    
    for (x,y,w,h) in plate:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
        #frame[y:y+h,x:x+w] = cv2.blur(frame[y:y+h,x:x+w],ksize=(10,10))
        cv2.putText(frame,text='License Plate',org=(x-3,y-3),fontFace=cv2.FONT_HERSHEY_COMPLEX,
                    color=(0,0,255),thickness=1,fontScale=0.6)  
        fps = video.get(cv2.CAP_PROP_FPS)
        video.set(cv2.CAP_PROP_FPS,5)  
        if i % 10==0:
            img= './krish/Frame'+str(i)+ '.jpg'
            print("creating frame",img)
        
       # text = pytesseract.image_to_string(img)
       
        cv2.imwrite(img,frame)
        i += 1 
       # print("lp",img)
        #cv2.imshow("License Plate Detection",img)
        #cv2.imshow('Video', frame)
        #cv2.imwrite('./krish/Frame'+str()+'.jpg', frame)
    #if ret == True:
        #cv2.imshow('Video', frame)
        #print("video",plate)

        #if i<=50:
            #break
        if cv2.waitKey(0) & 0xFF == ord("q"):
            break
video.release()
cv2.destroyAllWindows()    
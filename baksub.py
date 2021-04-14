import numpy as np 
import cv2 
import webbrowser
cap = cv2.VideoCapture(0)
subtractor = cv2.createBackgroundSubtractorMOG2(history=50, varThreshold=30)
h=80
w=200
k=0

added = np.zeros((h, w), np.uint8)
added2 = np.zeros((h, w), np.uint8)
added3 = np.zeros((h, w), np.uint8)
added4 = np.zeros((h, w), np.uint8)
allwhite = np.ones((h, w), np.uint8)
a=31

def getacol(img):
    avglist=[]
    for i in range(h):
        avg=sum(img[i])/len(img[i])
        avglist.append(avg)
    avg=sum(avglist)/h
    return avg


cv2.namedWindow('frame',0)
cv2.resizeWindow('frame',640,480)




while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    mask = subtractor.apply(frame)
    
    cimg1 = mask[50:50+h, 50:50+w]
    cimg2 = mask[300:300+h, 50:50+w]
    cimg3 = mask[50:50+h, 960:960+w]
    cimg4 = mask[300:300+h, 960:960+w]
    text1='happy'
    text2='sad'
    text3='exit(or press q)'
    text4='sleepy'
    cv2.putText(frame, text1, (100, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 1, cv2.LINE_AA)
    cv2.putText(frame, text2, (110, 370), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 1, cv2.LINE_AA)
    cv2.putText(frame, text3, (970, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 1, cv2.LINE_AA)
    cv2.putText(frame, text4, (1100, 370), cv2.FONT_HERSHEY_SIMPLEX, 1, (200, 200, 200), 1, cv2.LINE_AA)
    cv2.rectangle(frame, (5, 5), (285, 85), (0, 255, 0), 2)
    cv2.rectangle(frame, (5, 305), (285, 385), (0, 255, 0), 2)
    cv2.rectangle(frame, (965, 5), (1265, 85), (0, 255, 0), 2)
    cv2.rectangle(frame, (965, 305), (1265, 385), (0, 255, 0), 2)
    cv2.imshow('frame',frame)
    
    if a<=30:
            added = cv2.add(added,cimg1)
            added2 = cv2.add(added2,cimg2)
            added3 = cv2.add(added3,cimg3)
            added4 = cv2.add(added4,cimg4)
            a+=1
    else:
        smile = cv2.imread('image.jpg')
        sad = cv2.imread('sad.jpg')
        if getacol(added)>200:
            cv2.imshow('smile',smile)
            cv2.destroyWindow('sad')
        elif getacol(added2)>200 and getacol(added)<100:
            cv2.imshow('sad',sad)
            cv2.destroyWindow('smile')
        elif getacol(added3)>200:
            k=1
        elif getacol(added4)>200 and getacol(added3)<100:
            cv2.destroyWindow('sad')
            cv2.destroyWindow('smile')
            webbrowser.open_new('https://youtu.be/RsxR_k8KvUw')

            
        added.fill(0)
        added2.fill(0)
        added3.fill(0)
        added4.fill(0)
        a=0
    

    if (cv2.waitKey(1) & 0xFF == ord('q')) or k==1:
        break

cap.release()
cv2.destroyAllWindows()


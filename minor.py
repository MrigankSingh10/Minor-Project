import cv2
import numpy as np
import pyautogui

cap=cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
yellow_lower = np.array([20, 100, 100])
yellow_upper = np.array([30, 255, 255])
upper_limit=160
lower_limit=320

# left_limit=270-50
# right_limit=370+50

actions={'up':False,'down':False}

while True:
    ret,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(hsv,yellow_lower,yellow_upper)
    
    contours,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    frame = cv2.line(frame,(0,160),(640,160),(0,255,0),4)
    frame = cv2.line(frame,(0,350),(640,350),(0,255,0),4)
    cv2.putText(frame,'Up',(250, 50),font, 1,(0, 255, 255),2, cv2.LINE_4)
    cv2.putText(frame,'down',(250, 450),font, 1,(0, 255, 255),2, cv2.LINE_4)
 
    for c in contours:
        area=cv2.contourArea(c)
        if area>300:
            x,y,w,h=cv2.boundingRect(c)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            
                    
            if y<upper_limit:
                if actions.get('up')==False:
                    pyautogui.press('up')
                    actions['up']=True
                    print(actions)
            elif y>lower_limit:
                if actions.get('down')==False:
                    pyautogui.press('down')
                    actions['down']=True
                    print(actions)
            elif y>upper_limit and y<lower_limit:
                if actions.get('up') or actions.get('down'):
                    actions['up']=False
                    actions['down']=False
                    print(actions)
                
                
                
                
                
                
           
    cv2.imshow('frame',frame)
    if cv2.waitKey(10)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

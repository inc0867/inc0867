import cv2
import numpy
import mediapipe as mp
import HandM as ht
import HandTrackingModule as htm
import time
import pyautogui as oto



hcam = 1080
wcam = 1920



video = cv2.VideoCapture(0)

video.set(3,hcam)
video.set(4,wcam)
 
cTime = 0
pTime = 0

detec = htm.FindHands()



while True:
    isTrue , kare = video.read()


    cTime = time.time()



    fps = 1/(cTime - pTime)

    pTime = cTime

    cv2.putText(kare,str(int(fps)) , (35,25) , cv2.FONT_HERSHEY_COMPLEX , 1.0 , (255,255,255) , 3)

    

    kareD = detec.getPosition(kare,(6,8))

    kareC = detec.getPosition(kare,(10,12),draw=False)
    
    
    print(kareC)
    try:
        pt1 = kareD[0]
        pt2 = kareD[1]
    except:
        pass


    if detec.index_finger_up(kare) == True:
        
        try:
            pt1 = kareD[0]
            pt2 = kareD[1]

            clickler = kareC[1]
            
            if len(pt2) == 2:
                print("girdim")
                cv2.circle(kare , pt2 , 15 , (0,255,0) , cv2.FILLED)
                oto.moveTo(pt2)

            if detec.middle_finger_up(kare) == True:
                cv2.circle(kare, clickler , 15 , (255,0,0) , cv2.FILLED)
                cv2.line(kare , pt2 , clickler , (37,37,37) , 5)
                oto.click(pt2)


            if detec.middle_finger_up(kare) and detec.ring_finger_up((kare)) == True:
                cv2.circle(kare, clickler , 15 , (255,0,0) , cv2.FILLED)
                cv2.line(kare , pt2 , clickler , (37,37,37) , 5)
                oto.doubleClick(pt2)
        except:
            pass

    



    cv2.imshow('MainWindow',kare)


    




















    if cv2.waitKey(20) & 0xFF == ord('d'):
        break


video.release()


cv2.destroyAllWindows()
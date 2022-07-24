import face_recognition as inc
import cv2 as incc

#........................................................................................................................................................................................
#note : (pip install dlib , pip install face-recognition) #note2 if you can't download try these (pip install cmake , pip install wheel , pip install dlib , pip install face-recognition
#........................................................................................................................................................................................

yol = "Your video .mp4"

video = incc.VideoCapture(0)   #Web cam ---> 0 #video ----> yol
color = (0,255,0) #rgb color "green"

while True:
    oo,kare = video.read()

    lokasyon = inc.face_locations(kare)

    for index,fl in enumerate(lokasyon):
        topleftY,bottomRightX,bottomrightY,topleftX = fl 
        pt1 = (topleftX,topleftY)
        pt2 = (bottomRightX,bottomrightY)

        incc.rectangle(kare,pt1,pt2,color)
        incc.imshow("Tespit",kare)

    a = incc.waitKey(1)

    if a == 27:   #click esc for close
        break
video.release()
incc.destroyAllWindows()

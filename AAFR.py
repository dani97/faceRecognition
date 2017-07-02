import cv2
from FaceDetect import FaceDetector
from FaceRecognizer import FaceRecognizer
from DBAccess import DBAccess
from time import sleep


cap = cv2.VideoCapture(0)
dba = DBAccess()
sleep(1)
while True:
    flag = True
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faceDetector = FaceDetector()
    cv2.imshow('attendance',frame)
    status,gray = faceDetector.detect(gray)
    if status:
        fr = FaceRecognizer()
        flag,person = fr.recognize(gray)
        print "attendance : accept '%s'"%(person)
        if flag:
            s=raw_input("press y for yes n for no")
            if s=='y' or s=='n':
                if s=='y':
                    dba.update(person,1)
                    flag = False
                    break
                else:
                    break
            else:
                print "please enter the correct option"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()






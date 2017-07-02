import cv2
from DBAccess import DBAccess
from FaceDetect import FaceDetector
from time import sleep
fd = FaceDetector()

name = raw_input("Enter the name of the student")
regno = raw_input("register number of the candidate")

x = raw_input("enter anything to continue------------ 3 sec to take pictures")
dbHandle = DBAccess()
sql = "insert into student (name, id) values ('%s','%s')"%(name,regno)


dbHandle.insert(sql)

cap = cv2.VideoCapture(0)
sleep(1)
count = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        count+=1

        # Display the resulting frame
        face,gray = fd.detect(gray)
        cv2.imshow('frame', frame)
        if face:
            file = "trainImages/"+regno+"__"+str(count)+".jpg"
            cv2.imwrite(file,gray)
            if cv2.waitKey(1) & 0xFF == ord('q') or count==50:
                break

# When everything done, release the capture

cap.release()
cv2.destroyAllWindows()

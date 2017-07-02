import cv2


class FaceDetector:

    cascade = None

    def __init__(self,haar_file="haarcascade_frontalface_default.xml"):
        self.cascade = cv2.CascadeClassifier(haar_file)

    def detect(self,image):
        faces = self.cascade.detectMultiScale(image, 1.3, 5)
        for (x,y,w,h) in faces:
            #image = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
            image = image[y:y+h, x:x+w]
            return True,image
        return False,image




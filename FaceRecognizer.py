import cv2
import os
from PIL import Image
import numpy as np
import FaceDetect


class FaceRecognizer:

    recognizer = cv2.createLBPHFaceRecognizer()
    path = "trainImages"

    def __init__(self):
        images, labels = self.get_images_and_labels()
        self.recognizer.train(images, np.array(labels))

    def get_images_and_labels(self):

        image_paths = [os.path.join(self.path, f) for f in os.listdir(self.path)]
        images = []
        labels = []
        for image_path in image_paths:
            image_pil = Image.open(image_path).convert('L')
            image = np.array(image_pil, 'uint8')
            nbr = int(os.path.split(image_path)[1].split(".")[0].split("_")[0])
            images.append(image)
            labels.append(nbr)
        return images, labels

    def recognize(self,image):
        prediction, confidence = self.recognizer.predict(image)
        print confidence
        if confidence > 70:
            return True,prediction
        else:
            return False,0

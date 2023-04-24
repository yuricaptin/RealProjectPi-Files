import tensorflow as tf
import keras
import os
import matplotlib as plt
import numpy as np
import random
import RealProject
from RealProject import *
from RPTraining import *
from keras.metrics import Precision, Recall
import cv2
import app_data
from app_data import verify_image



#Verification backbone right here


os.listdir(os.path.join('app_data', 'verify_image'))
os.path.join('app_data', 'input_image', 'input_image.jpg')

for image in os.listdir(os.path.join('app_data', 'verify_image')):
    validation_img = os.path.join('app_data', 'verify_image', image )
    print(validation_img)

def verify(model, detection_threshold, verification_threshold):
    # Build results array
    results = []
    for image in os.listdir(os.path.join('app_data', 'verify_image')):
        input_img = preprocess(os.path.join('app_data', 'input_image', 'input_image.jpg'))
        validation_img = preprocess(os.path.join('app_data', 'verify_image', image))
        
        # Make Predictions 
        result = model.predict(list(np.expand_dims([input_img, validation_img], axis=1)))
        results.append(result)
    
    # Detection Threshold: Metric above which a prediciton is considered positive 
    detection = np.sum(np.array(results) > detection_threshold)
    
    # Verification Threshold: Proportion of positive predictions / total positive samples 
    verification = detection / len(os.listdir(os.path.join('app_data', 'verify_image'))) 
    verified = verification > verification_threshold
    
    return results, verified

#OPEN CV INCOMING
cap = cv2.VideoCapture(4)
while cap.isOpened():
    ret, frame = cap.read()
    frame = frame[120:120+250,200:200+250, :]
    
    cv2.imshow('Verification', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('v'):
    #This part will be modified with the xml file for the haar cascade to detect then do the siamese model.

        cv2.imwrite(os.path.join('app_data', 'input_image', 'input_image.jpg'), frame)
        # Run verification
        results, verified = verify(siamese_model, 0.5, 0.5)
        print(verified)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

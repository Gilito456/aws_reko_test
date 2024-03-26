import cv2
import boto3
import numpy as np 

image = np.zeros ((512,512,3), np.uint8)

cv2.rectangle(image, (0,0), (211, 511), (0, 255, 0), 5)

cv2.imshow('rectangle', image)
cv2.waitKey(0) & 0xFF 
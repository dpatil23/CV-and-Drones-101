import cv2
import numpy as np

def detect_color(s):
    img = cv2.imread(s)
    img1 = cv2.resize(img,(600,600))
    rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    lower_bound = np.array([150, 0, 0]) 
    upper_bound = np.array([255, 100, 100])
    mask = cv2.inRange(rgb, lower_bound, upper_bound)
    contours,_= cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    result=img1.copy()
    cv2.drawContours(result,contours,-1,(255,0,0),2)
    cv2.imshow('Original Image', img1)
    cv2.imshow('Color Detected', result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

s=input("Enter image path here:")
detect_color(s)

import cv2
import numpy as np
import math

def sobel(img):
    xKernel = np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    yKernel = np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    sobelled = np.zeros((img.shape[0]-2, img.shape[1]-2, 3), dtype="uint8")
    for y in range(1, gray.shape[0]-1):
        for x in range(1, gray.shape[1]-1):
            gx = np.sum(np.multiply(img[y-1:y+2, x-1:x+2], xKernel))
            gy = np.sum(np.multiply(img[y-1:y+2, x-1:x+2], yKernel))
            g = abs(gx) + abs(gy) #math.sqrt(gx ** 2 + gy ** 2) (Slower)
            g = g if g > 0 and g < 255 else (0 if g < 0 else 255)
            sobelled[y-1][x-2] = g
    cv2.imshow("edge detected",sobelled)
    cv2.waitKey(0)

s=input("Enter location of image here:")
img=cv2.imread(s)
cv2.imshow("Original",img)
cv2.waitKey(0)
gray=cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
sobel(gray)

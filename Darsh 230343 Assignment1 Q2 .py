import cv2 
import numpy as np 
import matplotlib.pyplot as plt

s=input("Enter path of image:")

# read image 
img = cv2.imread(s) 

img = cv2.resize(img, (256, 256), interpolation=cv2.INTER_CUBIC) 

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

laplacian = cv2.Laplacian(gray, cv2.CV_64F) 

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=7) 

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=7) 

sobel = cv2.bitwise_and(sobelx, sobely) 

# plot images 
plt.subplot(2, 2, 1) 
plt.imshow(laplacian, cmap='gray') 
plt.title('Laplacian') 

plt.subplot(2, 2, 2) 
plt.imshow(sobelx, cmap='gray') 
plt.title('SobelX') 

plt.subplot(2, 2, 3) 
plt.imshow(sobely, cmap='gray') 
plt.title('SobelY') 

plt.subplot(2, 2, 4) 
plt.imshow(sobel, cmap='gray') 
plt.title('Sobel') 

plt.show() 
sobel=cv2.normalize(sobel,None,0,200,cv2.NORM_MINMAX,cv2.CV_8UC1)
cv2.imshow('Edge detected image',sobel)
cv2.waitKey(0) 
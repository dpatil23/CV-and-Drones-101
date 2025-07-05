import cv2
import numpy as np

s=input("Enter location of image:")
img=cv2.imread(s)
cv2.imshow("Original Image",img)
blurred=cv2.GaussianBlur(img,(5,5),0)
edges=cv2.Canny(blurred,100,160)
#plt.figure(figsize=[10,10])
cv2.imshow("Canny edge detected",edges)
cv2.waitKey(0)
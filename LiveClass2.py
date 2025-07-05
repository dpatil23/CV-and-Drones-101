import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread("C:/Users/darsh/OneDrive/Desktop/tree.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Original Image",img)
cv2.waitKey(0)
#plt.imshow(img[:,:,::-1]);plt.title("Original Image");plt.axis("off");

#plt.imshow(gray,cmap='gray');plt.title("Original Image");plt.axis("off")

gray_inv=255-gray
#plt.imshow(gray_inv,cmap="gray");plt.title("Original Image");plt.axis("off");
cv2.imshow("Inverse Gray",gray_inv)
cv2.waitKey(0)

contours,hierarchy=cv2.findContours(gray_inv,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
img_copy=img.copy()
cv2.drawContours(img_copy,contours,-1,(255,0,0),2)
cv2.imshow("Original Image",img_copy)
cv2.waitKey(0)
#plt.figure(figsize=[10,10])
#plt.imshow(img_copy[:,:,::-1]);plt.title("Original Image");plt.axis("off")

_, binary=cv2.threshold(gray_inv,50,255,cv2.THRESH_BINARY)
#plt.imshow(binary,cmap="gray");plt.title("Binary Image");plt.axis("off")
cv2.imshow("Binary Image",binary)
cv2.waitKey(0)

blurred=cv2.GaussianBlur(img,(5,5),0)
edges=cv2.Canny(blurred,100,160)
#plt.figure(figsize=[10,10])
cv2.imshow("blurred",edges)
cv2.waitKey(0)

for i in contours:
    cv2.imshow("contour",contours[i])
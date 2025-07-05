import cv2
import numpy as np

lpf=np.zeros([256,256])
lpf[128,128]=1
print(lpf)

hpf=np.ones([256,256])
hpf[128,128]=0
print(hpf)

img1= cv2.imread(r'C:\Users\darsh\OneDrive\Desktop\ms-dhoni.webp')
newimg=cv2.resize(img1,[256,256])
gray1= cv2.cvtColor(newimg,cv2.COLOR_BGR2GRAY)
f1=cv2.dft(np.float32(gray1),flags=cv2.DFT_COMPLEX_OUTPUT)
fs1=np.fft.fftshift(f1)
magnitude=20*np.log(cv2.magnitude(fs1[:,:,0],fs1[:,:,1]))
magnitude=cv2.normalize(magnitude,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)
cv2.imshow('Fourier Transform of image 1',magnitude)
cv2.waitKey(0)

lpf_img=lpf*magnitude
cv2.imshow("Low pass",lpf_img)
cv2.waitKey(0)
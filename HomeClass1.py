import cv2
import numpy as np
def solve(s):
    img= cv2.imread(s)
    print(img.shape)
    img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray',img_gray)
    cv2.waitKey(0)
    f=cv2.dft(np.float32(img_gray),flags=cv2.DFT_COMPLEX_OUTPUT)
    fs=np.fft.fftshift(f)
    magnitude=20*np.log(cv2.magnitude(fs[:,:,0],fs[:,:,1]))
    magnitude=cv2.normalize(magnitude,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)
    cv2.imshow('Fourier Transform',magnitude)
    cv2.waitKey(0)

s= input("Enter the path of the image here:")
solve(s)
#   "C:\Users\darsh\OneDrive\Desktop\Dhoni-dive_165121_730x419-m.jpg"
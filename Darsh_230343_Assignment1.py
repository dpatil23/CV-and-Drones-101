import cv2
import numpy as np

lpf=np.zeros([256,256])
for i in (118,139):
    for j in (118,139):
        lpf[i,j]=1
print(lpf)

hpf=np.ones([256,256])
for i in (118,139):
    for j in (118,139):
        hpf[i,j]=0
print(hpf)

def hybrid(s1,s2):
    f1=cv2.dft(np.float32(gray1),flags=cv2.DFT_COMPLEX_OUTPUT)
    fs1=np.fft.fftshift(f1)
    magnitude=20*np.log(cv2.magnitude(fs1[:,:,0],fs1[:,:,1]))
    magnitude=cv2.normalize(magnitude,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)
    cv2.imshow('Fourier Transform of image 1',magnitude)
    cv2.waitKey(0)
    lpf1(magnitude)
    f2=cv2.dft(np.float32(gray2),flags=cv2.DFT_COMPLEX_OUTPUT)
    fs2=np.fft.fftshift(f2)
    magnitude1=20*np.log(cv2.magnitude(fs2[:,:,0],fs2[:,:,1]))
    magnitude1=cv2.normalize(magnitude1,None,0,255,cv2.NORM_MINMAX,cv2.CV_8UC1)
    cv2.imshow('Fourier Transform of image 2',magnitude1)
    cv2.waitKey(0)
    hpf1(magnitude)

    h1=magnitude*lpf
    h2=magnitude1*hpf
    cv2.imshow("low 1",h1)
    cv2.waitKey(0)
    cv2.imshow("high 2",h2)
    cv2.waitKey(0)
    hybrid=h1*h2
    cv2.imshow("Hybrid",hybrid)
    cv2.waitKey(0)

def lpf1(image):
    lpf_img=lpf*image
    cv2.imshow("Low pass of dhoni",lpf_img)
    cv2.waitKey(0)
    return lpf_img

def hpf1(image):
    hpf_img=hpf*image
    cv2.imshow("High pass of virat",hpf_img)
    cv2.waitKey(0)
    return hpf_img

s1=input("Enter location of image 1:")
s2=input("Enter location of image 2:")

img1= cv2.imread(s1)
img2= cv2.imread(s2)

newimg1= cv2.resize(img1,(256,256))
newimg2=cv2.resize(img2,(256,256))
cv2.imshow("original 1",newimg1)
cv2.waitKey(0)
cv2.imshow("Original 2",newimg2)
cv2.waitKey(0)

#cv2.imshow('Dhoni',newimg1)
#cv2.imshow('Virat',newimg2)

gray1= cv2.cvtColor(newimg1,cv2.COLOR_BGR2GRAY)
gray2= cv2.cvtColor(newimg2,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray Dhoni',gray1)
#cv2.imshow('Gray Virat',gray2)


hybrid(s1,s2)
#"C:\Users\darsh\OneDrive\Desktop\ms-dhoni.webp"
#"C:\Users\darsh\OneDrive\Desktop\virat-kohli.webp"

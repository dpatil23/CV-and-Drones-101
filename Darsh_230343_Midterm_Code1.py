from PIL import Image, ImageEnhance
import cv2
import numpy as np

def ig_filter(s):
    img=Image.open(s)
    img1 = ImageEnhance.Brightness(img)
    brightness=0.5
    enhanced1=img1.enhance(brightness)
    img2= ImageEnhance.Contrast(enhanced1)
    contrast=1.5
    enhanced2=img2.enhance(contrast)
    img3= ImageEnhance.Color(enhanced2)
    saturation=1.5
    enhanced3=img3.enhance(saturation)
    return enhanced3

s=input("Enter path of image:")
image=Image.open(s)
image.show()
output=ig_filter(s)
output.show()

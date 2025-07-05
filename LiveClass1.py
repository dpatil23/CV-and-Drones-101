import cv2

img = cv2.imread(r"C:\Users\darsh\OneDrive\Desktop\virat-kohli.webp")
print(img.shape)
blurred_image = cv2.blur(img,(1,1))

cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey()
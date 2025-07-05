import cv2
import numpy as np
import matplotlib.pyplot as plt

def hough_line(s):
    img= cv2.imread(s)
    cv2.imshow("original",img)
    cv2.waitKey(0)
    gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200, apertureSize=3)
    lines = cv2.HoughLines(edges, 1, np.pi / 180, threshold=150)
    finalimg = img.copy()
    cv2.imshow('edge detected',edges)
    cv2.waitKey(0)

    if lines is not None:
        for line in lines:
            rho, theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000 * (-b))
            y1 = int(y0 + 1000 * (a))
            x2 = int(x0 - 1000 * (-b))
            y2 = int(y0 - 1000 * (a))

            cv2.line(finalimg, (x1, y1), (x2, y2), (0, 0, 255), 2)

    plt.imshow(cv2.cvtColor(finalimg, cv2.COLOR_BGR2RGB))
    plt.show()

s = input("Enter path of image:")
hough_line(s)

import cv2
import numpy as np

def shape(s):
    img1=cv2.imread(s)
    img=cv2.resize(img1,(600,600))
    cv2.imshow("Original",img)
    cv2.waitKey(0)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(9,9),0)
    Canny=cv2.Canny(blur,50,200)
    contours, _ = cv2.findContours(Canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours based on the number of sides
    valid_contours = []
    for contour in contours:
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        num_sides = len(approx)
        if 3 <= num_sides <= 9:  # Assuming shapes have sides between 3 and 9
            valid_contours.append(contour)
        #if num_sides == 3:
        #    shape_name = 'Triangle'
        #elif num_sides == 4:
        #    shape_name = 'Rectangle' if cv2.isContourConvex(contour) else 'Quadrilateral'
        #elif num_sides == 5:
        #    shape_name = 'Pentagon'
        #elif num_sides == 6:
        #    shape_name = 'Hexagon'
        #elif num_sides == 7:
        #    shape_name = 'Heptagon'
        #elif num_sides == 8:
        #    shape_name = 'Octagon'
        #elif num_sides == 9:
        #    shape_name = 'Nonagon'
        #else:
        #    shape_name = 'Unknown'
        
        # Not getting right output for naming shapes
            
    # Draw the shape name and number of sides on the image
    #M = cv2.moments(contour)
    #if M["m00"] != 0:
    #    cX = int(M["m10"] / M["m00"])
    #    cY = int(M["m01"] / M["m00"])
    #    cv2.putText(img, f'{shape_name} ({num_sides} sides)', (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    #    cv2.circle(img, (cX, cY), 5, (0, 0, 255), -1)
    

    # Sort contours by area in descending order
    valid_contours = sorted(valid_contours, key=cv2.contourArea, reverse=True)

    # Mark the centers of the two largest contours
    for i in range(min(2, len(valid_contours))):
        M = cv2.moments(valid_contours[i])
        if M["m00"] != 0:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.putText(img, f"Largest-{i+1}", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
            cv2.circle(img, (cX, cY), 5, (255, 255, 255), -1)

    # Draw contours on the original image
    cv2.drawContours(img, valid_contours, -1, (0, 255, 0), 2)

    # Display the result
    cv2.imshow('Identified Shapes', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

s=input("Enter image path:")
shape(s)
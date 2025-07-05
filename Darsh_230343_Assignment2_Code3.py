from PIL import Image, ImageDraw, ImageFont
import math
import PIL
import numpy as np
import cv2

# Function to generate and display the Indian flag
def generate():
    # Creating a blank image with a white background
    flag = Image.new("RGB", (600, 600), "white")
    draw = ImageDraw.Draw(flag)

    # Drawing the green rectangle (bottom stripe)
    draw.rectangle([(0, 400), (600, 600)], fill="#138808")

    # Drawing the saffron rectangle (top stripe)
    draw.rectangle([(0, 0), (600, 200)], fill="#FF9933")

    # Drawing the white rectangle (middle stripe)
    draw.rectangle([(0, 200), (600, 400)], fill="white")

    # Drawing the navy blue circle (chakra)
    center = (300, 300)
    radius = 100
    draw.ellipse(
        [(center[0] - radius, center[1] - radius),
         (center[0] + radius, center[1] + radius)],
        fill="white",
        outline="#000080",
        width=2
    )

    # Drawing the spokes
    spokes = 24  # Number of spokes in the Ashoka Chakra
    spoke_width = 2  # Width of each spoke

    for i in range(spokes):
        angle = i * (360 / spokes)
        x1 = center[0] + radius  * math.cos(math.radians(angle))
        y1 = center[1] + radius  * math.sin(math.radians(angle))
        x2 = center[0] + radius  * math.cos(math.radians(angle+180))
        y2 = center[1] + radius  * math.sin(math.radians(angle+180))

        draw.line(
            [(x1, y1), (x2, y2)],
            fill="#000080",
            width=spoke_width
        )

    # Display the flag
    flag.show()
    return flag

def rotate(img, angle):
    if img is not None:
        return img.rotate(angle, resample=Image.BICUBIC, expand=True)
    else:
        return None

def rotatedFlags(img):
    global rotated_flag_0, rotated_flag_90, rotated_flag_180, rotated_flag_270
    
    # Store the original flag in the global variable
    rotated_flag_0=flag

    rotated_flag_90= rotate(flag,90)
    rotated_flag_180= rotate(flag,180)
    rotated_flag_270= rotate(flag,270)
 

# Uncomment the line below to test the function
flag= generate()
#rotatedFlags(flag)

def unskew(s):
    img=cv2.imread(s)
    midline_index=img.shape[1]//2
    vertical = [tuple(img[i, midline_index]) for i in range(img.shape[0])]
    for i in range(1,midline_index):
        color=tuple(img[i,midline_index])
        if color not in vertical and color != (0,0,255) and color !=(0,0,0):
            vertical.append(color)
    
    color_counts = {}

    # Step 4: Count occurrences of each color in the vertical array
    for color in vertical:
        count = np.count_nonzero((img == color).all(axis=1))
        color_counts[color] = count

    # Step 5: Identify the primary colors of the Indian flag
    correct_order = [color for color, count in sorted(color_counts.items(), key=lambda x: x[1], reverse=True)]
    # Step 7: Initialize output_image list
    output_image = []

    # Step 8: Perform horizontal traversal and replace colors
    for i in range(img.shape[0]):
        row = []
        for j in range(img.shape[1]):
            color = tuple(img[i, j])
            if color == (0, 0, 255) or color == (0, 0, 0):
                row.append(color)
            else:
                # Replace colors based on the correct order
                row.append(correct_order.index(color))

        output_image.append(row)

    # Convert output_image to a NumPy array
    output_image = np.array(output_image, dtype=np.uint8)

    # Display the final output image
    cv2.imshow("Corrected Image", output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
s=input("Enter path:")
unskew(s)
    
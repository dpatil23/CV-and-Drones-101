from PIL import Image, ImageDraw, ImageFont
import math

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

# Uncomment the line below to test the function
generate()

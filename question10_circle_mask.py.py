
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")

# Image size
h = img.shape[0]
w = img.shape[1]

# Center
cx = w // 2
cy = h // 2

# Radius
r = min(h, w) // 8

# Create grid
Y, X = np.ogrid[:h, :w]

# Distance equation
dist = (X - cx) ** 2 + (Y - cy) ** 2

# White filled circle
circle = dist <= r ** 2

r_outer = r + 15
r_inner = r + 5

mask_outer = dist <= r_outer ** 2
mask_inner = dist <= r_inner ** 2

ring = mask_outer & (~mask_inner)

# Draw
img[circle] = [255, 255, 255]
img[ring] = [0, 0, 255]

# Show
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("White Circle and Red Ring")
plt.axis("off")
plt.show()

# Save
cv2.imwrite("task10_output.jpg", img)


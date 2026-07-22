
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")

# Print image information
print("Shape =", img.shape)
print("Data Type =", img.dtype)
print("Dimensions =", img.ndim)
print("Total Pixels =", img.size)

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Get center pixel
y = img.shape[0] // 2
x = img.shape[1] // 2

# Scalar
print("\nScalar =", gray[y, x])
print("Scalar Shape =", np.shape(gray[y, x]))
print("Explanation: One grayscale pixel, so it is a single value.")

# Vector
print("\nVector =", img[y, x])
print("Vector Shape =", img[y, x].shape)
print("Explanation: One color pixel with B, G, R values.")

# Matrix
print("\nMatrix Shape =", gray.shape)
print("Explanation: Grayscale image has rows and columns only.")

# 3D Array
print("\n3D Array Shape =", img.shape)
print("Explanation: Color image has height, width, and 3 color channels.")
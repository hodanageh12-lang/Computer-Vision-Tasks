
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")

part = img[100:200, 100:200]

part[:] = (255, 0, 0)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Bug")
plt.axis("off")
plt.show()

img2 = cv2.imread("image.jpg")

part2 = img2[100:200, 100:200].copy()

part2[:] = (255, 0, 0)

plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
plt.title("Fix")
plt.axis("off")
plt.show()

img3 = cv2.imread("image.jpg")

print("Bug :", np.array_equal(img, img3))
print("Fix :", np.array_equal(img2, img3))

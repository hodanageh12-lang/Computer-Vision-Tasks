# pixel_ level image 

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")

print("Shape =", img.shape)
print("Data Type =", img.dtype)
print("Total Pixels =", img.size)

#center pixel
h = img.shape[0]
w = img.shape[1]

cy = h // 2
cx = w // 2

print("Center Pixel =", img[cy, cx])
print("Blue =", img[cy, cx, 0])
print("Green =", img[cy, cx, 1])
print("Red =", img[cy, cx, 2])

# 3- Draw circle
result = img.copy()

# 3- Draw circle

h = img.shape[0]
w = img.shape[1]

cx = w // 2
cy = h // 2

r = 50

for y in range(h):
    for x in range(w):

        d = (x - cx) ** 2 + (y - cy) ** 2

        if r**2 - r <= d <= r**2 + r:
            img[y, x] = (0, 0, 255)
# Split channels
B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

plt.figure(figsize=(10, 3))

plt.subplot(1, 3, 1)
plt.imshow(B, cmap="gray")
plt.title("Blue")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(G, cmap="gray")
plt.title("Green")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(R, cmap="gray")
plt.title("Red")
plt.axis("off")

plt.savefig("channels1.png")
plt.show()

# convert to float 
img_float = img.astype(np.float32)

img_float = img_float / 255

img_back = img_float * 255

img_back = img_back.astype(np.uint8)

print("Recovered Center =", img_back[cy, cx])

#Save output
cv2.imwrite("output_1.jpg", result)

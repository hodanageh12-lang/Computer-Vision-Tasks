import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")

# Convert to HSV
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

print(img.shape)

# Create Mask
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(img2, lower_blue, upper_blue)
inverse_mask = cv2.bitwise_not(mask)

# convert to lab
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

l, a, b = cv2.split(lab)

l = cv2.add(l, 50)

lab = cv2.merge((l, a, b))

result = cv2.cvtColor(lab, cv2.COLOR_LAB2BGR)


foreground = cv2.bitwise_and(result, result, mask=mask)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

background = cv2.bitwise_and(gray, gray, mask=inverse_mask)


final = cv2.add(foreground, background)

# Display images
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(mask, cmap="gray")
plt.title("Mask")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(final, cv2.COLOR_BGR2RGB))
plt.title("Final Result")
plt.axis("off")

plt.show()





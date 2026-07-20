import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")

# 1) 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 
lower_blue = (100, 100, 100)
upper_blue = (130, 255, 255)

# 
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 
result = cv2.bitwise_and(img, img, mask=mask)
# 
plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(mask, cmap="gray")
plt.title("Mask")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
plt.title("Result")
plt.axis("off")

plt.show()
import cv2
import numpy as np

# Create black image حطوه1
img = np.zeros((500, 500, 3), dtype=np.uint8)


# Draw  line خطوه  2
#

for i in range(50, 301):
    img[i, i] = (150, 150, 150)

# Draw circle

cx = 100
cy = 100
r = 50

for y in range(500):
    for x in range(500):

        d = (x - cx) ** 2 + (y - cy) ** 2

        if r**2 - r <= d <= r**2 + r:
            img[y, x] = (150, 150, 150)

# Display image
cv2.imshow("Task 2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
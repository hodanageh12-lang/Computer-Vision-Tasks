import cv2
import matplotlib.pyplot as plt

# Read image
img = cv2.imread("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")

# Convert BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Show images
plt.figure(figsize=(10,5))


plt.subplot(1,2,1)
plt.imshow(img)
plt.title("Wrong (BGR fed as RGB)")
plt.axis("off")

# Correct image
plt.subplot(1,2,2)
plt.imshow(rgb)
plt.title("Correct (converted to RGB)")
plt.axis("off")

# Save figure
plt.savefig("question5_output.png")

# Display figure
plt.show()
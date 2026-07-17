#

#task1 
# #import&load (seection 1)(A)

import cv2
import numpy as np
import matplotlib.pyplot as plt

images = [
    "/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png",
    "/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-15 06-29-29.png",
    "/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-15 06-41-34.png"
]

for image in images:

    img = cv2.imread(image)

    if img is None:
        raise FileNotFoundError(image)

    # section 2 <inspect array >

    print(img.shape)
    print(img.dtype)
    print(img.size)

    H, W = img.shape[:2]

    # section 3 : access pixel

    cx, cy = W // 2, H // 2

    print(img[cy, cx])
    print(img[cy, cx, 0])
    print(img[cy, cx, 1])
    print(img[cy, cx, 2])

    # section 4 : convert image to float32 
    img_float = img.astype(np.float32)

    print(img_float[cy, cx])

    img = img_float.astype(np.uint8)

    # display with cv2.imshow()

    cv2.imshow('window', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # split channels using slicing (c)

    B = img[:, :, 0]
    G = img[:, :, 1]
    R = img[:, :, 2]

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))

    for ax, ch, name in zip(axes, [B, G, R], ['Blue', 'Green', 'Red']):
        ax.imshow(ch, cmap='gray')
        ax.set_title(name)
        ax.axis('off')

    plt.tight_layout()

    # save figure before showing it
    plt.savefig(f"{image}_channels.png")

    plt.show() 

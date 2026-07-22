# تاسك 14
import cv2
import matplotlib.pyplot as plt

def show_all_spaces(path):

    img = cv2.imread(path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
    ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)

    h = img.shape[0]
    w = img.shape[1]

    cy = h // 2
    cx = w // 2

    print("BGR =", img[cy, cx])
    print("Gray =", gray[cy, cx])
    print("HSV =", hsv[cy, cx])
    print("LAB =", lab[cy, cx])
    print("YCrCb =", ycrcb[cy, cx])

    plt.figure(figsize=(15,4))

    plt.subplot(1,5,1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("BGR")
    plt.axis("off")

    plt.subplot(1,5,2)
    plt.imshow(gray, cmap="gray")
    plt.title("Gray")
    plt.axis("off")

    plt.subplot(1,5,3)
    plt.imshow(hsv)
    plt.title("HSV")
    plt.axis("off")

    plt.subplot(1,5,4)
    plt.imshow(lab)
    plt.title("LAB")
    plt.axis("off")

    plt.subplot(1,5,5)
    plt.imshow(ycrcb)
    plt.title("YCrCb")
    plt.axis("off")

    plt.savefig("output.png")
    plt.show()


show_all_spaces("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")
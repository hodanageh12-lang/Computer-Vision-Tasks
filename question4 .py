import cv2

def safe_load(path, flag):

    img = cv2.imread(path, flag)

    if img is None:
        raise FileNotFoundError("Image not found")

    print("Shape =", img.shape)
    print("Data Type =", img.dtype)
    print("Flag =", flag)

    return img


path = "/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png"

safe_load(path, cv2.IMREAD_COLOR)

safe_load(path, cv2.IMREAD_GRAYSCALE)

safe_load(path, cv2.IMREAD_UNCHANGED)

try:
    safe_load("image.jpg", cv2.IMREAD_COLOR)
except FileNotFoundError as e:
    print(e)
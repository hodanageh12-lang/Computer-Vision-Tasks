import cv2
import matplotlib.pyplot as plt
img = cv2.imread("/home/hoda/Pictures/Screenshots/Screenshot from 2026-07-12 16-31-35.png")
B, G , R = cv2 .split (img)
fig , axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].imshow(B, cmap='gray')
axes[0].set_title('Blue')


axes[1].imshow(G, cmap='gray')
axes[1].set_title('Green')


axes[2].imshow(R, cmap='gray')
axes[2].set_title('Red')

plt.show()
w=img .shape[1]
h=img .shape[0]
cx,cy = w//2 ,h//2
print(img[cy,cx])
print(img[cy,cx,0])
print(img[cy,cx,1])
print(img[cy,cx,2])
cv2.circle(img,(cx,cy),10,(0,255,0),-1)
cv2.imshow('window', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




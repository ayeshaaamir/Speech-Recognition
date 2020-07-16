import cv2
img=cv2.imread("C:/Users/Kiet k Maree/Pictures/Saved Pictures/OOP.jpg")
print(img)
print(type(img))

#show image
cv2.imshow('oop image',img)
cv2.waitkey(0)

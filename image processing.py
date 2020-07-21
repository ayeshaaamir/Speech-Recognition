import cv2
img=cv2.imread(C:/Users/Kiet k Maree/Downloads/images/cat)
print(type(img))
cv2.imshow('cat image',img)
cv2.waitKey(0)

# to rotate
h,w=img.shape[0:2]
rotate_matrix=cv2.getRotateMatrix2D((w/5,h/3),45,.2) #zoom in/zoom out
cv2.imshow('rotate image',rotate_matrix)
cv2.waitKey(0)

# to visualize matrix --> warpAffine
rotate_img=cv2.warpAffine(img,rotate_matrix,(w,h))
cv2.imshow('rotate image',rotate_img)
cv2.waitKey(0)

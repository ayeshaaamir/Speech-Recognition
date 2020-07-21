import cv2
img=cv2.imread(C:/Users/Kiet k Maree/Downloads/images/cat)
print(type(img))
cv2.imshow('cat image',img)
cv2.waitKey(0)

# to rotate
h,w=img.shape[0:2]
rotate_matrix=cv2.getRotateMatrix2D((w/5,h/3),45,1) #zoom in/zoom out
cv2.imshow('rotate image',rotate_matrix)
cv2.waitKey(0)

# to visualize matrix --> warpAffine
rotate_img=cv2.warpAffine(img,rotate_matrix,(w,h))
cv2.imshow('rotate image',rotate_img)
cv2.waitKey(0)

# to crop image
SR=int(h*15)
SC=int(w*15)
ER=int(h*84)
EC=int(w*84)
cropped_img=img[SR:ER,SC:EC]
cv2.imshow('crop image',cropped_img)
cv2.waitKey(0)

# resize an image
new_image=cv2.resize(img(0,0),fx=.10,fy=.20)
cv2.imshow("resize image",new_image)
cv2.waitKey(0)

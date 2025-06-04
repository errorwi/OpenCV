import cv2 as cv
import numpy as np

img=cv.imread('c:\\Users\\anush\\OneDrive\\Documents\\Codes\\OpenCV\\Photos\\car.jpeg')
cv.imshow('Image', img)
#translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions= (img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# if value of x is positive, image moves right
# if value of x is negative, image moves left
# if value of y is positive, image moves down
# if value of y is negative, image moves up

translated= translate(img, 100, -100)
cv.imshow('Translated', translated)
# rotation
def rotate(img, angle, rotPoint=None):
    (h,w)=img.shape[:2]

    if rotPoint is None:
        rotPoint=(w//2,h//2)
    rotMat=cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions=(w,h)
    return cv.warpAffine(img, rotMat, dimensions)

rotated= rotate(img, 45, (25,25 ))
# cv.imshow('rotated',rotated)

#resize
resized=cv.resize(img, (100,100), interpolation=cv.INTER_LINEAR)
cv.imshow('resized', resized)

#flipping
flipped=cv.flip(img, -1) 
 #0 for vertical flip, 1 for horizontal flip, -1 for both
cv.imshow('Flipped', flipped)

#cropping
cropped=img[200:400, 300:500]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
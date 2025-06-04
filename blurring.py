import cv2 as cv
import numpy as np

img= cv.imread('c:\\Users\\anush\\OneDrive\\Documents\\Codes\\OpenCV\\Photos\\image 0.jpeg')
cv.imshow('Image', img)

# averaging
average=cv.blur(img,(3,3))
cv.imshow('Average', average)

# gaussian
gauss=cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gauss)

# median
median=cv.medianBlur(img, 3)
cv.imshow('Median', median)

# bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)

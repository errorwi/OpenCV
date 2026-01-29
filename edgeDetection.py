import cv2 as cv
import numpy as np

img=cv.imread('Photos\\image 0.jpeg')
# cv.imshow('Image', img)

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian Edge Detection
lap=cv.Laplacian(gray, cv.CV_64F)
lap=np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel Edge Detection
sobelx=cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely=cv.Sobel(gray, cv.CV_64F, 0, 1)
combined=cv.bitwise_or(sobelx, sobely)


cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)    
cv.imshow('Combined Sobel', combined)

#canny
canny=cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)


cv.waitKey(0)

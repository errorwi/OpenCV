import cv2 as cv
import numpy as np

img= cv.imread('c:\\Users\\anush\\OneDrive\\Documents\\Codes\\OpenCV\\Photos\\image 0.jpeg')
cv.imshow('Image', img)

blank=np.zeros(img.shape[:2], dtype='uint8')

#splitting the channels
b,g,r=cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue Channel', blue)
cv.imshow('Green Channel', green)
cv.imshow('Red Channel', red)

# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged=cv.merge([b,g,r])
cv.imshow('merged',merged)

cv.waitKey(0)
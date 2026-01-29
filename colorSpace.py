import cv2 as cv
import numpy as np

img=cv.imread('Photos\\image 0.jpeg')
cv.imshow('Image', img)

#hsv -> hue saturation value
hsv=cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

#lab -> l*a*b
lab=cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('LAB', lab)

#rgb -> red green blue
rgb=cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)


cv.waitKey(0)

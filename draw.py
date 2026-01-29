import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3), dtype='uint8')
# cv.imshow('Blank', blank)
img=cv.imread('Photos\\car.jpeg')
# cv.imshow('Image', img)

blank[200:300, 300:700]=0,25,69
# cv.imshow('Green', blank)

# cv.rectangle(blank, (0,0), (250,250), (74,25,4), thickness=cv.FILLED)
# cv.imshow('Rectangle', blank)

cv.circle(blank, (250,250), 30, (69,0,0), thickness=-1)
cv.imshow('Circle', blank)

cv.putText(blank, 'Hey', (235,250), cv.FONT_HERSHEY_DUPLEX, 1.0, (255,255,255))
cv.imshow('Text', blank)

cv.waitKey(0)

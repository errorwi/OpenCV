import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img= cv.imread('c:\\Users\\anush\\OneDrive\\Documents\\Codes\\OpenCV\\Photos\\car.jpeg')
cv.imshow('Image', img)

blank=np.zeros(img.shape[:2], dtype='uint8')


gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
circle=cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask=cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Masked Image', mask)


# grayscale histogram
gray_hist=cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# color histogram
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist=cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim
plt.show()
cv.waitKey(0)
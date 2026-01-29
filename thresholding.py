import cv2 as cv

img=cv.imread('Photos\\image 0.jpeg')
cv.imshow('Image', img)

# in thresholding, the pixels in the image are either 0 or 255. We take a threshold value, say x,
# if the pixel value is greater than x, we set it to 255, else we set it to 0.

gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
threshold, thresh=cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
# thresh is the output image, threshold is the threshold value used
cv.imshow('Simple Threshold', thresh)

# inverse simple thresholding
threshold, thresh_inv=cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Inverse Simple Threshold', thresh_inv)

# adaptive thresholding
# here computer calculates the threshold value for each pixel based on the neighborhood of that pixel
adaptive_thresh=cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 9)
cv.imshow('Adaptive Threshold', adaptive_thresh)





cv.waitKey(0)

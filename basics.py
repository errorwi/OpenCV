import cv2 as cv

img=cv.imread('c:\\Users\\anush\\OneDrive\\Documents\\Codes\\OpenCV\\Photos\\car.jpeg')


cv.imshow('Image',img)

#convert image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('grayscale',gray)


#blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
#kernel size must be odd
#as kernel size increases, the image becomes more blurred
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('canny',canny)


# dilating the image
dilated= cv.dilate(canny, (7,7), iterations=3)
cv.imshow('dilated', dilated)

#eroding
erode=cv.erode(dilated, (7,7), iterations=3)
cv.imshow('eroded',erode)

#resize and crop
resized=cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized', resized)

crop=img[50:100, 200:400]
cv.imshow('Cropped', crop)
cv.waitKey(0)
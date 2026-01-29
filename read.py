import cv2 as cv
img=cv.imread('Photos\\car.jpeg')
# print(img)
# cv.imshow('Image', img)

def rescaleFrame(frame, scale=0.75):
    w=int(frame.shape[1]*scale)
    h=int(frame.shape[0]*scale)
    dim=(w,h)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)
capture=cv.VideoCapture('c:\\Users\\anush\\OneDrive\\Documents\\Codes\\OpenCV\\Videos\\vid.mp4')

while True:
    isTrue, frame=capture.read()
    frame_resized=rescaleFrame(frame, scale=0.5)
    cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()

# resized_img1=rescaleFrame(img,scale=0.5)
# resized_img2=rescaleFrame(img,scale=0.25)
# resized_img3=rescaleFrame(img,scale=0.125)
# cv.imshow('image', resized_img1)
# cv.imshow('imag', resized_img2)
# cv.imshow('ima', resized_img3)
cv.waitKey(0)

#def 


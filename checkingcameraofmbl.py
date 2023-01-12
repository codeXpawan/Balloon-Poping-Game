import cv2 as cv

video = cv.VideoCapture(1)
# address = "http://localhost:4747/video?640x480"
# video.open(address)
if video.isOpened()== False:
    print("Video is not opened")
while video.isOpened():
    ret, frame = video.read()
    if ret == True:
        cv.imshow('Frame', frame)
        if cv.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break
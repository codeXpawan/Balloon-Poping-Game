import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
top = 200
bottom = 1000
left = 50
right = 1700
def resizing_video(video, scale=0.5):
    width = int(video.shape[1] * scale)
    height = int(video.shape[0] * scale)
    return cv.resize(video, (width, height), interpolation=cv.INTER_AREA)
video = cv.VideoCapture("Balloon/Balloon.mp4")
if video.isOpened() == False:
    print("Error opening video stream or file")
    exit(0)
while video.isOpened():
    ret,frame = video.read()
    if not ret:
        print("Cannot receive frame (stream end?). Exiting ...")
        break
    # cv.imshow("Frame",frame)
    # plt.imshow(cv.cvtColor(frame,cv.COLOR_BGR2RGB))
    # plt.show()
    
    frame = frame[top:bottom,left:right]
    frame = resizing_video(frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray,(7,7),0)
    cv.imshow("Blur",blur)
    canny = cv.Canny(blur,100,150)
    contours, hierarchies  = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cv.imshow("Canny",canny)
    contours_poly = [None]*len(contours)
    perimeter = [None]*len(contours)
    boundRect = [None]*len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        boundRect[i] = cv.minAreaRect(contours_poly[i])
        perimeter[i] = cv.contourArea(contours_poly[i])
    for i in range(len(contours)):
        box = cv.boxPoints(boundRect[i])
        box = np.int0(box)
        print(perimeter[i])
        if perimeter[i]>10:
            cv.drawContours(frame,[box],0,(0,0,255),2)
        # cv.rectangle(img, (int(boundRect[i][0]), int(boundRect[i][1])),(int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), (0,255,0), 2)
        else:
            cv.drawContours(frame, [box], 0, (0,255,0), 2)
    cv.imshow("Rectangle",frame)

    # cv.imshow("Frame",frame)
    if cv.waitKey(100) == ord('q'):
        break
video.release()
cv.destroyAllWindows()
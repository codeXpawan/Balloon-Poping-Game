import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
flag = 0
top = 200
bottom = 1000
left = 100
right = 1700
def resizing_video(video, scale=0.5):
    width = int(video.shape[1] * scale)
    height = int(video.shape[0] * scale)
    return cv.resize(video, (width, height), interpolation=cv.INTER_AREA)
video = cv.VideoCapture("Balloon/New_Balloon.mp4")
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
    # print(frame.shape)
    cv.imshow("Frame",frame)
    gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    blur_frame = cv.GaussianBlur(gray_frame,(9,9),0)
    canny_frame = cv.Canny(blur_frame,50,150)
    # print(frame.shape)
    contours, hierarchies = cv.findContours(canny_frame, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    cnt = []
    area = [None]*len(contours)
    sliced = []
    sliced_gray = []
    # sliced_contours = [None]*len(contours)
    for i in range(len(contours)):
        area[i] = cv.contourArea(contours[i])
        # print(area[i])
        if area[i] > 100 and area[i]<300:
            cnt.append(contours[i])
    for i in range(len(cnt)):
        x,y,w,h = cv.boundingRect(cnt[i])
        # print(x,y,w,h)
        # cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        # cv.drawContours(sliced[i], sliced_contours, -1, (0,255,0), 3)
        if y-2 > 0 and y+h+2 < frame.shape[0] and x-2 > 0 and x+w+2 < frame.shape[1]:
            sliced.append(frame[y-1:y+h+2, x-1:x+w+2])
        # sliced.append(frame[y:y+h, x:x+w])
            sliced_gray.append(cv.cvtColor(sliced[i],cv.COLOR_BGR2GRAY))
            sliced_blur = cv.GaussianBlur(sliced_gray[i], (9,9), 0)
            sliced_canny = cv.Canny(sliced_blur, 50, 150)
            cv.imshow("Sliced{}canny".format(i), sliced_canny)
            sliced_contours,sliced_hierarchy = cv.findContours(sliced_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
            for j in range(len(sliced_contours)):
                sliced_area = cv.contourArea(sliced_contours[j])
                # print(sliced_area)
                if sliced_area > 10 and sliced_area < 70:
                    # cv.drawContours(sliced[i], sliced_contours, j, (0,255,0), 3)
                    print("hit")
                    flag = 1
                    x,y,w,h = cv.boundingRect(sliced_contours[j])
                    cv.rectangle(sliced[i],(x,y),(x+w,y+h),(0,255,0),2)
            cv.imshow("Sliced{}".format(i), sliced[i])
    # print(len(sliced_contours),i)
    # for j in range(len(sliced)):
        # circles = cv.HoughCircles(sliced_gray[j],cv.HOUGH_GRADIENT,0.5,1)
        # print(circles)
        # # print(len(sliced_contours[j]))
        # for k in range(len(sliced_contours)):
        #     sliced_area = cv.contourArea(sliced_contours[k])
        #     print(sliced_area)
            # if sliced_area > 100 and sliced_area < 300:
            #     cv.drawContours(sliced[j], sliced_contours[j], k, (0,255,0), 3)
        # if len(sliced_contours[j])>5:
        #     print("hit")
        # if circles.size > 4:
        #     print("hit", j)
        # if circles is not None:
        #     circles = np.round(circles[0, :]).astype("int")
        #     for (x, y, r) in circles:
        #         # draw the circle in the output image, then draw a rectangle
        #         # corresponding to the center of the circle
        #         print("#")
        #         cv.circle(sliced[j], (x, y), r, (0, 255, 0), 4)
        #         cv.rectangle(sliced[j], (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    if cv.waitKey(10) == ord('q'):
        break
video.release()
cv.destroyAllWindows()
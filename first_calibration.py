import cv2 as cv
import numpy as np
#defing empty corners for calibration
pt = [[124, 366], [574, 321], [555, 107], [114, 125]]
maxHeight = 400
maxWidth = 800
input_pts = np.float32([pt[0], pt[1], pt[2], pt[3]])
output_pts = np.float32([[0, maxHeight],
                                    [maxWidth, maxHeight],
                                    [maxWidth , 0],
                                    [0, 0]])
flag = 0
M = cv.getPerspectiveTransform(input_pts,output_pts)
#defing a function for mouse callback
def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        pt.append([x,y])

def starting_calibration():
    global M, maxWidth, maxHeight,input_pts, output_pts
    cam = cv.VideoCapture(0)
    result, img = cam.read()
    cv.imshow("Calibration", img)
    cv.setMouseCallback("Calibration", mouse_callback)
    while True:
        key = cv.waitKey(1) & 0xFF
        if key == ord('o'):
            print(pt)
            input_pts = np.float32([pt[0], pt[1], pt[2], pt[3]])
            output_pts = np.float32([[0, maxHeight],
                                    [maxWidth, maxHeight],
                                    [maxWidth , 0],
                                    [0, 0]])
            # Compute the perspective transform M
            M = cv.getPerspectiveTransform(input_pts,output_pts)
            out = cv.warpPerspective(img,M,(maxWidth, maxHeight),flags=cv.INTER_LINEAR)
            cv.imshow("Output", out)
            cam.release()
        elif key == ord('q'):
            break
    cv.destroyAllWindows()
def opencv():
    global flag
    # starting_calibration()
    cap = cv.VideoCapture(0)
    if cap.isOpened() == False:
        print("Error opening video stream or file")
        exit(0)
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == True:
            #wraping the frame and calibrating it
            frame = cv.warpPerspective(frame,M,(maxWidth,maxHeight),flags = cv.INTER_LINEAR)
            cv.imshow('Frame', frame)
            #finding the balloon
            gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
            blur_frame = cv.GaussianBlur(gray_frame,(9,9),0)
            canny_frame = cv.Canny(blur_frame,50,150)
            contours, hierarchies = cv.findContours(canny_frame, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
            cnt = []
            area = [None]*len(contours)
            for i in range(len(contours)):
                area[i] = cv.contourArea(contours[i])
                if area[i] > 100 and area[i]<300:
                    cnt.append(contours[i])
            #cutting the frame of balloon 
            for i in range(len(cnt)):
                x,y,w,h = cv.boundingRect(cnt[i])
                if y-2 > 0 and y+h+2 < frame.shape[0] and x-2 > 0 and x+w+2 < frame.shape[1]:
                    sliced = frame[y-1:y+h+2, x-1:x+w+2]
                    sliced_gray = cv.cvtColor(sliced,cv.COLOR_BGR2GRAY)
                    sliced_blur = cv.GaussianBlur(sliced_gray, (9,9), 0)
                    sliced_canny = cv.Canny(sliced_blur, 50, 150)
                    cv.imshow("Sliced canny", sliced_canny)
                    sliced_contours,sliced_hierarchy = cv.findContours(sliced_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
                    for j in range(len(sliced_contours)):
                        sliced_area = cv.contourArea(sliced_contours[j])
                        if sliced_area > 10 and sliced_area < 70:
                            print("hit")
                            flag = 1
                            x,y,w,h = cv.boundingRect(sliced_contours[j])
                            cv.rectangle(sliced,(x,y),(x+w,y+h),(0,255,0),2)
                    cv.imshow("Sliced", sliced)
            if cv.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    cap.release()
    cv.destroyAllWindows()

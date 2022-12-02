#importing cv2
import cv2 as cv
import numpy as np
# blue_balloon = cv.imread("Resized_Balloon/Blue_Balloon.png")

# blur = cv.GaussianBlur(blue_balloon,(5,5),0)
# canny = cv.Canny(blur,50,150)
# cv.imshow("Canny",canny)
# cv.waitKey(0)
# cv.destroyAllWindows()
def resize(image,scale=0.5):
    resized_width = int(image.shape[1] * scale)
    resized_height = int(image.shape[0] * scale)
    return cv.resize(image, (resized_width, resized_height), interpolation=cv.INTER_AREA)
video = cv.VideoCapture("Balloon/Balloon.mp4")
if video.isOpened() == False:
    print("Error opening video stream or file")
    exit(0)
while video.isOpened():
    ret,frame = video.read()
    if not ret:
        print("Cannot receive frame (stream end?). Exiting ...")
        break
    frame = resize(frame)
    # cv.imshow("Frame",frame)
    gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    canny = cv.Canny(gray,50,150)
    contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # cnt = contours[0]
    contours_poly = [None]*len(contours)
    centers = [None]*len(contours)
    radius = [None]*len(contours)
    for i,c in enumerate(contours):
        contours_poly[i] = cv.approxPolyDP(c, 3, True)
        centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])
    # print(contours)
    drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype=np.uint8)
    for i in range(len(contours)):
        cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), [0,255,0], 2)
    cv.imshow("Canny",canny)
    cv.imshow("Frame",frame)
    cv.imshow("Drawing",drawing)
    if cv.waitKey(1) == ord('q'):
        break
video.release()
cv.destroyAllWindows()
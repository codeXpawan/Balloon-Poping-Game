import cv2 as cv
import numpy as np

img = cv.imread("Resized_Balloon/AllBalloon.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(7,7),0)
cv.imshow("Blur",blur)
canny = cv.Canny(blur,100,150)
contours, hierarchies  = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.imshow("Canny",canny)
# cv.drawContours(img, contours, -1, (0,255,0), 3)
print(len(contours))
# cv.imshow("Contours",img)
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
    if perimeter[i]>900:
        cv.drawContours(img,[box],0,(0,0,255),2)
    # cv.rectangle(img, (int(boundRect[i][0]), int(boundRect[i][1])),(int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), (0,255,0), 2)
    else:
        cv.drawContours(img, [box], 0, (0,255,0), 2)
cv.imshow("Rectangle",img)
# lower_black = np.array([0,0,0])
# upper_black = np.array([0,255,255])
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# mask = cv.inRange(hsv, lower_black, upper_black)
# masked = cv.bitwise_and(img, img, mask=mask)
# cv.imshow("Masked",masked)
cv
cv.waitKey(0)
cv.destroyAllWindows()
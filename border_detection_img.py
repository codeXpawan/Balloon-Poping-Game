import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("Resized_Balloon/AllBalloon.png")
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray,(5,5),0)
cv.imshow("Blur",blur)
canny = cv.Canny(blur,100,150)
contours, hierarchies  = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.imshow("Canny",canny)
# cv.drawContours(img, contours, -1, (0,255,0), 3)
# print(len(contours))
# cv.imshow("Contours",img)
contours_poly = [None]*len(contours)
area = [None]*len(contours)
boundRect = [None]*len(contours)
text = [None]*len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv.approxPolyDP(c, 3, True)
    boundRect[i] = cv.minAreaRect(contours_poly[i])
    area[i] = cv.contourArea(contours_poly[i])
    text = cv.putText(img, str(area[i]), (int(boundRect[i][0][0]), int(boundRect[i][0][1])), cv.FONT_HERSHEY_SIMPLEX, 0.5, (45, 255, 166), 1)
for i in range(len(contours)):
    box = cv.boxPoints(boundRect[i])
    box = np.int0(box)
    print(area[i])
    if area[i]>1000:
        cv.drawContours(img,[box],0,(0,0,255),2)
        # cv.putText(img,str(area[i]),(int(boundRect[i]),int(box[0][1]/2)),cv.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
        # print(contours_poly[i])
    # cv.rectangle(img, (int(boundRect[i][0]), int(boundRect[i][1])),(int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), (0,255,0), 2)
    else:
        cv.drawContours(img, [box], 0, (0,255,0), 2)
        # cv.putText(img,str(area[i]),(int(box[0][1]/2),int(box[0][1]/2)),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
cv.imshow("Rectangle",img)
# # black = np.where((img == [0,0,0]).all(axis = 2))
# # print(black)
# lower_black = np.array([0,0,0])
# upper_black = np.array([0,0,0])
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow("HSV",hsv)
# # plt.imshow(hsv)
# # plt.show()
# top = 142
# bottom = 159
# left = 487
# right = 499
# hsv_cut = hsv[top:bottom,left:right]
# cv.imshow("HSV",hsv_cut)
# lower_black = hsv[0][0][0] - 10, 100, 100
# upper_black = hsv[0][0][0] + 10, 255, 255
# mask = cv.inRange(hsv, np.array(lower_black), np.array(upper_black))
# masked = cv.bitwise_and(img, img, mask=mask)
# # print(mask)
# cv.imshow("Masked",masked)
cv.waitKey(0)
cv.destroyAllWindows()
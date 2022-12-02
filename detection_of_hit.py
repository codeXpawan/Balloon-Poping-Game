import cv2 as cv
import numpy as np

img = cv.imread("Balloon/AllBalloon.png")
cv.imshow("AllBalloon",img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)
canny = cv.Canny(gray,50,150)
cv.imshow("Canny",canny)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
contours_poly = [None]*len(contours)
centers = [None]*len(contours)
radius = [None]*len(contours)
for i,c in enumerate(contours):
    contours_poly[i] = cv.approxPolyDP(c, 3, True)
    centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])
drawing = np.zeros((canny.shape[0], canny.shape[1], 3), dtype=np.uint8)
for i in range(len(contours)):
    cv.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), [0,255,0], 2)
cv.imshow("Circle",drawing)
cv.waitKey(0)
cv.destroyAllWindows()
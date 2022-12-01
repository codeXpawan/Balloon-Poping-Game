#importing cv2
import cv2 as cv

blue_balloon = cv.imread("Resized_Balloon/Blue_Balloon.png")

blur = cv.GaussianBlur(blue_balloon,(5,5),0)
canny = cv.Canny(blur,50,150)
cv.imshow("Canny",canny)
cv.waitKey(0)
cv.destroyAllWindows()
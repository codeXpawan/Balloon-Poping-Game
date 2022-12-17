import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
img = cv.imread("Resized_Balloon/Blue_Balloon.png")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower_blue = hsv[100][50][0] - 10,100,100
upper_blue = hsv[100][50][0] + 10,255,255
# print(lower_blue,upper_blue)
# plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
# plt.show()
lower_blue = np.array(lower_blue)
upper_blue = np.array(upper_blue)
all_img = cv.imread("Balloon/AllBalloon.png")
hsv_all = cv.cvtColor(all_img, cv.COLOR_BGR2HSV)
mask = cv.inRange(hsv_all, lower_blue, upper_blue)
masked = cv.bitwise_and(all_img, all_img, mask=mask)
cv.imshow("Masked",masked)
cv.waitKey(0)
cv.destroyAllWindows()
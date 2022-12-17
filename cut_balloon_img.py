import cv2 as cv
import numpy as np

img = cv.imread('Resized_Balloon/mixed.png')
blur = cv.GaussianBlur(img, (9,9), 0)
cv.imshow("Blur", blur)
canny = cv.Canny(blur, 50, 150)
cv.imshow("Canny", canny)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# cv.drawContours(img, contours, -1, (0,255,0), 3)
cnt = []
area = [None]*len(contours)
sliced = []
sliced_gray = []
for i in range(len(contours)):
    area[i] = cv.contourArea(contours[i])
    # print(area[i])
    if area[i] > 200 and area[i]<400:
        cnt.append(contours[i])
for i in range(len(cnt)):
    x,y,w,h = cv.boundingRect(cnt[i])
    # print(x,y,w,h)
    # cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    sliced.append(img[y:y+h, x:x+w])
    sliced_gray.append(cv.cvtColor(sliced[i],cv.COLOR_BGR2GRAY))
    sliced_blur = cv.GaussianBlur(sliced_gray[i], (9,9), 0)
    sliced_canny = cv.Canny(sliced_blur, 50, 150)
    sliced_contours,sliced_hierarchy = cv.findContours(sliced_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(sliced[i], sliced_contours, -1, (0,255,0), 3)
    cv.imshow("Sliced{}".format(i), sliced[i])
# print(len(sliced_contours),i)
for j in range(len(sliced)):
    circles = cv.HoughCircles(sliced_gray[j],cv.HOUGH_GRADIENT,1.2,10)
    print(circles.size)
    if circles.size > 4:
        print("hit", j)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
            print("#")
            cv.circle(sliced[j], (x, y), r, (0, 255, 0), 4)
            cv.rectangle(sliced[j], (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
    # print("for sliced {}".format(i))
    # print("*")
    # cv.HoughCircles(sliced[j])
    # if len(sliced_contours[j])>=4:
    #     print("hit",i)
    #     # x,y,w,h = cv.boundingRect(sliced_contours[j])
    #     # cv.rectangle(sliced[i],(x,y),(x+w,y+h),(0,0,255),2)
    # # print(cv.contourArea(sliced_contours[j]))
    # cv.imshow("Sliced{}".format(j), sliced[j])
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()
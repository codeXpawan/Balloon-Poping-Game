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
    # cv.imshow("Sliced{}".format(i), sliced[i])
    sliced_blur = cv.GaussianBlur(sliced[i], (9,9), 0)
    sliced_canny = cv.Canny(sliced_blur, 50, 150)
    sliced_contours,sliced_hierarchy = cv.findContours(sliced_canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(sliced[i], sliced_contours, -1, (0,255,0), 3)
    for j in range(len(sliced_contours)):
        print("for sliced {}".format(i))
        if cv.contourArea(sliced_contours[j])>500:
            x,y,w,h = cv.boundingRect(sliced_contours[j])
            cv.rectangle(sliced[i],(x,y),(x+w,y+h),(0,0,255),2)
        print(cv.contourArea(sliced_contours[j]))
        cv.imshow("Sliced{}".format(i), sliced[i])
cv.imshow("Original", img)
cv.waitKey(0)
cv.destroyAllWindows()
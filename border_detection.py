#importing cv2
import cv2 as cv

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
    cv.imshow("Frame",frame)
    canny = cv.Canny(frame,50,150)
    cv.imshow("Canny",canny)
    if cv.waitKey(1) == ord('q'):
        break
video.release()
cv.destroyAllWindows()
import cv2 as cv
import matplotlib.pyplot as plt
top = 200
bottom = 1000
left = 50
right = 1700
def resizing_video(video, scale=0.5):
    width = int(video.shape[1] * scale)
    height = int(video.shape[0] * scale)
    return cv.resize(video, (width, height), interpolation=cv.INTER_AREA)
video = cv.VideoCapture("Balloon/Balloon.mp4")
if video.isOpened() == False:
    print("Error opening video stream or file")
    exit(0)
while video.isOpened():
    ret,frame = video.read()
    if not ret:
        print("Cannot receive frame (stream end?). Exiting ...")
        break
    # cv.imshow("Frame",frame)
    # plt.imshow(cv.cvtColor(frame,cv.COLOR_BGR2RGB))
    # plt.show()
    
    frame = frame[top:bottom,left:right]
    frame = resizing_video(frame)
    cv.imshow("Frame",frame)
    if cv.waitKey(100) == ord('q'):
        break
video.release()
cv.destroyAllWindows()
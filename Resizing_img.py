import os
import cv2 as cv
import shutil

def resize(image,scale=0.05):
    resized_width = int(image.shape[1] * scale)
    resized_height = int(image.shape[0] * scale)
    return cv.resize(image, (resized_width, resized_height), interpolation=cv.INTER_AREA)
#loading the image of balloon
blue_balloon = cv.imread("Balloon/Blue_Balloon.png")
red_balloon = cv.imread("Balloon/Red_Balloon.png")
green_balloon = cv.imread("Balloon/Green_Balloon.png")
red_balloon_hit = cv.imread("Balloon/Red_Balloon_hit.png")
#building the path
path = "Resized_Balloon"
if os.path.exists(path):
    shutil.rmtree(path)
os.mkdir(path)
#resizing the image of balloon and saving it
cv.imwrite("Resized_Balloon/Blue_Balloon.png", resize(blue_balloon))
cv.imwrite("Resized_Balloon/Red_Balloon.png", resize(red_balloon))
cv.imwrite("Resized_Balloon/Green_Balloon.png", resize(green_balloon))
cv.imwrite("Resized_Balloon/Red_Balloon_hit.png", resize(red_balloon_hit))
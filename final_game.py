# import cv2 as cv
# import numpy as np
import pygame
from pygame import mixer
import time
import first_calibration as fc
import random
random.seed(5)
mixer.init()
pygame.init()    #initialize pygame
start_time = time.time()
score = 0
#defining the screen width and height
Screen_Width = 1280
Screen_Height = 720
#set up the window
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
#setting the title of the window
pygame.display.set_caption("Poping Game")
#importing the font
font = pygame.font.Font('freesansbold.ttf', 32)
#loading the image of balloon
blue_balloon = pygame.image.load("Resized_Balloon/Blue_Balloon.png")
red_balloon = pygame.image.load("Resized_Balloon/Red_Balloon.png")
green_balloon = pygame.image.load("Resized_Balloon/Green_Balloon.png")
#loading the pop sound
mixer.music.load('Balloon/balloonpop.wav')
mixer.music.set_volume(0.7)
#making the list of balloon
balloons = [red_balloon,blue_balloon,green_balloon]
#run until the user asks to quit
running = True
x = random.randint(6,1050)
y = Screen_Height
balloon_to_display = random.choice(balloons)

def balloon_appear():       #defing a function for balloon to appear
    global x, y, balloon_to_display
    x = random.randint(6,1050)
    y = Screen_Height
    balloon_to_display = random.choice(balloons) #choose a balloon from different color
#starting the game
while running:
    # fc.opencv()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
    time_text = font.render('Time: ' + str(int(time.time() - start_time)), True, (0, 0, 0))
    screen.fill((255, 255, 255))  #fill the screen with white
    screen.blit(balloon_to_display,(x,y))  #draw the blue balloon
    screen.blit(score_text, (1130, 4))
    screen.blit(time_text, (10, 10))
    y -=1  #make the balloon go up and can change speed by increasing or decreasing the number
    if y <= -400:
        balloon_appear()
    if fc.flag != 0:
        score += 5
        y = -400
        mixer.music.play()
        fc.flag = 0
    pygame.display.flip()
pygame.quit()
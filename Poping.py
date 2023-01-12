#import pygame to use pygame
import pygame
#import random to use random
from pygame import mixer
import random
import time
random.seed(5)

start_time = time.time()
#import cv2 to use opencv
# import cv2 as cv
# import Resizing_video as rv
mixer.init()
mixer.music.load('Balloon/balloonpop.wav')
pygame.init()    #initialize pygame
score = 0
mixer.music.set_volume(0.7)
#defining the screen width and height
Screen_Width = 800
Screen_Height = 570
#set up the window
screen = pygame.display.set_mode((Screen_Width, Screen_Height),pygame.RESIZABLE)
#setting the title of the window
pygame.display.set_caption("Poping Game")
font = pygame.font.Font('freesansbold.ttf', 32)
#loading the image of balloon
blue_balloon = pygame.image.load("Resized_Balloon/Blue_Balloon.png")
red_balloon = pygame.image.load("Resized_Balloon/Red_Balloon.png")
green_balloon = pygame.image.load("Resized_Balloon/Green_Balloon.png")
red_balloon_hit = pygame.image.load("Resized_Balloon/Balloon_hit.png")
#making the list of balloon
balloons = [red_balloon,blue_balloon,green_balloon,red_balloon_hit]
balloon_to_display = random.choice(balloons) #choose a balloon from different color
#run until the user asks to quit
running = True
#defing the place to make the balloon appear
x = random.randint(6,700)
y = Screen_Height
# flag = rv.flag
#making delay to make the balloon go up slowly
delay = 5
while running:
    #Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    text1 = font.render('Score: ' + str(score), True, (0, 0, 0))
    text2 = font.render('Time: ' + str(int(time.time() - start_time)), True, (0, 0, 0))
    screen.fill((255, 255, 255))  #fill the screen with white
    screen.blit(balloon_to_display,(x,y))  #draw the blue balloon
    screen.blit(text1, (1130, 4))
    screen.blit(text2, (10, 10))
    y -=0.3  #make the balloon go up and can change speed by increasing or decreasing the number
    if y <= -400:
        y = Screen_Height
        score+=0.3
        # mixer.music.play()
        x = random.randint(0,Screen_Width-200)
        balloon_to_display = random.choice(balloons) #choose a balloon from different color
    pygame.display.flip()
    # if rv.flag != 0:
    #     rv.flag = 0
    #     y = -400
    # pygame.time.delay(delay)  #making delay
pygame.quit()
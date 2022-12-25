#import pygame to use pygame
import pygame
#import random to use random
import random
random.seed(5)
#import cv2 to use opencv
# import cv2 as cv
pygame.init()    #initialize pygame

#defining the screen width and height
Screen_Width = 1280
Screen_Height = 720
#set up the window
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
#setting the title of the window
pygame.display.set_caption("Poping Game")
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
x = random.randint(0,Screen_Width-200)
y = Screen_Height
#making delay to make the balloon go up slowly
delay = 5
while running:
    #Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))  #fill the screen with white
    screen.blit(balloon_to_display,(x,y))  #draw the blue balloon
    y -=0.5  #make the balloon go up and can change speed by increasing or decreasing the number
    if y == -400:
        y = Screen_Height
        x = random.randint(0,Screen_Width-200)
        balloon_to_display = random.choice(balloons) #choose a balloon from different color
    pygame.display.flip()
    # pygame.time.delay(delay)  #making delay
pygame.quit()
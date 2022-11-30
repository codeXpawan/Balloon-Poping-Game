#import pygame to use pygame
import pygame
#import cv2 to use opencv
# import cv2 as cv
pygame.init()    #initialize pygame

#defining the screen width and height
Screen_Width = 1280
Screen_Height = 620
#set up the window
screen = pygame.display.set_mode((Screen_Width, Screen_Height))
#setting the title of the window
pygame.display.set_caption("Poping Game")
#loading the image of balloon
blue_balloon = pygame.image.load("Resized_Balloon/Blue_Balloon.png")
red_balloon = pygame.image.load("Resized_Balloon/Red_Balloon.png")
green_balloon = pygame.image.load("Resized_Balloon/Green_Balloon.png")
#run until the user asks to quit
running = True
while running:
    #Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255, 255, 255))
    screen.blit(blue_balloon,(0,0))
    pygame.display.flip()
pygame.quit()
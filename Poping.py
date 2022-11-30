#import pygame to use pygame
import pygame
pygame.init()    #initialize pygame

#set up the window
screen = pygame.display.set_mode((640, 480))
#run until the user asks to quit
running = True
while running:
    #Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()
import pygame
from pygame import mixer
import time
from calibration import Calibration
import random
from multiprocessing import Process
from threading import Thread
random.seed(5)
mixer.init()
pygame.init()    #initialize pygame
start_time = time.time()
score = 0
#defining the screen width and height
Screen_Width = 800
Screen_Height = 570
#set up the window
# screen = pygame.display.set_mode((Screen_Width, Screen_Height),pygame.RESIZABLE)
#setting the title of the window
pygame.display.set_caption("Poping Game")
#importing the font
font = pygame.font.Font('freesansbold.ttf', 32)
#loading the image of balloon
blue_balloon = pygame.image.load("Resized_Balloon/Blue_Balloon.png")
red_balloon = pygame.image.load("Resized_Balloon/Red_Balloon.png")
green_balloon = pygame.image.load("Resized_Balloon/Green_Balloon.png")
#loading the pop sound
mixer.music.load('Balloon/bgm.mp3')
mixer.music.set_volume(0.7)
#making the list of balloon
balloons = [red_balloon,blue_balloon,green_balloon]
#run until the user asks to quit
running = True
life = 10
speed = 0.3
x = random.randint(6,Screen_Width-230)
y = Screen_Height
balloon_to_display = random.choice(balloons)

def balloon_appear():       #defing a function for balloon to appear
    global x, y, balloon_to_display
    x = random.randint(6,Screen_Height-230)
    y = Screen_Height
    balloon_to_display = random.choice(balloons) #choose a balloon from different color
def restart():
    global life, speed
    life = 10
    speed = 0.3
    balloon_appear()
    
#starting the game
def start(fc):
    screen = pygame.display.set_mode((Screen_Width, Screen_Height),pygame.RESIZABLE)
    global running, score, start_time, balloon_to_display, x, y, life, speed
    mixer.music.play(loops=-1)
    while running:
        # fc.opencv()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
        life_text = font.render('Life: ' + str(life), True, (0, 0, 0))
        time_text = font.render('Time: ' + str(int(time.time() - start_time)-20), True, (0, 0, 0))
        screen.fill((255, 255, 255))  #fill the screen with white
        screen.blit(balloon_to_display,(x,y))  #draw the blue balloon
        screen.blit(life_text, (Screen_Width/2-50, 4))
        screen.blit(score_text, (Screen_Width-180, 4))
        screen.blit(time_text, (10, 4))
        pygame.draw.line(screen, (0, 0, 0), (0, 31), (Screen_Width, 31), 2)
        y -=speed  #make the balloon go up and can change speed by increasing or decreasing the number
        if y <= -400:
            if time.time() - start_time > 20:
                life -= 1
                if life != 0:
                    mixer.Channel(2).play(pygame.mixer.Sound('Balloon/life.ogg'))
            balloon_appear()
        # fc.getflag()
        if fc.getflag() != 0:
            if int(time.time() - start_time) > 20:
                score += 5
                balloon_appear()
                speed += 0.003 
                mixer.Channel(1).play(pygame.mixer.Sound('Balloon/pop.wav'))
            fc.setflag()
        if life == 0:
            over_time = time.time()
            pygame.mixer.Channel(0).play(pygame.mixer.Sound('Balloon/gameover.wav'))
            while(int(time.time() - over_time) < 5):
                screen.fill((255, 255, 255))
                over_text = font.render('Game Over', True, (0, 0, 0))
                screen.blit(over_text, (Screen_Width/2-100, Screen_Height/2-50))
                score_text = font.render('Score: ' + str(score), True, (0, 0, 0))
                screen.blit(score_text, (Screen_Width/2-100, Screen_Height/2))
                time_text = font.render('Time Played: ' + str(int(over_time-20-start_time)), True, (0, 0, 0))
                screen.blit(time_text, (Screen_Width/2-100, Screen_Height/2+50))
                pygame.display.flip()
            print("Game Over")
            print("Your Score is: ", score)
            print("Your Time is: ", int(over_time - start_time)-20, "seconds")
            
            pygame.quit()
        pygame.display.flip()
    pygame.quit()
    
if __name__ == '__main__':
    fc = Calibration()
    # Process(target= fc.opencv).start()
    # Process(target=start(fc)).start()
    Thread(target= fc.opencv).start()
    Thread(target=start(fc)).start()
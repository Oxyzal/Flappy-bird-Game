import pygame 
from pygame.locals import *
from data.bird import Bird
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60 

#on set l'écran de jeu

screen_w = 850
screen_h = 940

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Steven Bird')

#variable de jeu 
ground_s = 0
scroll_speed = 4


#charger les images
background = pygame.image.load('resources/images/background.png')
ground = pygame.image.load('resources/images/ground.png')

group = pygame.sprite.Group()
player = Bird(100, int(screen_h /2))
group.add(player)

run = True
while run :
    
    clock.tick(fps)
    #on met en place le décor
    screen.blit(background,(0,0))
    
    group.draw(screen)
    player.update()
    screen.blit(ground,(ground_s,760))
    
    
    #le scroll du jeu 
    ground_s -= scroll_speed
    if abs(ground_s) > 35:
        ground_s = 0
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
    
pygame.quit()
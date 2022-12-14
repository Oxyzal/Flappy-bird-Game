import pygame 
from pygame.locals import *
from data.bird import Bird
from data.pipe import Pipe
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60 

#on set l'écran de jeu

screen_w = 850
screen_h = 900

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('Steven Bird')

#variable de jeu 
ground_s = 0
scroll_speed = 4
fly = False
game_over = False
timer_pipe = 1500
last_pipe = pygame.time.get_ticks() - timer_pipe

#charger les images
background = pygame.image.load('resources/images/background.png')
ground = pygame.image.load('resources/images/ground.png')

group = pygame.sprite.Group()
pipe_group = pygame.sprite.Group()

player = Bird(100, int(screen_h /2))
group.add(player)




run = True
while run :
    
    clock.tick(fps)
    #on met en place le décor
    screen.blit(background,(0,0))
    
    group.draw(screen)
    player.update(fly, game_over)
    pipe_group.draw(screen)
    
    screen.blit(ground,(ground_s,760))
    
    #collision
    if pygame.sprite.groupcollide(group, pipe_group, False, False) or player.rect.top < 0:
        game_over = True
        
    if player.rect.bottom >= 760:
        game_over = True
        fly = False
        
    if game_over == False and fly == True: 
        #génération de pipe
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > timer_pipe:
            random_pipe = random.randint(-150,150)
            botom_pipe = Pipe(screen_w, int(screen_h /2 ) + random_pipe, -1)
            top_pipe = Pipe(screen_w, int(screen_h /2 ) + random_pipe, 1)
            pipe_group.add(botom_pipe)
            pipe_group.add(top_pipe)
            last_pipe = time_now
        #le scroll du jeu 
        ground_s -= scroll_speed
        if abs(ground_s) > 35:
            ground_s = 0
        pipe_group.update(scroll_speed)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and fly == False and game_over == False:
            fly = True
            
    pygame.display.update()
    
pygame.quit()
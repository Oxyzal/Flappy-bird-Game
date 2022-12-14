import pygame

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./resources/images/pipe.png')
        self.rect = self.image.get_rect()
        
        pipe_gap = 80
        #position 1 pour le haut et -1 pour le bas
        if position == 1:
            self.image = pygame.transform.flip(self.image, False , True)
            self.rect.bottomleft = [x, y - int(pipe_gap)]
        if position == -1:
            self.rect.topleft = [x,y + int(pipe_gap)]
            
    def update(self, scroll_speed):
        self.rect.x -= scroll_speed
        #delete la pite
        if self.rect.right < 0 :
            self.kill()
    

import pygame
from pygame.locals import *


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, radius, pos):
        super().__init__()
        self.image = pygame.Surface([2 * radius, 2 * radius])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        




def main() :
    #init screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('First Pygame Game')

    #fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250,255,255))

    #display text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello, World!", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    #blit everything to the screen
    screen.blit(background, (0,0))
    pygame.display.flip()
    
    ball = Ball((10,10,10), 50, (100,100))
    
    balls = pygame.sprite.Group()
    balls.add(ball)

    #event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background, (0,0))
        pygame.display.flip()
        balls.draw(screen)

if __name__ == '__main__':
    main()
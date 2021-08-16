import pygame
import math
from pygame.locals import *

GRAVITY = -10
FPS = 40


class Vector():
    def __init__(self, mag, angle):
        self.mag = mag
        self.angle = angle
    
    def getXMag(self):
        return math.cos(self.angle)

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, radius, pos):
        super().__init__()
        self.image = pygame.Surface([2 * radius, 2 * radius])
        self.image.fill((255,255,255))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = pos
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.velocity = Vector(0, (0,0))


    def getNextPos(self):
        pass

    def update(self):
        pass

def main() :
    #init screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('First Pygame Game')

    #fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    #blit everything to the screen
    screen.blit(background, (0,0))
    pygame.display.flip()
    
    balls = pygame.sprite.Group()
    ball = Ball((250,250,250), 25, (100,100))
    ball2 = Ball((255, 0, 0), 40, (300, 300))
    balls.add(ball)
    balls.add(ball2)

    clock = pygame.time.Clock()

    #event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background, (0,0))
        balls.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
        

if __name__ == '__main__':
    main()
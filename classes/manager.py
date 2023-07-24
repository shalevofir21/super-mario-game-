from classes.object import Object
from constants import *
import pygame
import os
class saw(object):
    rotate = [pygame.image.load(os.path.join('images', 'enemy.png')),pygame.image.load(os.path.join('images', 'green2.png')),pygame.image.load(os.path.join('images', 'bricks.png')),pygame.image.load(os.path.join('images', '0.5green.png'))]
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rotateCount = 0
        self.vel = 1.4

    def draw(self,win):
        self.hitbox = (self.x + 10, self.y + 5, self.width - 20, self.height - 5)
        pygame.draw.rect(win, (255,0,0), self.hitbox, 2)
        if self.rotateCount >= 8:
            self.rotateCount = 0
        win.blit(pygame.transform.scale(self.rotate[self.rotateCount//2], (64,64)), (self.x,self.y))
        self.rotateCount += 1

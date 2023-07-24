from constants import *
from classes.object import Object
import pygame

class Mario(Object):
    def __init__(self, size, location, picture, height):
        Object.__init__(self, size, location, picture, height)
        self.y_axis_speed = 0
        self.isJump = False
        self.jumpCount = 10
        self.life = 3
        self.score =0
        self.super_mario = False

    def gravity(self):
        if self.location[Y_AXIS]<590:
            self.y_axis_speed -= 0.3
        if self.location[Y_AXIS]>= 590:
            self.y_axis_speed=0



    def jump(self):
        if self.y_axis_speed ==0:
            self.y_axis_speed = 9


    def move(self, side):
        if side == LEFT:
            self.location[X_AXIS] -= MARIO_SPEED
        if side == RIGHT:
            self.location[X_AXIS] += MARIO_SPEED
        if side == "y_axis":
            self.location[Y_AXIS] -= self.y_axis_speed


    def lose_life(self):
        self.life -=1

    def collision(self,direction):
        if direction == LEFT:
            self.move(RIGHT)
        if direction == RIGHT:
            self.move(LEFT)
        if direction == "y_axis":
            self.y_axis_speed == 0


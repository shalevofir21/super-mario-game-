from classes.object import Object
from constants import *
from constants import *
class Enemy(Object):
    def __init__(self, size, location, picture, height, point_value,side):
        self.point_value = point_value
        self.side = side
        Object.__init__(self, size, location, picture, height)
    def walk(self):
        pass

    def enemy_move(self, side):
        if side == LEFT:
            self.location[X_AXIS] -= ENEMY_SPEED
        if side == RIGHT:
            self.location[X_AXIS] += ENEMY_SPEED
        if side == "y_axis":
            self.location[Y_AXIS] -= self.y_axis_speed
from classes.object import Object
from constants import  *
class Mushroom(Object):
    def __init__(self, size, location, picture, height, side):
        Object.__init__(self, size, location, picture, height)
        self.side = side

    def enemy_move(self, side):
        if side == LEFT:
            self.location[X_AXIS] -= MUSHROOM_SPEED
        if side == RIGHT:
            self.location[X_AXIS] += MUSHROOM_SPEED
        if side == "y_axis":
            self.location[Y_AXIS] -= self.y_axis_speed
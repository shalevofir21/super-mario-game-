from classes.object import Object
class Coin(Object):
    def __init__(self, size, location, picture, height, point_value):
        Object.__init__(self, size, location, picture, height)
        self.point_value = point_value

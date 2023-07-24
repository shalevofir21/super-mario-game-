from classes.object import Object
import pygame
def clip(surface, x, y, x_size, y_size):  # Get a part of the image
    handle_surface = surface.copy()  # Sprite that will get process later
    clipRect = pygame.Rect(x, y, x_size, y_size)  # Part of the image
    handle_surface.set_clip(clipRect)  # Clip or you can call cropped
    image = surface.subsurface(handle_surface.get_clip())  # Get subsurface
    return image.copy()  # Return
class Block_object(Object):
    def __init__(self, size, location, picture, height, image_size):
        Object.__init__(self, size, location, picture, height)
        self.image_size = image_size

    def spawn(self, screen):

        img2 = pygame.image.load(self.picture)
        img2 = pygame.transform.scale(img2, (self.size, self.height))
        for y in range(int(self.height / self.image_size)):
            for x in range(int(self.size / self.image_size)):
                screen.blit(img2, (self.image_size * x+self.location[0], self.image_size * y+self.location[1]))

    def show_on_screen(self,screen, x):
        img2 = pygame.image.load(self.picture)
        img2 = pygame.transform.scale(img2, (self.size, self.height))
        for y in range(int(self.height / self.image_size)):
            for x in range(int(self.size / self.image_size)):
                screen.blit(img2, (self.image_size * x + self.location[0], self.image_size * y + self.location[1]))
            #if self.size % self.image_size != 0:
            #    img3 = clip(img2, 0, 0, self.size % self.image_size, self.image_size)
            #    screen.blit(img3, (self.image_size * int(self.size / self.image_size) + self.location[0],
            #                       self.image_size * y + self.location[1]))

        """
               for x in range(int(self.size / self.image_size)):
                   if self.height % self.image_size != 0:
                       img4 = clip(img2, 0, 0, self.image_size, self.height % self.image_size)
                       screen.blit(img3, (self.image_size * x+self.location[0], self.image_size * int(self.height / self.image_size)+self.location[1]))

               if self.height % self.image_size != 0 and self.size % self.image_size != 0:
                   img3 = clip(img2, 0, 0, self.size % self.image_size, self.height % self.image_size)
                   screen.blit(img3, (self.image_size * int(self.size / self.image_size)+self.location[0], self.image_size * int(self.height / self.image_size)+self.location[1]))
                   """

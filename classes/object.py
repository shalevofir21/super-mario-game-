import pygame
class Object:

    def __init__(self,size,location,picture,height):
        self.size = size
        self.location = location
        self.picture = picture
        self.height = height
        self.status = True

    def spawn(self, screen):

        width1 = 300
        height1 = 300
        img2 = pygame.image.load(self.picture)
        img2 = pygame.transform.scale(img2, (self.size, self.height))
        screen.blit(img2, (130, 350))
    def show_on_screen(self,screen, x):
        img2 = pygame.image.load(self.picture)
        img2 = pygame.transform.scale(img2, (self.size, self.height))
        screen.blit(img2, (self.location[0] + x, self.location[1]))

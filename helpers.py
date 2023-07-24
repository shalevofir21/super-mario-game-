import pygame
from classes.enemy import *
from classes.coin import *
from classes.mushroom import *

def mouse_in_button(button: object, mouse_pos: object) -> object:
    if button.x_pos + button.width > mouse_pos[0] > button.x_pos and \
            button.y_pos < mouse_pos[1] < button.y_pos + button.height:
        return True

WINDOW_WIDTH = 750
WINDOW_HEIGHT = 800
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.init()

pipe = Object(60, [400, 560], "images/green2.png", 90)
pipe.spawn(screen)

pipe2 = Object(60, [800, 530], "images/green2.png", 120)
pipe.spawn(screen)

pipe3 = Object(60, [1070, 560], "images/green2.png", 90)
pipe3.spawn(screen)

pipe4 = Object(60, [1250, 540], "images/green2.png", 110)
pipe4.spawn(screen)
# ENEMY
enemy = Enemy(90, [620, 590], "images/enemy.png", 60, 3, "left")
enemy.spawn(screen)
enemy2 = Enemy(90, [850, 590], "images/enemy.png", 60, 3, "left")
enemy2.spawn(screen)

enemy3 = Enemy(90, [1300, 590], "images/enemy.png", 60, 3, "left")
enemy3.spawn(screen)


coin = Coin(60, [700, 500], "images/coins.png", 60,5)
coin.spawn(screen)

coin2 = Coin(60, [1150, 350], "images/coins.png", 60,5)
coin2.spawn(screen)


coin3 = Coin(60, [1250, 300], "images/coins.png", 60,5)
coin3.spawn(screen)

# sky

sky = Object(60, [450, 200], "images/cloud.png", 60)
sky.spawn(screen)

sky2 = Object(60, [600, 200], "images/cloud2.png", 60)
sky2.spawn(screen)

mushroom1 = Mushroom(60, [670, 590], "images/covid.png", 60,"left")
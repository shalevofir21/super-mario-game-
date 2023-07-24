
from classes.Button import *
from classes.mario import Mario
from helpers import *


pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.set_volume(0.7)




screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
x_loc = 0
y_loc = 0
x = 0

img_path = "images/home_screen.png"
img = pygame.image.load(img_path)
img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
img_path2 = "images/game over.png"
img2 = pygame.image.load(img_path2)
img2 = pygame.transform.scale(img2, (SCREEN_WIDTH, SCREEN_HEIGHT))
img_path3 = "images/71cyNRgTcKL._SS500_.jpg"
img3 = pygame.image.load(img_path3)
img3 = pygame.transform.scale(img3, (FINISH_LINE_WIDTH, SCREEN_HEIGHT))
img_path4 = "images/theend.png"
img4 = pygame.image.load(img_path4)
img4 = pygame.transform.scale(img4, (SCREEN_WIDTH, SCREEN_HEIGHT))

cerrent_screen = "start_screen()"



mario = Mario(60, [X_POS_MARIO, Y_POS_MARIO], "images/mario.png", 60)
mario.spawn(screen)


obstacle_list = [pipe, pipe2,pipe3,pipe4]
enemy_list= [enemy,enemy2,enemy3]
coin_list = [coin,coin2,coin3]
def check_left_obstacle(creature, x):
    if creature.location[X_AXIS] <= -x:
        return False
    for obstacle in obstacle_list:
        if obstacle.size + MARIO_SPEED > creature.location[X_AXIS] - obstacle.location[X_AXIS] > obstacle.size - MARIO_SPEED \
                and creature.location[Y_AXIS] <= obstacle.location[Y_AXIS] + obstacle.height \
                and creature.location[Y_AXIS] + creature.height >= obstacle.location[Y_AXIS]:
            return False
    return True



def check_right_obstacle(creature):
    if creature.location[X_AXIS] + creature.size >= TOTAL_WIDTH:
        return False
    for obstacle in obstacle_list:
        if creature.size + MARIO_SPEED > obstacle.location[X_AXIS] - creature.location[X_AXIS] > creature.size - MARIO_SPEED \
                and creature.location[Y_AXIS] <= obstacle.location[Y_AXIS] + obstacle.height \
                and creature.location[Y_AXIS] + creature.height >= obstacle.location[Y_AXIS]:
            return False
    return True


def check_y_axis_obstacle(creature):
    for obstacle in obstacle_list:
        if obstacle.location[Y_AXIS] - creature.location[Y_AXIS] <= creature.height \
                and creature.location[Y_AXIS] - obstacle.location[Y_AXIS] <= obstacle.height \
                and creature.location[X_AXIS] <= obstacle.location[X_AXIS] + obstacle.size - MARIO_SPEED \
                and creature.location[X_AXIS] + creature.size >= obstacle.location[X_AXIS] + MARIO_SPEED:
            creature.y_axis_speed = 0
def move_enemy_main(x):
    for enemy in enemy_list:
        enemy.enemy_move(enemy.side)
        if not check_left_obstacle(enemy,x):
            enemy.side = RIGHT
        if not check_right_obstacle(enemy):
            enemy.side = LEFT


def check_Collision_Meeting(x):
    mario_rect = pygame.draw.rect(screen,BLUE,pygame.Rect(mario.location[X_AXIS]+x, mario.location[Y_AXIS], mario.size, mario.height))

    for enemy in enemy_list:
        enemy_rect=pygame.draw.rect(screen, BLUE, pygame.Rect(enemy.location[X_AXIS] + x, enemy.location[Y_AXIS], enemy.height, enemy.size))
        if mario_rect.colliderect(enemy_rect) and enemy.status:
            if mario.location[Y_AXIS] + mario.height + mario.y_axis_speed <= enemy.location[Y_AXIS] and mario.super_mario:
                enemy.status = False
                mario.score += enemy.point_value
                pygame.mixer.music.load("sounds/8d82b5_Super_Mario_Bros_Kick_Sound_Effect.mp3")
                pygame.mixer.music.play()

            else:
                mario.lose_life()
                mario.spawn(screen)
                mario.super_mario = False
                mushroom1.status = True
                mario.picture = "images/mario.png"
                mario.location = [X_POS_MARIO, Y_POS_MARIO]
                pygame.mixer.music.load("sounds/8d82b5_SM64_Mario_Takes_Damage_Sound_Effect.mp3")
                pygame.mixer.music.play()
                return True
    for coin in coin_list:
        enemy_rect=pygame.draw.rect(screen, BLUE, pygame.Rect(coin.location[X_AXIS] + x, coin.location[Y_AXIS], coin.height, coin.size))
        if mario_rect.colliderect(enemy_rect) and coin.status:
            pygame.mixer.music.load("sounds/Super_Mario_Bros_Coin_Sound_Effect.mp3")
            pygame.mixer.music.play()
            if mario.super_mario:
                mario.score += coin.point_value * 2
            else:
                mario.score += coin.point_value
            coin.status = False
    mushroom_rect=pygame.draw.rect(screen, BLUE, pygame.Rect(mushroom1.location[X_AXIS] + x, mushroom1.location[Y_AXIS], mushroom1.height, mushroom1.size))
    if mario_rect.colliderect(mushroom_rect) and mushroom1.status:
        pygame.mixer.music.load("sounds/8d82b5_Super_Mario_Bros_Power_Up_Sound_Effect.mp3")
        pygame.mixer.music.play()
        mario.super_mario = True
        mushroom1.status = False
        mario.picture = "images/super_duper_mario.png"

    return False




def display_screen(x):
    if cerrent_screen == "start_screen()":
        screen.blit(img, (x_loc, y_loc))
    elif cerrent_screen == "game_screen()":
        pygame.draw.rect(screen, BLUE, pygame.Rect(0, 0, 750, 800))
        pygame.draw.rect(screen, BROWN, pygame.Rect(0, 650, 750, 150))
        display_moving_screen(x)
        text_font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE)
        text_to_display = text_font.render("Score: " + str(mario.score), True, WHITE)
        text_rect = text_to_display.get_rect()
        text_rect.x = TEXT_BUFFER
        text_rect.y = TEXT_BUFFER
        text_pos = text_rect
        screen.blit(text_to_display, text_pos)
        text_to_display = text_font.render("Lives: " + str(mario.life), True, WHITE)
        text_rect = text_to_display.get_rect()
        text_rect.x = WINDOW_WIDTH - TEXT_BUFFER - text_rect.width
        text_rect.y = TEXT_BUFFER
        text_pos = text_rect
        screen.blit(text_to_display, text_pos)


    elif cerrent_screen =="end_screen()":
        screen.blit(img2, (x_loc, y_loc))
    elif cerrent_screen == "wining screen()":
        screen.blit(img4, (x_loc, y_loc))
        text_font = pygame.font.SysFont('Comic Sans MS', FONT_SIZE*2)
        text_to_display = text_font.render("Score: " + str(mario.score), True, WHITE)
        text_rect = text_to_display.get_rect()
        text_rect.x = (WINDOW_WIDTH - text_rect.width)/2
        text_rect.y = WINDOW_HEIGHT - TEXT_BUFFER_V2
        text_pos = text_rect
        screen.blit(text_to_display, text_pos)




def display_moving_screen(x):
    mario.show_on_screen(screen, x)

    for enemy in enemy_list:
        if enemy.status:
            enemy.show_on_screen(screen,x)
    for obstacle in obstacle_list:
        obstacle.show_on_screen(screen, x)
    for coin in coin_list:
        if coin.status:
            coin.show_on_screen(screen, x)
    if mushroom1.status:
        mushroom1.show_on_screen(screen, x)
    screen.blit(img3, (TOTAL_WIDTH - FINISH_LINE_WIDTH +x, y_loc))


running = True
start_button = Button(222, 453, 446, 161)
while running:

    if check_Collision_Meeting(x):
        x= 0
    if mario.life == 0:
        pygame.mixer.music.load("sounds/YOU_DIED_HD[EagleConverter.com].mp3")
        pygame.mixer.music.play()
        mario.life = -1
        cerrent_screen = "end_screen()"

    display_screen(x)

    mario.move("y_axis")
    mario.gravity()
    check_y_axis_obstacle(mario)
    move_enemy_main(x)


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = event.pos
            if mouse_in_button(start_button, mouse_pos):
                cerrent_screen = "game_screen()"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                mario.jump()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and check_left_obstacle(mario, x):
        mario.move(LEFT)

    if keys[pygame.K_RIGHT] and check_right_obstacle(mario):
        mario.move(RIGHT)
        if mario.location[X_AXIS] + x > SCREEN_WIDTH / 2 and mario.location[
            X_AXIS] - MARIO_SPEED <= TOTAL_WIDTH - SCREEN_WIDTH / 2:
            x = SCREEN_WIDTH / 2 - mario.location[X_AXIS]
    if mario.location[X_AXIS]+ mario.size > TOTAL_WIDTH-FINISH_LINE_WIDTH:
        cerrent_screen = "wining screen()"
        pygame.mixer.music.load("sounds/Queen_We_Are_The_Champions_Ringtone_(by Fringster.com).mp3")
        pygame.mixer.music.play()
        mario.location[X_AXIS]= 0


    pygame.display.flip()
pygame.quit()
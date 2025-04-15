import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = test_font.render(f'score: {current_time}', False, (113, 42, 135))
    score_rect = score_surf.get_rect(center=(400, 50))
    pygame.draw.rect(screen, "#c0e8ec", score_rect.inflate(15, 6), 13, 15)
    screen.blit(score_surf, score_rect)
    return current_time


def obstacle_movement(obstacle_list):
    global mons_hit
    new_list = []
    for obstacle_rect in obstacle_list:
        obstacle_rect.x -= 5
        if player_rect.colliderect(obstacle_rect):
            mons_hit = True
        if obstacle_rect.right > 0:
            if obstacle_rect.bottom == 200:
                if (pygame.time.get_ticks() // 200) % 2 == 0:
                    screen.blit(fly_surf, obstacle_rect)
                else:
                    screen.blit(fly_surf2, obstacle_rect)
            else:
                screen.blit(mons_surf, obstacle_rect)
            new_list.append(obstacle_rect)
    return new_list


pygame.init()
screen = pygame.display.set_mode(size=(800, 400),
                                 flags=0,
                                 depth=0,
                                 display=0,
                                 vsync=0)

pygame.display.set_caption(title="learning-跑步", icontitle="None")
# set up maximum fps (minimum fps also approachable by using other approach)
clock = pygame.time.Clock()
test_font = pygame.font.Font(r"D:\uoa_course\skills\Airflow_tutorial\aaa\font\Pixeltype.ttf", 50)
title_font = pygame.font.Font(r"D:\uoa_course\skills\Airflow_tutorial\aaa\font\Pixeltype.ttf", 65)
game_active = False
start_time = 0
score = 0

# create regular surf
# test_surf = pygame.Surf((100, 200))  # pygame has origin at top left, y extends downward
# test_surf.fill("Red")
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

# Because the use of previous display_score, following has been removed
# score_surf = test_font.render("My game", False, (113, 42, 135)).convert()
# score_rect = score_surf.get_rect(center=(400, 50))

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
fly_surf = pygame.image.load("graphics/fly/fly1.png")
snail_rect = snail_surf.get_rect(midbottom=(600, 300))
snail_surf2 = pygame.image.load("graphics/snail/snail2.png")
fly_surf2 = pygame.image.load("graphics/fly/fly2.png")

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))  # on the ground surf
player_surf2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_gravity = 0

# start menu
title_surf = title_font.render("Pixel Runner", False, (82, 196, 209)).convert()
title_rect = title_surf.get_rect(center=(400, 100))
start_line = title_font.render("Press Space to Start", False, (82, 196, 209)).convert()
start_rect = start_line.get_rect(center=(400, 300))
static_player = pygame.image.load('graphics/player/player_stand.png').convert_alpha()
# static_player_scaled = pygame.transform.scale(static_player, (200, 400))
static_rect = static_player.get_rect(center=(400, 200))

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 3000)  # add one event every 3000ms

# obstacle list
obstacle_rect_list = []
mons_surf = pygame.image.load("kenny_char/tile_0000.png").convert_alpha()
# print(mons_surf.get_size())
mons_surf = pygame.transform.scale(mons_surf, (55, 55))
mons_rect = mons_surf.get_rect(midbottom=(700, 300))
mons_hit = False

# music
player_sound = pygame.mixer.Sound("audio/jump.mp3")
player_sound.set_volume(0.2)
bgm = pygame.mixer.Sound("audio/music.wav")
bgm.set_volume(0.3)
bgm.play()

# To keep screen running forever
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()  # shut down every code
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # mousebuttonup/down
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
                # print(event.pos)

                if player_rect.collidepoint(event.pos):
                    pass
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
                    player_sound.play()
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

                snail_rect.left = 800
                start_time = int(pygame.time.get_ticks() / 1000)
        if event.type == obstacle_timer and game_active:
            if randint(0, 2):
                obstacle_rect_list.append(fly_surf.get_rect(midbottom=(randint(900, 1100), 200)))
            else:
                obstacle_rect_list.append(mons_surf.get_rect(midbottom=(randint(900, 1100), 300)))

    if game_active:
        # draw all our elements, update everything
        screen.blit(sky_surf, (0, 0))
        screen.blit(ground_surf, (0, 300))
        # pygame.draw.rect(screen, "#c0e8ec", score_rect.inflate(15, 6), 13, 15)
        # # pygame.draw.line(screen, "Gold", (0, 0), pygame.mouse.get_pos(), 10)
        # # pygame.draw.ellipse(screen, "brown", pygame.Rect(50, 200, 100, 100))
        # screen.blit(score_surf, score_rect)
        score = display_score()

        if snail_rect.left < -100:
            snail_rect.left = 800
        if (pygame.time.get_ticks() // 200) % 2 == 0:
            screen.blit(snail_surf, snail_rect)
        else: screen.blit(snail_surf2, snail_rect)
        snail_rect.left -= 5

        # player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        if (pygame.time.get_ticks() // 200) % 2 == 0:
            screen.blit(player_surf, player_rect)
        else:
            screen.blit(player_surf2, player_rect)

        # obstacles movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        if snail_rect.colliderect(player_rect) or mons_hit:
            game_active = False
            # pygame.quit()
            # exit()
        # keys = pygame.key.get_pressed()
        # if player_rect.colliderect(snail_rect):
        #     pass
        # mouse_pos = pygame.mouse.get_pos()
        # if player_rect.collidepoint(mouse_pos):
        #     # print(pygame.mouse.get_pressed())
        #     break
    else:
        score_massage = title_font.render(f"Your final score is  {score}", False, (82, 196, 209))
        score_massage_rect = score_massage.get_rect(center=(400, 100))
        screen.fill((25, 87, 94))
        if score == 0:
            screen.blit(title_surf, title_rect)

        else:
            screen.blit(score_massage, score_massage_rect)
        screen.blit(start_line, start_rect)
        screen.blit(static_player, static_rect)
        mons_hit = False
        obstacle_rect_list.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
    pygame.display.update()  # to keep window showing
    clock.tick(60)  # maximum fps rate = 60

import pygame
from player import Player
from enemy import Enemy
from projectile import Projectile
import time
import shelve


pygame.init()

# Create the window
screen = pygame.display.set_mode((550, 850))

# Background image
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, screen.get_size())

# Set caption and load/set icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("player.png")
pygame.display.set_icon(icon)

# Title font
title_font = pygame.font.Font("superchargelaser.ttf", 20)
title_x = 170
title_y = 10
title = title_font.render("Space Invaders", True, (255, 0, 0))

# score font
score = 0
score_font = pygame.font.Font("supercharge3d.ttf", 30)
score_x = 180
score_y = 780

# timer font
timer_font = pygame.font.Font("supercharge.ttf", 16)
timer_x = 10
timer_y = 25

# high score font
high_score_font = pygame.font.Font("supercharge.ttf", 16)
high_score_x = 400
high_score_y = 25

running = True
clock = pygame.time.Clock()

player = Player(pygame.K_a, pygame.K_d, pygame.K_LEFT, pygame.K_RIGHT)
enemy = Enemy()

num_of_enemies = 1
enemy_group = pygame.sprite.Group()
next_enemy_time = time.time() + 0  # Time for the next enemy
next_player_projectile = time.time() + 0  # Time for the next laser

player_projectile_group = pygame.sprite.Group()

laser_sound = pygame.mixer.Sound("laser_sound.wav")
laser_sound.set_volume(0.2)
explosion_sound = pygame.mixer.Sound("explosion.wav")
explosion_sound.set_volume(0.4)
background_sound = pygame.mixer.Sound("background.wav")
background_sound.set_volume(0.6)

background_sound.play()

start_time = pygame.time.get_ticks()

d = shelve.open('score.txt')


def end_game():
    global running
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background, (0, 0))
        screen.blit(title, (title_x, title_y))
        score_text = score_font.render("Game Over", True, (255, 255, 255))
        screen.blit(score_text, (score_x, score_y))
        pygame.display.update()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Add a new enemy every 3 seconds
    if time.time() >= next_enemy_time:
        enemy_group.add(Enemy())
        next_enemy_time += 1

    keys = pygame.key.get_pressed()

    if time.time() >= next_player_projectile:
        if keys[pygame.K_SPACE]:
            player_projectile_group.add(Projectile(player.rect.x + 16, player.rect.y - 25))
            next_player_projectile += 1
            laser_sound.play()
        else:
            next_player_projectile += 1

    current_time = (pygame.time.get_ticks() - start_time) / 1000

    # Draw background
    screen.blit(background, (0, 0))
    # Draw text
    screen.blit(title, (title_x, title_y))
    score_text = score_font.render("Score: " + str(score), True, (255, 255, 255))
    timer_text = timer_font.render("Time: " + str(round(current_time, 1)), True, (255, 255, 255))
    high_score_text = high_score_font.render("High Score: " + str(d["score"]), True, (255, 255, 255))
    screen.blit(high_score_text, (high_score_x, high_score_y))
    screen.blit(score_text, (score_x, score_y))
    screen.blit(timer_text, (timer_x, timer_y))
    # Draw the player and enemy
    player.draw(screen)
    enemy_group.draw(screen)
    player_projectile_group.draw(screen)
    # Move the player
    player.move()
    enemy_group.update()
    player_projectile_group.update()
    # collision
    collision_list = pygame.sprite.groupcollide(player_projectile_group, enemy_group, True, True)
    for projectile, enemies in collision_list.items():
        for enemy in enemies:
            explosion_sound.play()
            score += 1

    player_list = pygame.sprite.spritecollide(player, enemy_group, True)
    for hit in player_list:
        d['score'] = score
        d.close()
        end_game()

    pygame.display.update()
    clock.tick(120)

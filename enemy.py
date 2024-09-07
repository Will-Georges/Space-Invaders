import pygame
import random


horizontal_multiplier = 1


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ufo.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = random.randint(0, 486)
        self.rect.y = 70
        self.y_float = self.rect.y
        self.speed = 2
        self.horizontal_multiplier = 1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, round(self.y_float)))  # Round y_float to integer when drawing

    def update(self):
        self.move()

    def move(self):
        self.rect.x += self.speed * self.horizontal_multiplier
        self.y_float += 0.3  # Update floating-point y position

        # Convert y_float to integer for collision and boundary checks
        self.rect.y = round(self.y_float)

        # Check boundaries for each enemy
        if self.rect.x <= 0:
            self.horizontal_multiplier = 1  # Change direction for this enemy only
            self.rect.x = 0
        elif self.rect.x >= 486:
            self.horizontal_multiplier = -1  # Change direction for this enemy only
            self.rect.x = 486

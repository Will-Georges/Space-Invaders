import pygame
import random


class Projectile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("laser.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))  # Round y_float to integer when drawing

    def update(self):
        self.move()

    def move(self):
        self.rect.y -= self.speed

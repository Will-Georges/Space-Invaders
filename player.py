import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self, left, right, left1, right1):
        super().__init__()
        self.image = pygame.image.load("player.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.x = 225
        self.rect.y = 700
        self.speed = 2
        self.left = left
        self.right = right
        self.left1 = left1
        self.right1 = right1

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[self.left] or keys[self.left1]:
            self.rect.x -= self.speed
        if keys[self.right] or keys[self.right1]:
            self.rect.x += self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 486:
            self.rect.x = 486

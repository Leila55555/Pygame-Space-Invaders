import pygame, random

class Alien(pygame.sprite.Sprite):
    def __init__(self, type, image, x,y):
        super().__init__()
        self.type = type
        self.image = image
        self. rect = pygame.Rect(self.image.get_rect(topleft = (x, y)))

    def update(self,direction):
        self.rect.x += direction
class MysteryShip(pygame.sprite.Sprite):
    def __init__(self, screen_width):
        super().__init__()
        self.screen_width = screen_width
        self.image = pygame.image.load('mysteryship.png')

        x = random.choice([0,screen_width - self.image.get_width()])
        if x == 0:
            self.speed = 3
        else:
            self.speed = -3

        self.rect = self.image.get_rect(topleft = (x, 85))

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width:
            self.kill()
        elif self.rect.left < 0:
            self.kill()

import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('./assets/images/coffee_bag.png')
        self.rect = self.image.get_rect()
        self.rect.center = (640 / 2, 480 / 2)
        self.rect.y = 390

    def aButtonClicked(self, x):
        self.rect.x += -x
        if self.rect.right <= 0:
            self.rect.left = 640

    def dButtonClicked(self, x):
        self.rect.x += x
        if self.rect.left >= 640:
            self.rect.right = 0
import pygame
import images
import os


class PhotoRect:
    def __init__(self, screen, filename, sizex, sizey):
        self.name = "graphic\\" + filename + ".png"
        this_folder = os.path.dirname(os.path.abspath(__file__))
        self.name = os.path.join(this_folder, self.name)
        self.screen = screen
        self.image = pygame.image.load(self.name)
        self.image = pygame.transform.scale(self.image, (sizex, sizey))

        self.rect = self.image.get_rect()
        self.rect.left -= self.rect.width
        self.rect.top -= self.rect.height

    def blitme(self):
        self.screen.blit(self.image, self.rect)

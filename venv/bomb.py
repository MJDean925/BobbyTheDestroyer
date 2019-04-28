from pygame.sprite import Sprite
from photo_rect import PhotoRect
import pygame


class Bomb(Sprite):

    def __init__(self, screen, row, col, pla, guard):
        super(Bomb, self).__init__()
        self.player = pla
        self.guard = guard
        self.screen = screen
        self.s_rect = screen.get_rect()
        self.im = PhotoRect(screen, "bomb\\bomb_idle", 64, 64)
        self.im.rect.centerx = col * 64 + 32
        self.im.rect.centery = row * 64 + 32
        self.rect = self.im.rect
        self.row = row
        self.col = col
        self.timer = pygame.time.get_ticks()
        self.finished = False
        self.detonating = False
        self.stepped = False
        self.state = 1

    def boom(self):
        if not self.finished:
            if self.player.col == self.col and self.player.row == self.row and not self.stepped:
                self.stepped = True
                self.timer = pygame.time.get_ticks()
            elif self.stepped and pygame.time.get_ticks() - self.timer >= 2000 and not self.detonating:
                self.detonating = True
                self.timer = pygame.time.get_ticks()
                # Check guards for if they hear it in this spot
                self.guard.get_path(self.row, self.col)
            elif self.detonating and pygame.time.get_ticks() - self.timer >= 100:
                self.timer = pygame.time.get_ticks()
                temp = "bomb\\b" + str(self.state)
                self.rect = self.im.rect
                self.im = PhotoRect(self.screen, temp, 64, 64)
                self.im.rect = self.rect
                if self.state >= 5:
                    self.finished = True
                    # Manipulate finishing game
                else:
                    self.state += 1

    def blitme(self):
        if not self.finished:
            self.im.blitme()
from photo_rect import PhotoRect
import pygame
from pygame.sprite import Group


class Level:
    WALL_SIZE = 64

    def __init__(self, screen, levelfile):
        self.screen = screen
        self.filename = levelfile

        with open(self.filename, 'r') as f:
            self.rows = f.read().splitlines()


        self.mblocks = []
        sz = Level.WALL_SIZE

        self.mblock = PhotoRect(screen, "block", sz, sz)
        self.deltax = self.deltay = sz

        self.build()

    def build(self):
        r = self.mblock.rect
        w, h = r.width, r.height
        dx, dy, = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]

                if col == 'M':
                    self.mblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))


    def blitme(self):
        for rect in self.mblocks:
            self.screen.blit(self.mblock.image, rect)

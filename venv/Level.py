from photo_rect import PhotoRect
import pygame
from pygame.sprite import Group


class Level:
    WALL_SIZE = 10

    def __init__(self, screen, levelfile):
        self.screen = screen
        self.filename = levelfile

        with open(self.filename, 'r') as f:
            self.rows = f.read().splitlines()

        self.lblocks = []
        self.rblocks = []
        self.tblocks = []
        self.bblocks = []
        self.gblocks = []
        self.mblocks = []
        self.nblocks = []
        self.oblocks = []
        self.yblocks = []
        self.zblocks = []
        self.wblocks = []
        self.xblocks = []
        sz = Level.WALL_SIZE
        self.lblock = PhotoRect(screen, "left_blocks", sz, sz)
        self.rblock = PhotoRect(screen, "right_blocks", sz, sz)
        self.tblock = PhotoRect(screen, "top_blocks", sz, sz)
        self.bblock = PhotoRect(screen, "bottom_blocks", sz, sz)
        self.gblock = PhotoRect(screen, "top_right_block", sz, sz)
        self.mblock = PhotoRect(screen, "top_left_block", sz, sz)
        self.nblock = PhotoRect(screen, "bottom_right_block", sz, sz)
        self.oblock = PhotoRect(screen, "bottom_left_block", sz, sz)
        self.yblock = PhotoRect(screen, "top_left_corner_blocks", sz, sz)
        self.zblock = PhotoRect(screen, "top_right_corner_blocks", sz, sz)
        self.wblock = PhotoRect(screen, "bottom_left_corner_blocks", sz, sz)
        self.xblock = PhotoRect(screen, "bottom_right_corner_blocks", sz, sz)

        self.deltax = self.deltay = Level.BRICK_SIZE

        self.build()

    def build(self):
        r = self.lblock.rect
        w, h = r.width, r.height
        dx, dy, = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'L':
                    self.lblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'R':
                    self.rblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'T':
                    self.tblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'B':
                    self.bblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'G':
                    self.gblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'M':
                    self.mblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'N':
                    self.nblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'O':
                    self.oblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'Y':
                    self.yblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'Z':
                    self.zblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'W':
                    self.wblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'X':
                    self.xblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for rect in self.tblocks:
            self.screen.blit(self.tblock.image, rect)
        for rect in self.bblocks:
            self.screen.blit(self.bblock.image, rect)
        for rect in self.rblocks:
            self.screen.blit(self.rblock.image, rect)
        for rect in self.lblocks:
            self.screen.blit(self.lblock.image, rect)
        for rect in self.gblocks:
            self.screen.blit(self.gblock.image, rect)
        for rect in self.mblocks:
            self.screen.blit(self.mblock.image, rect)
        for rect in self.nblocks:
            self.screen.blit(self.nblock.image, rect)
        for rect in self.oblocks:
            self.screen.blit(self.oblock.image, rect)
        for rect in self.yblocks:
            self.screen.blit(self.yblock.image, rect)
        for rect in self.zblocks:
            self.screen.blit(self.zblock.image, rect)
        for rect in self.wblocks:
            self.screen.blit(self.wblock.image, rect)
        for rect in self.xblocks:
            self.screen.blit(self.xblock.image, rect)

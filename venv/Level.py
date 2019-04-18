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

        self.ablocks = []
        self.bblocks = []
        self.cblocks = []
        self.dblocks = []
        self.eblocks = []
        self.fblocks = []
        self.gblocks = []
        self.hblocks = []
        self.iblocks = []
        self.jblocks = []
        self.kblocks = []
        self.lblocks = []
        self.mblocks = []
        sz = Level.WALL_SIZE
        self.ablock = PhotoRect(screen, "blocks\\A", sz, sz)
        self.bblock = PhotoRect(screen, "blocks\\B", sz, sz)
        self.cblock = PhotoRect(screen, "blocks\\C", sz, sz)
        self.dblock = PhotoRect(screen, "blocks\\D", sz, sz)
        self.eblock = PhotoRect(screen, "blocks\\E", sz, sz)
        self.fblock = PhotoRect(screen, "blocks\\F", sz, sz)
        self.gblock = PhotoRect(screen, "blocks\\G", sz, sz)
        self.hblock = PhotoRect(screen, "blocks\\H", sz, sz)
        self.iblock = PhotoRect(screen, "blocks\\I", sz, sz)
        self.jblock = PhotoRect(screen, "blocks\\J", sz, sz)
        self.kblock = PhotoRect(screen, "blocks\\K", sz, sz)
        self.lblock = PhotoRect(screen, "blocks\\L", sz, sz)
        self.mblock = PhotoRect(screen, "blocks\\M", sz, sz)
        self.deltax = self.deltay = sz

        self.build()

    def build(self):
        r = self.lblock.rect
        w, h = r.width, r.height
        dx, dy, = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'A':
                    self.ablocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'B':
                    self.bblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'C':
                    self.cblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'D':
                    self.dblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'E':
                    self.eblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'F':
                    self.fblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'G':
                    self.gblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'H':
                    self.hblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'I':
                    self.iblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'J':
                    self.jblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'K':
                    self.kblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'L':
                    self.lblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'M':
                    self.mblocks.append(pygame.Rect(ncol * dx, nrow * dy, w, h))


    def blitme(self):
        for rect in self.ablocks:
            self.screen.blit(self.bblock.image, rect)
        for rect in self.bblocks:
            self.screen.blit(self.bblock.image, rect)
        for rect in self.cblocks:
            self.screen.blit(self.cblock.image, rect)
        for rect in self.dblocks:
            self.screen.blit(self.dblock.image, rect)
        for rect in self.eblocks:
            self.screen.blit(self.mblock.image, rect)
        for rect in self.fblocks:
            self.screen.blit(self.fblock.image, rect)
        for rect in self.gblocks:
            self.screen.blit(self.gblock.image, rect)
        for rect in self.hblocks:
            self.screen.blit(self.hblock.image, rect)
        for rect in self.iblocks:
            self.screen.blit(self.iblock.image, rect)
        for rect in self.jblocks:
            self.screen.blit(self.jblock.image, rect)
        for rect in self.kblocks:
            self.screen.blit(self.kblock.image, rect)
        for rect in self.lblocks:
            self.screen.blit(self.lblock.image, rect)
        for rect in self.mblocks:
            self.screen.blit(self.mblock.image, rect)

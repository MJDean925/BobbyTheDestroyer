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

        self.lwalls = []
        self.rwalls = []
        self.twalls = []
        self.bwalls = []
        self.gwalls = []
        self.mwalls = []
        self.nwalls = []
        self.owalls = []
        self.ywalls = []
        self.zwalls = []
        self.wwalls = []
        self.xwalls = []
        sz = Level.WALL_SIZE
        self.lwall = PhotoRect(screen, "left_wall", sz, sz)
        self.rwall = PhotoRect(screen, "right_wall", sz, sz)
        self.twall = PhotoRect(screen, "top_wall", sz, sz)
        self.bwall = PhotoRect(screen, "bottom_wall", sz, sz)
        self.gwall = PhotoRect(screen, "top_right_in", sz, sz)
        self.mwall = PhotoRect(screen, "top_left_in", sz, sz)
        self.nwall = PhotoRect(screen, "bottom_right_in", sz, sz)
        self.owall = PhotoRect(screen, "bottom_left_in", sz, sz)
        self.ywall = PhotoRect(screen, "top_left_out", sz, sz)
        self.zwall = PhotoRect(screen, "top_right_out", sz, sz)
        self.wwall = PhotoRect(screen, "bottom_left_out", sz, sz)
        self.xwall = PhotoRect(screen, "bottom_right_out", sz, sz)

        self.deltax = self.deltay = Level.BRICK_SIZE

        self.build()

    def build(self):
        r = self.lwall.rect
        w, h = r.width, r.height
        dx, dy, = self.deltax, self.deltay

        for nrow in range(len(self.rows)):
            row = self.rows[nrow]
            for ncol in range(len(row)):
                col = row[ncol]
                if col == 'L':
                    self.lwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'R':
                    self.rwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'T':
                    self.twalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'B':
                    self.bwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'G':
                    self.gwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'M':
                    self.mwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'N':
                    self.nwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'O':
                    self.owalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'Y':
                    self.ywalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'Z':
                    self.zwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'W':
                    self.wwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))
                elif col == 'X':
                    self.xwalls.append(pygame.Rect(ncol * dx, nrow * dy, w, h))

    def blitme(self):
        for rect in self.twalls:
            self.screen.blit(self.twall.image, rect)
        for rect in self.bwalls:
            self.screen.blit(self.bwall.image, rect)
        for rect in self.rwalls:
            self.screen.blit(self.rwall.image, rect)
        for rect in self.lwalls:
            self.screen.blit(self.lwall.image, rect)
        for rect in self.gwalls:
            self.screen.blit(self.gwall.image, rect)
        for rect in self.mwalls:
            self.screen.blit(self.mwall.image, rect)
        for rect in self.nwalls:
            self.screen.blit(self.nwall.image, rect)
        for rect in self.owalls:
            self.screen.blit(self.owall.image, rect)
        for rect in self.ywalls:
            self.screen.blit(self.ywall.image, rect)
        for rect in self.zwalls:
            self.screen.blit(self.zwall.image, rect)
        for rect in self.wwalls:
            self.screen.blit(self.wwall.image, rect)
        for rect in self.xwalls:
            self.screen.blit(self.xwall.image, rect)

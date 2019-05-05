from a_star import a_star_alg
from photo_rect import PhotoRect
import pygame


class Guard:
    def __init__(self, screen, row, col, player, level):
        self.row = row
        self.col = col
        self.screen = screen
        self.goal_col = 12  # [m]
        self.goal_row = 12  # [m]
        self.matrix_size = 1.0  # [m]
        self.rob_size = 0.0  # [m]
        self.player = player
        self.level = level
        self.velocity = 120
        self.pathx, self.pathy = [], []
        self.ph = PhotoRect(self.screen, "enemy\\enemy_down\\enemy_down_1", 64, 64)
        self.ph.rect.centerx = col * 64 + 32
        self.ph.rect.centery = row * 64 + 32
        self.rect = self.ph.rect
        self.obs_xpos = []
        self.obs_ypos = []
        self.prow1 = 12
        self.pcol1 = 1
        self.prow2 = 12
        self.pcol2 = 12
        self.prow3 = 8
        self.pcol3 = 12
        self.prow4 = 8
        self.pcol4 = 1
        self.anim_timer = pygame.time.get_ticks()
        self.state = 1
        self.speed_timer = pygame.time.get_ticks()
        self.prepare()
        self.seen = False

    def prepare(self):

        for i in range(13):
            self.obs_xpos.append(i)
            self.obs_ypos.append(0.0)
        for i in range(13):
            self.obs_xpos.append(13.0)
            self.obs_ypos.append(i)
        for i in range(14):
            self.obs_xpos.append(i)
            self.obs_ypos.append(13.0)
        for i in range(14):
            self.obs_xpos.append(0.0)
            self.obs_ypos.append(i)

        #######################################################
        for i in range(1):
            self.obs_xpos.append(12)
            self.obs_ypos.append(i + 7)
        #######################################################
        for i in range(1):
            self.obs_xpos.append(11)
            self.obs_ypos.append(i + 11)

        for i in range(4):
            self.obs_xpos.append(11)
            self.obs_ypos.append(i + 2)
        #######################################################
        for i in range(1):
            self.obs_xpos.append(10)
            self.obs_ypos.append(i + 11)
        for i in range(1):
            self.obs_xpos.append(10)
            self.obs_ypos.append(i + 9)
        for i in range(4):
            self.obs_xpos.append(10)
            self.obs_ypos.append(i + 2)

        ######################################################
        for i in range(1):
            self.obs_xpos.append(9)
            self.obs_ypos.append(i + 11)

        for i in range(1):
            self.obs_xpos.append(9)
            self.obs_ypos.append(i + 9)

        #######################################################

        for i in range(4):
            self.obs_xpos.append(8)
            self.obs_ypos.append(i + 4)

        for i in range(1):
            self.obs_xpos.append(8)
            self.obs_ypos.append(i + 2)
        ########################################################
        for i in range(1):
            self.obs_xpos.append(7)
            self.obs_ypos.append(i + 11)

        for i in range(1):
            self.obs_xpos.append(7)
            self.obs_ypos.append(i + 9)

        for i in range(1):
            self.obs_xpos.append(7)
            self.obs_ypos.append(i + 6)

        for i in range(1):
            self.obs_xpos.append(7)
            self.obs_ypos.append(i + 2)

        #######################################################

        for i in range(1):
            self.obs_xpos.append(6)
            self.obs_ypos.append(i + 11)

        for i in range(1):
            self.obs_xpos.append(6)
            self.obs_ypos.append(i + 9)

        for i in range(1):
            self.obs_xpos.append(6)
            self.obs_ypos.append(i + 6)

        for i in range(1):
            self.obs_xpos.append(6)
            self.obs_ypos.append(i + 2)

        #########################################################

        for i in range(4):
            self.obs_xpos.append(5)
            self.obs_ypos.append(i + 4)

        for i in range(1):
            self.obs_xpos.append(5)
            self.obs_ypos.append(i + 2)
        #########################################################

        for i in range(1):
            self.obs_xpos.append(4)
            self.obs_ypos.append(i + 11)
        for i in range(1):
            self.obs_xpos.append(4)
            self.obs_ypos.append(i + 9)

        ##########################################################

        for i in range(1):
            self.obs_xpos.append(3)
            self.obs_ypos.append(i + 11)

        for i in range(1):
            self.obs_xpos.append(3)
            self.obs_ypos.append(i + 9)

        for i in range(4):
            self.obs_xpos.append(3)
            self.obs_ypos.append(i + 2)

        ##########################################################

        for i in range(1):
            self.obs_xpos.append(2)
            self.obs_ypos.append(i + 11)

        for i in range(4):
            self.obs_xpos.append(2)
            self.obs_ypos.append(i + 2)

        ##########################################################

        for i in range(1):
            self.obs_xpos.append(1)
            self.obs_ypos.append(i + 7)
        self.get_path(self.goal_row, self.goal_col)

    def get_path(self, grow, gcol):
        self.goal_col, self.goal_row = gcol, grow
        self.pathx, self.pathy = a_star_alg(self.col, self.row, gcol, grow, self.obs_xpos, self.obs_ypos,
                                            self.matrix_size, self.rob_size)

    def update(self):

        if pygame.time.get_ticks() - self.speed_timer >= self.velocity:
            self.speed_timer = pygame.time.get_ticks()
            if self.row == self.player.row and self.col == self.player.col:
                self.player.dead = True
            if self.row == self.goal_row and self.col == self.goal_col:
                if self.seen:
                    self.seen = False
                if self.row == self.prow1 and self.col == self.pcol1:
                    self.get_path(self.prow2, self.pcol2)
                elif self.row == self.prow2 and self.col == self.pcol2:
                    self.get_path(self.prow3, self.pcol3)
                elif self.row == self.prow3 and self.col == self.pcol3:
                    self.get_path(self.prow4, self.pcol4)
                elif self.row == self.prow4 and self.col == self.pcol4:
                    self.get_path(self.prow1, self.pcol1)
                else:
                    self.get_path(self.prow1, self.pcol1)

                self.col = self.pathx.pop()
                self.row = self.pathy.pop()
                self.ph.rect.centerx = self.col * 64 + 32
                self.ph.rect.centery = self.row * 64 + 32
                self.rect = self.ph.rect
            elif self.row != self.goal_row or self.col != self.goal_col:
                self.col = self.pathx.pop()
                self.row = self.pathy.pop()
                self.ph.rect.centerx = self.col * 64 + 32
                self.ph.rect.centery = self.row * 64 + 32
                self.rect = self.ph.rect

        if pygame.time.get_ticks() - self.anim_timer >= 10:
            self.anim_timer = pygame.time.get_ticks()
            if self.state < 10:
                self.state += 1
            else:
                self.state = 1
            temp = "enemy\\enemy_down\\enemy_down_" + str(self.state)
            self.rect = self.ph.rect
            self.ph = PhotoRect(self.screen, temp, 64, 64)
            self.ph.rect = self.rect

    def sight(self):
        if not self.player.dead and not self.seen:
            if self.player.row == self.row:
                if self.player.col < self.col:
                    for x in range(self.player.col, int(self.col)):
                        if self.level.rows[int(self.row)][x] == 'M':
                            return False
                    self.seen = True
                    self.get_path(self.player.row, self.player.col)
                elif self.player.col > self.col:
                    for x in range(int(self.col), self.player.col):
                        if self.level.rows[int(self.row)][x] == 'M':
                            return False
                    self.seen = True
                    self.get_path(self.player.row, self.player.col)
            elif self.player.col == self.col:
                if self.player.row < self.row:
                    for x in range(self.player.row, int(self.row)):
                        if self.level.rows[x][int(self.col)] == 'M':
                            return False
                    self.seen = True
                    self.get_path(self.player.row, self.player.col)
                elif self.player.row > self.row:
                    for x in range(int(self.row), self.player.row):
                        if self.level.rows[x][int(self.col)] == 'M':
                            return False
                    self.seen = True
                    self.get_path(self.player.row, self.player.col)

    def faster(self):
        self.velocity = self.velocity * 0.8

    def blitme(self):
        self.ph.blitme()

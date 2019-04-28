from a_star import a_star_alg
from photo_rect import PhotoRect


class Guard:
    def __init__(self, screen, row, col, player, level):
        self.row = row
        self.col = col

        self.goal_col = 13  # [m]
        self.goal_row = 9.0  # [m]
        self.matrix_size = 1.0  # [m]
        self.rob_size = 0.0  # [m]
        self.player = player
        self.level = level
        self.pathx, self.pathy = [], []
        self.ph = PhotoRect(screen, "enemy\\enemy_v1_moving_down", 64, 64)
        self.rect = self.ph.rect
        self.obs_col = []
        self.obs_row = []
        self.prepare()

    def prepare(self):

        for i in range(13):
            self.obs_col.append(i)
            self.obs_row.append(0.0)
        for i in range(13):
            self.obs_col.append(13.0)
            self.obs_row.append(i)
        for i in range(14):
            self.obs_col.append(i)
            self.obs_row.append(13.0)
        for i in range(14):
            self.obs_col.append(0.0)
            self.obs_row.append(i)

        #
        # for i in range(50):
        #     self.obs_col.append(i)
        #     self.obs_row.append(0.0)
        # for i in range(50):
        #     self.obs_col.append(50.0)
        #     self.obs_row.append(i)
        # for i in range(51):
        #     self.obs_col.append(i)
        #     self.obs_row.append(50.0)
        # for i in range(51):
        #     self.obs_col.append(0.0)
        #     self.obs_row.append(i)
        #

        #######################################################
        for i in range(1):
            self.obs_col.append(12)
            self.obs_row.append(i + 7)
        #######################################################
        for i in range(1):
            self.obs_col.append(11)
            self.obs_row.append(i + 11)

        for i in range(4):
            self.obs_col.append(11)
            self.obs_row.append(i + 2)
        #######################################################
        for i in range(1):
            self.obs_col.append(10)
            self.obs_row.append(i + 11)
        for i in range(1):
            self.obs_col.append(10)
            self.obs_row.append(i + 9)
        for i in range(4):
            self.obs_col.append(10)
            self.obs_row.append(i + 2)

        ######################################################
        for i in range(1):
            self.obs_col.append(9)
            self.obs_row.append(i + 11)

        for i in range(1):
            self.obs_col.append(9)
            self.obs_row.append(i + 9)

        #######################################################

        for i in range(4):
            self.obs_col.append(8)
            self.obs_row.append(i + 4)

        for i in range(1):
            self.obs_col.append(8)
            self.obs_row.append(i + 2)
        ########################################################
        for i in range(1):
            self.obs_col.append(7)
            self.obs_row.append(i + 11)

        for i in range(1):
            self.obs_col.append(7)
            self.obs_row.append(i + 9)

        for i in range(1):
            self.obs_col.append(7)
            self.obs_row.append(i + 6)

        for i in range(1):
            self.obs_col.append(7)
            self.obs_row.append(i + 2)

        #######################################################

        for i in range(1):
            self.obs_col.append(6)
            self.obs_row.append(i + 11)

        for i in range(1):
            self.obs_col.append(6)
            self.obs_row.append(i + 9)

        for i in range(1):
            self.obs_col.append(6)
            self.obs_row.append(i + 6)

        for i in range(1):
            self.obs_col.append(6)
            self.obs_row.append(i + 2)

        #########################################################

        for i in range(4):
            self.obs_col.append(5)
            self.obs_row.append(i + 4)

        for i in range(1):
            self.obs_col.append(5)
            self.obs_row.append(i + 2)
        #########################################################

        for i in range(1):
            self.obs_col.append(4)
            self.obs_row.append(i + 11)
        for i in range(1):
            self.obs_col.append(4)
            self.obs_row.append(i + 9)

        ##########################################################

        for i in range(1):
            self.obs_col.append(3)
            self.obs_row.append(i + 11)

        for i in range(1):
            self.obs_col.append(3)
            self.obs_row.append(i + 9)

        for i in range(4):
            self.obs_col.append(3)
            self.obs_row.append(i + 2)

        ##########################################################

        for i in range(1):
            self.obs_col.append(2)
            self.obs_row.append(i + 11)

        for i in range(4):
            self.obs_col.append(2)
            self.obs_row.append(i + 2)

        ##########################################################

        for i in range(1):
            self.obs_col.append(1)
            self.obs_row.append(i + 7)
        self.get_path(self.goal_row, self.goal_col)

    def get_path(self, grow, gcol):
        self.goal_col, self.goal_row = gcol, grow
        self.pathx, self.pathy = a_star_alg(self.col, self.row, gcol, grow, self.obs_row, self.obs_col,
                                            self.matrix_size, self.rob_size)

    def update(self):

        self.sight()
        if self.row == self.goal_row and self.col == self.goal_col:
            if self.row == self.prow1 and self.col == pcol1:
                self.get_path(self.prow2, self.pcol2)
            elif self.row == self.prow1 and self.col == pcol1:
                self.get_path(self.prow1, self.pcol1)
            else:
                self.get_path(self.prow1, self.pcol1)
            self.col = self.pathx.pop()
            self.row = self.pathy.pop()
            self.ph.rect.centerx = self.col * 64
            self.ph.rect.centery = self.row * 64
            self.rect = self.ph.rect
        elif self.row != self.goal_row and self.col != self.goal_col:
            self.col = self.pathx.pop()
            self.row = self.pathy.pop()
            self.ph.rect.centerx = self.col * 64
            self.ph.rect.centery = self.row * 64
            self.rect = self.ph.rect

    def blitme(self):
        self.ph.blitme()

    def sight(self):
        if self.player.row == self.row:
            if player.col < self.col:
                for x in range(player.col, self.col):
                    if self.level.rows[self.row][x] == 'M':
                        return false
                self.get_path(player.row, player.col)

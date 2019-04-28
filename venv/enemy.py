import a_star

class Guard:
    def __init__(self, row, col, pat1, pat2, player):
        self.row = row
        self.col = col

        self.goal_col = 13  # [m]
        self.goal_row = 9.0  # [m]
        self.matrix_size = 1.0  # [m]
        self.rob_size = 0.0  # [m]
        self.prepare()
        self.pathx, self.pathy = [], []
        self.ph = PhotoRect(self.screen, self.filename + self.dir + '_' + str(self.state), 18, 18)
        self.rect = self.ph.rect


    def prepare(self):
        obs_col, obs_row = [], []

        for i in range(13):
            obs_col.append(i)
            obs_row.append(0.0)
        for i in range(13):
            obs_col.append(13.0)
            obs_row.append(i)
        for i in range(14):
            obs_col.append(i)
            obs_row.append(13.0)
        for i in range(14):
            obs_col.append(0.0)
            obs_row.append(i)

        #
        # for i in range(50):
        #     obs_col.append(i)
        #     obs_row.append(0.0)
        # for i in range(50):
        #     obs_col.append(50.0)
        #     obs_row.append(i)
        # for i in range(51):
        #     obs_col.append(i)
        #     obs_row.append(50.0)
        # for i in range(51):
        #     obs_col.append(0.0)
        #     obs_row.append(i)
        #

        #######################################################
        for i in range(1):
            obs_col.append(12)
            obs_row.append(i + 7)
        #######################################################
        for i in range(1):
            obs_col.append(11)
            obs_row.append(i + 11)

        for i in range(4):
            obs_col.append(11)
            obs_row.append(i + 2)
        #######################################################
        for i in range(1):
            obs_col.append(10)
            obs_row.append(i + 11)
        for i in range(1):
            obs_col.append(10)
            obs_row.append(i + 9)
        for i in range(4):
            obs_col.append(10)
            obs_row.append(i + 2)

        ######################################################
        for i in range(1):
            obs_col.append(9)
            obs_row.append(i + 11)

        for i in range(1):
            obs_col.append(9)
            obs_row.append(i + 9)

        #######################################################

        for i in range(4):
            obs_col.append(8)
            obs_row.append(i + 4)

        for i in range(1):
            obs_col.append(8)
            obs_row.append(i + 2)
        ########################################################
        for i in range(1):
            obs_col.append(7)
            obs_row.append(i + 11)

        for i in range(1):
            obs_col.append(7)
            obs_row.append(i + 9)

        for i in range(1):
            obs_col.append(7)
            obs_row.append(i + 6)

        for i in range(1):
            obs_col.append(7)
            obs_row.append(i + 2)

        #######################################################

        for i in range(1):
            obs_col.append(6)
            obs_row.append(i + 11)

        for i in range(1):
            obs_col.append(6)
            obs_row.append(i + 9)

        for i in range(1):
            obs_col.append(6)
            obs_row.append(i + 6)

        for i in range(1):
            obs_col.append(6)
            obs_row.append(i + 2)

        #########################################################

        for i in range(4):
            obs_col.append(5)
            obs_row.append(i + 4)

        for i in range(1):
            obs_col.append(5)
            obs_row.append(i + 2)
        #########################################################

        for i in range(1):
            obs_col.append(4)
            obs_row.append(i + 11)
        for i in range(1):
            obs_col.append(4)
            obs_row.append(i + 9)

        ##########################################################

        for i in range(1):
            obs_col.append(3)
            obs_row.append(i + 11)

        for i in range(1):
            obs_col.append(3)
            obs_row.append(i + 9)

        for i in range(4):
            obs_col.append(3)
            obs_row.append(i + 2)

        ##########################################################

        for i in range(1):
            obs_col.append(2)
            obs_row.append(i + 11)

        for i in range(4):
            obs_col.append(2)
            obs_row.append(i + 2)

        ##########################################################

        for i in range(1):
            obs_col.append(1)
            obs_row.append(i + 7)


    def get_path(self, grow, gcol):
        self.goal_col, self.goal_row = gcol, grow
        self.pathx, self.pathy = a_star_alg(self.col, self.row, gcol, grow, self.matrix_size, self.rob_size)


    def move(self):
        if self.row == self.goal_row and self.col == self.goal_col:
            if self.row == self.prow1 and self.col == pcol1:
                self.get_path(self.prow2, self.pcol2)
            if self.row == self.prow1 and self.col == pcol1:
                self.get_path(self.prow1, self.pcol1)
            else:
                GetPath(self.CurrentPosition, self.GoalPos)
        elif self.row != self.goal_row and self.col != self.goal_col:
            self.col = self.pathx.pop()
            self.row = self.pathy.pop()
            self.ph.rect.centerx = self.col * 64
            self.ph.rect.centery = self.row * 64
            self.rect = self.ph.rect



    def seen(self, prow, pcol):


        self.GoalPos = player position
        self.Path = A_Star(self.CurrentPosition, self.GoalPos)




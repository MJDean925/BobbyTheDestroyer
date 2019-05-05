from pygame.sprite import Sprite
from photo_rect import PhotoRect
import pygame


class Player(Sprite):

    def __init__(self, screen, row, col, maze):
        super(Player, self).__init__()
        self.screen = screen
        self.s_rect = screen.get_rect()
        self.im = PhotoRect(screen, "character\\character_up\\character_up_1", 64, 64)

        self.im.rect.centerx = col*64 + 32
        self.im.rect.centery = row*64 + 32
        self.maze = maze
        self.rect = self.im.rect
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        self.speed = 64
        self.state = 1
        self.death_state = 1
        self.dir = "right"
        self.speed_timer = pygame.time.get_ticks()
        self.row = row
        self.col = col
        self.walls = ['T', 'B', 'R', 'L', 'G', 'M', 'N', 'O', 'Y', 'Z', 'W', 'X', 'S']
        self.dead = False
        self.sound_timer = pygame.time.get_ticks()
        self.finished = False

    def update(self):
        temp = ""
        if not self.dead:
            if self.moving_up and pygame.time.get_ticks() - self.speed_timer >= 100:

                temp = self.maze.rows[self.row-1]
                val = temp[self.col]
                if val not in self.walls:
                    self.im.rect.y -= self.speed
                    self.row -= 1
                self.im.blitme()
                self.speed_timer = pygame.time.get_ticks()
                self.dir = 'up'
                temp = "character\\character_up\\character_up_" + str(self.state)
            elif self.moving_down and pygame.time.get_ticks() - self.speed_timer >= 100:

                temp = self.maze.rows[self.row+1]
                val = temp[self.col]
                if val not in self.walls:
                    self.row += 1
                    self.im.rect.y += self.speed
                self.im.blitme()
                self.speed_timer = pygame.time.get_ticks()
                self.dir = 'down'
                temp = "character\\character_down\\character_down_" + str(self.state)
            elif self.moving_right and pygame.time.get_ticks() - self.speed_timer >= 100:

                temp = self.maze.rows[self.row]
                if self.col < 27:
                    val = temp[self.col+1]
                else:
                    val = temp[0]
                if val not in self.walls:
                    self.im.rect.x += self.speed
                    self.col += 1
                self.im.blitme()
                self.speed_timer = pygame.time.get_ticks()
                self.dir = 'right'
                temp = "character\\character_right\\character_right_" + str(self.state)
            elif self.moving_left and pygame.time.get_ticks() - self.speed_timer >= 100:

                temp = self.maze.rows[self.row]
                val = temp[self.col-1]
                if val not in self.walls:
                    self.im.rect.x -= self.speed
                    self.col -= 1
                self.im.blitme()
                self.speed_timer = pygame.time.get_ticks()
                self.dir = 'left'
                temp = "character\\character_left\\character_left_" + str(self.state)
            elif not (self.moving_left or self.moving_right or self.moving_up or self.moving_down) \
                    and pygame.time.get_ticks() - self.speed_timer >= 100:
                temp = "character\\character_" + self.dir + "\\character_" + self.dir + "_1"
                self.state = 1
            else:
                return temp

            self.rect = self.im.rect
            self.im = PhotoRect(self.screen, temp, 64, 64)
            self.im.rect = self.rect
            if self.state >= 6:
                self.state = 1
            else:
                self.state += 1
        else:
            self.finished = True

    def blitme(self):
        self.im.blitme()

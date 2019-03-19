import pygame
import sys


class GameLoop:

    def __init__(self, player, gamelevel):

        self.finished = False
        self.won = False
        self.player = player
        self.gamelevel = gamelevel
        self.counter = 1

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = True
            self.player.moving_left = False
            self.player.moving_up = False
            self.player.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = True
            self.player.moving_right = False
            self.player.moving_up = False
            self.player.moving_down = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = True
            self.player.moving_left = False
            self.player.moving_down = False
            self.player.moving_right = False

        elif event.key == pygame.K_DOWN:
            self.player.moving_down = True
            self.player.moving_left = False
            self.player.moving_right = False
            self.player.moving_up = False

        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.player.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.player.moving_left = False
        elif event.key == pygame.K_UP:
            self.player.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.player.moving_down = False



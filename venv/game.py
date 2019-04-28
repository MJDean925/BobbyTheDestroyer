import pygame
from GameLoop import GameLoop
from Level import Level
from Player import Player
import os
from pygame.sprite import Group
from enemy import Guard
from bomb import Bomb


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((896, 896))
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 25)
        self.won = False
        self.lost = False
        pygame.display.set_caption("AI game")
        self.clock = pygame.time.Clock()
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'maze.txt')
        self.level = Level(self.screen, my_file)
        self.player = Player(self.screen, 1, 1, self.level)
        self.guard = Guard(self.screen, 2, 1, self.player, self.level)
        self.bomb = Bomb(screen, 3, 5, self.player, self.guard)
        self.game_active = True

    def update_screen(self):

        self.screen.fill(Game.BLACK)
        if self.game_active:

            self.level.blitme()

            self.player.update()
            self.player.blitme()
            # self.guard.update()
            # self.guard.blitme()

        pygame.display.flip()

    def play(self):
        loop = GameLoop(self.player, self.level)

        while not loop.finished:
            loop.check_events()
            self.update_screen()
            self.clock.tick(60)
            self.won = loop.won


game = Game()
game.play()


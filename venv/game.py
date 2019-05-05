import pygame
from GameLoop import GameLoop
from Level import Level
from Player import Player
import os
from pygame.sprite import Group
from enemy import Guard
from photo_rect import PhotoRect
from bomb import Bomb


class Game:
    BLACK = (47, 47, 47)

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((896, 896))
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 25)
        self.won = False
        self.lost = False
        pygame.display.set_caption("Bobby The Destroyer")
        self.clock = pygame.time.Clock()
        this_folder = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(this_folder, 'maze_old.txt')
        self.level = Level(self.screen, my_file)
        self.player = Player(self.screen, 1, 1, self.level)
        self.guard = Guard(self.screen, 12, 1, self.player, self.level)
        self.bombs = []
        self.numfin = 0
        self.bombs.append(Bomb(self.screen, 3, 5, self.player, self.guard))
        self.bombs.append(Bomb(self.screen, 3, 8, self.player, self.guard))
        self.bombs.append(Bomb(self.screen, 10, 7, self.player, self.guard))
        self.bombs.append(Bomb(self.screen, 10, 6, self.player, self.guard))
        self.bombs.append(Bomb(self.screen, 12, 2, self.player, self.guard))
        self.bombs.append(Bomb(self.screen, 12, 10, self.player, self.guard))
        self.bombs.append(Bomb(self.screen, 7, 3, self.player, self.guard))
        self.bombs.append(Bomb(self.screen, 7, 10, self.player, self.guard))
        self.game_active = True
        self.bg = PhotoRect(self.screen, "background", 896, 896)

    def update_screen(self):

        self.screen.fill(Game.BLACK)
        if self.player.finished:
            self.game_active = False
        elif self.numfin == 8:
            self.game_active = False
            surface = self.font.render("YOU WIN!", True, (255, 255, 255))
            text_rect = surface.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centerx))
            self.screen.blit(surface, text_rect)
        if self.game_active:
            self.bg.blitme()
            self.level.blitme()

            self.player.update()
            self.player.blitme()
            self.guard.sight()  # added this
            self.guard.update()
            self.guard.blitme()
            for b in self.bombs:
                b.boom()
                b.blitme()
                if b.finished:
                    self.numfin += 1
                    self.bombs.remove(b)

        elif self.player.dead:
            surface = self.font.render("GAME OVER", True, (255, 255, 255))
            text_rect = surface.get_rect(center=(self.screen_rect.centerx, self.screen_rect.centerx))
            self.screen.blit(surface, text_rect)

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

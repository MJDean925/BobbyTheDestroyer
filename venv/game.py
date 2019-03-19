import pygame
from GameLoop import GameLoop
from Level import Level

from pygame.sprite import Group


class Game:
    BLACK = (0, 0, 0)

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((280, 360))
        self.screen_rect = self.screen.get_rect()
        self.font = pygame.font.Font(None, 50)
        self.font2 = pygame.font.Font(None, 25)
        self.won = False
        self.lost = False
        pygame.display.set_caption("Pacman Portal")
        self.clock = pygame.time.Clock()
        self.level = Level(self.screen, 'levelfile1.txt')
        self.player = Player(self.screen, 25, 13, self.level)
        self.game_active =True

    def update_screen(self):

        self.screen.fill(Game.BLACK)
        if self.game_active:

            self.level.blitme()

            self.player.update()
            self.player.blitme()

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


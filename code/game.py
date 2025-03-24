#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame

from code import score
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.credits import Credits
from code.level import Level
from code.menu import Menu
from code.player import Player
from code.score import Score


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            if menu_return == MENU_OPTION[0]:
                player_score = [0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                player_score = level_return
                player = None
                for ent in level.entity_list:
                    if ent.name == "Player1":
                         player = ent
                         break
                if player:
                    score_instance = Score(self.window)
                    score_instance.show(menu_return, player_score, player)
                else:
                    print('End game')

            elif menu_return == MENU_OPTION[1]:
                credits = Credits(self.window)
                credits_return = credits.run()
            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()

            else:
                pass

#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.enemy import Enemy
from code.player import Player
import random

from code.prize import Prize


class EntityFactory:
    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Bg0':
                list_bg = []
                for i in range(5):
                    list_bg.append(Background(f'Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2))
            case 'Enemy2':
                return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(30, WIN_HEIGHT - 40)))
            case 'Prize1':
                return Prize('Prize1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'Prize2':
                return Prize('Prize2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))


#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.background import Background
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player


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
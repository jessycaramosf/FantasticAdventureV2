#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface

from code import entityFactory
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name: str, menu_option: tuple):
        self.window = window
        self.name: name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Bg0'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()



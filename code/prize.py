#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Prize(Entity):
    def __init__(self, name: str, position: tuple, score_value= int):
        super().__init__(name, position)



        
    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left = WIN_WIDTH

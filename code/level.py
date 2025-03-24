#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from random import choice

import pygame
import random
from pygame import Surface, Rect
from pygame.font import Font

from code import entityFactory
from code.EntityMediator import EntityMediator
from code.const import WIN_HEIGHT, C_YELLOW, C_PURPLE, EVENT_TIME, SPAWN_TIME
from code.entity import Entity
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window: Surface, name: str, menu_option: tuple):
        self.timeout = 30000
        self.name = name
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Bg0'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        pygame.time.set_timer(EVENT_TIME, SPAWN_TIME)

    def run(self):
        pygame.mixer_music.load('./assets/Music2.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_TIME:
                    choice = random.choice(('Prize1', 'Prize2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIME:
                    self.entity_list.append(EntityFactory.get_entity('Enemy2'))

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_PURPLE, (15, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_YELLOW, (15, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_YELLOW, (15, WIN_HEIGHT - 20))
            self.level_text(14, f'Player1 - Health  | Score: ', C_PURPLE, (15, 25))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

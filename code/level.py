#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

import pygame
import random
from pygame import Surface, Rect
from pygame.font import Font

from code.EntityMediator import EntityMediator
from code.const import WIN_HEIGHT, C_YELLOW, EVENT_TIME, SPAWN_TIME, C_WHITE, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_END
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window: Surface, name: str, menu_option: tuple, player_score: list[int]):
        self.timeout = TIMEOUT_END
        self.name = name
        self.window = window
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Bg0'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_TIME, SPAWN_TIME)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
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
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player):
                                player_score[0] = ent.score
                        return True

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    return False

            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_WHITE, (15, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_YELLOW, (15, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_YELLOW, (15, WIN_HEIGHT - 20))
            for ent in self.entity_list:
                if ent.name == 'Player1':
                    self.level_text(14, f'Player1 - Health:{ent.health} | Score:{ent.score}', C_WHITE, (15, 25))

            pygame.display.flip()

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Segoe UI Black", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

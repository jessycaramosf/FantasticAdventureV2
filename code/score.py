import sys

import pygame
from pygame import Surface, Rect, K_ESCAPE
from pygame.font import Font

from code.const import C_ORANGE, WIN_WIDTH, C_YELLOW, WIN_HEIGHT, SCORE_POS



class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/Credits.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def show(self, menu_return, player_score: list[int], player):
        pygame.mixer_music.load('./assets/Music1.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        while True:

            self.score_text(60, 'YOU WIN!', C_ORANGE, SCORE_POS['Title'])
            self.score_text(50, f'Score: {player.score}', C_YELLOW, (WIN_WIDTH / 2, WIN_HEIGHT / 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

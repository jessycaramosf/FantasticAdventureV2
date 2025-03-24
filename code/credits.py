import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_ORANGE, WIN_WIDTH, C_WHITE, C_CYAN, C_BLACK, C_PURPLE, C_YELLOW


class Credits:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pygame.image.load('./assets/Credits.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./assets/Music1.mp3')
        pygame.mixer_music.play(-1)

        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.credit_text(50, 'Créditos', C_ORANGE, (WIN_WIDTH / 2, 60))
            self.credit_text(18, 'Criado por: Jéssyca. C. R. Ferreira - RA: 4545764', C_YELLOW,
                           (WIN_WIDTH / 2, 120))
            self.credit_text(14, 'Musica 1: Mars uk Drill instrumental, Por: prazkhanal - '
                                 'Fonte: Freesound.org', C_YELLOW, (WIN_WIDTH / 2, 150))
            self.credit_text(14, 'Musica 2: Musical Composition Por: flavioconcini - '
                                 'Fonte: Freesound.org', C_YELLOW,
                             (WIN_WIDTH / 2, 180))
            self.credit_text(14, 'Imagens Coletadas em CRAFTPIX.NET', C_YELLOW,
                             (WIN_WIDTH / 2, 210))
            self.credit_text(18, 'OBRIGADA POR JOGAR!!!', C_YELLOW,
                             (WIN_WIDTH / 2, 250))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.flip()

    def credit_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
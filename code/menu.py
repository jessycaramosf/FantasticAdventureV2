import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import C_WHITE, WIN_WIDTH, C_GREEN, MENU_OPTION


class Menu:
    def __init__(self, window: Surface):
        self.window = window
        # self.name = name
        self.surf = pygame.image.load('./assets/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer_music.load('./assets/Music1.mp3')
        pygame.mixer_music.play(-1)

        while True:

            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, 'Fantastic', C_WHITE, (WIN_WIDTH / 2, 85))
            self.menu_text(50, 'Adventure', C_WHITE, (WIN_WIDTH / 2, 130))
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(35, MENU_OPTION[i], C_GREEN, (WIN_WIDTH / 2, 180 + 40*i))
                   
                else:
                    self.menu_text(35, MENU_OPTION[i], C_WHITE, (WIN_WIDTH / 2, 180 + 40*i))


            pygame.display.flip()

            # Close Window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Comic Sans", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

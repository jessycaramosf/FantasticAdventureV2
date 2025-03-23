# C
import pygame

C_WHITE = (255,255,255)
C_GREEN = (0,176,0)
C_PURPLE = (128, 0, 128)
C_YELLOW = (255,255,128)
C_ORANGE = (255, 128, 0)
C_CYAN = (0, 128, 128)

# E
ENTITY_SPEED = {
    'Bg0': 0,
    'Bg1': 1,
    'Bg2': 2,
    'Bg3': 3,
    'Bg4': 3,
    'Player1': 3,
    'Enemy1': 1,
    'Enemy2': 2,
    'Prize1': 1,
    'Prize2': 2,
    }

EVENT_ENEMY = pygame.USEREVENT + 1


# M

MENU_OPTION = ('Play',
               'Score',
               'Exit'
               )



# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL}

# S

SPAWN_TIME = 6000

#W

WIN_WIDTH = 576
WIN_HEIGHT = 324
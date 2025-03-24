# C
import pygame

C_WHITE = (255,255,255)
C_GREEN = (0,176,0)
C_PURPLE = (255, 0, 255)
C_YELLOW = (255,255,128)
C_ORANGE = (255, 128, 0)
C_CYAN = (0, 128, 128)
C_BLACK = (0, 0, 0)

# E
ENTITY_SPEED = {
    'Bg0': 1,
    'Bg1': 1,
    'Bg2': 2,
    'Bg3': 3,
    'Bg4': 3,
    'Player1': 3,
    'Enemy1': 1,
    'Enemy2': 1,
    'Prize1': 1,
    'Prize2': 2,
    }


ENTITY_DAMAGE = {
    'Bg0': 0,
    'Bg1': 0,
    'Bg2': 0,
    'Bg3': 0,
    'Bg4': 0,
    'Player1': 1,
    'Enemy2': 40,
    'Prize1': 0,
    'Prize2': 0,
 }

ENTITY_SCORE = {
    'Bg0': 0,
    'Bg1': 0,
    'Bg2': 0,
    'Bg3': 0,
    'Bg4': 0,
    'Player1': 0,
    'Enemy2': 0,
    'Prize1': 50,
    'Prize2': 70,
}

ENTITY_HEALTH = {
    'Bg0': 999,
    'Bg1': 999,
    'Bg2': 999,
    'Bg3': 999,
    'Bg4': 999,
    'Player1': 300,
    'Enemy2': 1,
    'Prize1': 1,
    'Prize2': 1,
}

EVENT_TIME = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

# M

MENU_OPTION = ('Play',
               'Credits',
               'Exit'
               )



# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RCTRL}

# S

SPAWN_TIME = 3000
SCREEN_DELAY = 3000

# T
TIMEOUT_STEP = 100
TIMEOUT_END = 30000

#W

WIN_WIDTH = 576
WIN_HEIGHT = 324

# SP

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 50),
    'Label': (WIN_WIDTH / 2, 90),
    0: (WIN_WIDTH / 2, 110),
}
# M
import pygame

MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'EXIT')

# C
COLOR_PURPLE = (64, 0, 128)
COLOR_BLACK = (0, 0, 0)
COLOR_YELLOW = (255, 255, 128)

# W
WIN_WIDTH = 1152
WIN_HEIGHT = 648

# E
EVENT_ENEMY = pygame.USEREVENT + 1
ENTITY_SPEED = {'Level1Bg0': 1.2,
                'Level1Bg1': 2,
                'Level1Bg2': 3,
                'Player1': 6,
                'Player2': 6,
                'Enemy1': 4.5,
                'Enemy2': 2}

# P
PLAYER_KEY_UP = {'Player1': pygame.K_w,
                 'Player2': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player1': pygame.K_s,
                   'Player2': pygame.K_DOWN}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_d,
                    'Player2': pygame.K_RIGHT}
PLAYER_KEY_LEFT = {'Player1': pygame.K_a,
                   'Player2': pygame.K_LEFT}

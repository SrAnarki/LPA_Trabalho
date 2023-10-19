#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Code.Const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH
from Code.Entity import Entity


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_w] and self.rect.top > 2:  # Se a tecla 'W' foi pressionada
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_s] and self.rect.bottom < WIN_HEIGHT:  # Se a tecla 'S' foi pressionada
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_d] and self.rect.right < WIN_WIDTH:  # Se a tecla 'D' foi pressionada
            self.rect.centerx += ENTITY_SPEED[self.name]

        if pressed_key[pygame.K_a] and self.rect.left > 0:  # Se a tecla 'A' foi pressionada
            self.rect.centerx -= ENTITY_SPEED[self.name]

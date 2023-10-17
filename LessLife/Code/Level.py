#!/usr/bin/python
# -*- coding: utf-8 -*-
from Code import Entity


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.name = name
        self.mode = menu_option  # Opção do menu
        self.entity_list = list[Entity] = []

    def run(self, ):
        pass

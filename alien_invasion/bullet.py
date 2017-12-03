# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблём"""
    def __init__(self, ai_settings, screen, ship):
        """Создаёт объект пули в текущей позиции корабля"""
        super(Bullet, self).__init__()
        self.screen = screen

        # Создание пули в позиции (0,0) и назначение правильной позиции.

        self.rect = pygame.Rect(0,0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top


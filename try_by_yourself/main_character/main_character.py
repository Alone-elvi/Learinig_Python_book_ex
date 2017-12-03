# -*- coding: utf-8 -*-

import pygame


class MainCharacter():
    def __init__(self, screen):

        self.screen = screen

        self.screen_width = 120
        self.screen_height = 120
        self.bg_color = (102, 178, 255)
        self.image = pygame.image.load('./main_character/images/raskraski-uchenyj.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

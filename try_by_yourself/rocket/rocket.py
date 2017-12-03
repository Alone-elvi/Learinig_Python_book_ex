# -*- coding: utf-8 -*-

import pygame


class Rocket():
    def __init__(self, ai_settings, screen):
        self.screen = screen

        self.image = pygame.transform.scale(pygame.image.load('./images/Marketplace_Rocket_Sculpture-icon.png')
                                            .convert_alpha(), (ai_settings.rocket_width, ai_settings.rocket_height))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        self.moving_right = False
        self.moving_left = False

        self.moving_up = False
        self.moving_down = False

        self.ai_settings = ai_settings

    def update(self):
        """Обновляет позицию корабля с учётом флага"""
        # Обновляется атрибут center, не rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.rocket_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.rocket_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.rocket_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.rocket_speed_factor
        # Обновление атрибута rect на основании self.center.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

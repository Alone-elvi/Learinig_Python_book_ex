# -*- coding: utf-8 -*-

import sys
import pygame

from settings import Settings
from rocket import Rocket

import functions as gf


def run_discovery():
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height
    ))
    pygame.display.set_caption("Rocket Discovery")

    # Создание корабля.
    rocket = Rocket(ai_settings, screen)

    # Запуск основного цикла игры.
    while True:
        gf.check_events(rocket)
        rocket.update()
        gf.update_screen(ai_settings, screen, rocket)


run_discovery()

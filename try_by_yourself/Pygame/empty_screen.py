# -*- coding: utf-8 -*-

import sys
import pygame

def run_empty_screen():
    screen_width = 1200
    screen_height = 900
    bg_color = (102, 178, 255)

    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)

run_empty_screen()
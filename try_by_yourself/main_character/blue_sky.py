# -*- coding: utf-8 -*-

import sys
import pygame

from try_by_yourself.main_character.main_character import MainCharacter

def blue_sky():
    pygame.init()
    screen_b = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Blue Sky')
    bg_color = (102, 178, 255)
    main_character = MainCharacter(screen_b)
    while True:
        screen_b.fill(bg_color)
        main_character.blitme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


blue_sky()

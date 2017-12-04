# -*- coding: utf-8 -*-


class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 900
        self.bg_color = (102, 178, 255)

        self.rocket_width = 120
        self.rocket_height = 120

        self.rocket_speed_factor = 2

        # Пуля
        self.bullet_width = 1
        self.bullet_height = 15
        self.bullet_speed_factor = 1
        self.bullet_color = 255, 0, 0

        # Разрешенное количество пуль на экране
        self.bullet_allowed = 3


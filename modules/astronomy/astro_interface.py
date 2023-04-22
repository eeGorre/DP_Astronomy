import pygame as pg
from settings import WIN_WIDTH, WIN_HEIGHT
import time
from handler import process_input_text

class Astro_Interface:
    def __init__(self, obj):
        self.objects = obj
        self.fnt452645126 = pg.font.SysFont('Arial', 14)

    def obj_name(self, screen, camera):    
        for obj in self.objects:
            planet_name = self.fnt452645126.render(obj.name, 1, (255, 255, 255))
            screen.blit(planet_name, ((obj.x + obj.radius) * camera.zoom_level - camera.rect.x, (obj.y - obj.radius) * camera.zoom_level - camera.rect.y))

            
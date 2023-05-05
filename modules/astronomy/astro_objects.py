import pygame as pg
from settings import WIN_HEIGHT, WIN_WIDTH
from math import sqrt

class AstroObjects:
    def __init__(self, x, y, name, m, vx, vy, radius, obj_type, color):
        self.name = name
        self.m = m
        self.vx = vx
        self.vy = vy
        self.x = x
        self.y = y
        self.radius = radius
        self.trace = []
        self.color = color
        self.selected = False
        self.parent = None
        self.obj_type = obj_type
        self.G = 6.67 * (10**-11)
        self.fcv = sqrt(self.G*(self.m/self.radius))
        self.scv = sqrt(2) * (sqrt(self.G*(self.m/self.radius)))
        
        
    def render(self, screen, camera, mouse_pos, event):
        if self.radius*camera.e <= 3:
            if self.obj_type == 'Star':
                radius = 3
            if self.obj_type == 'Planet':
                radius = 2
            if self.obj_type == 'Satellite':
                radius = 1
            if self.obj_type == 'Asteroid':
                radius = 1
            if self.obj_type == None:
                radius = 1
        else:
            radius = self.radius*camera.e
            
        pg.draw.circle(screen, self.color,
                       (self.x*camera.e - camera.Ox, self.y*camera.e - camera.Oy),
                       (radius))

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if (self.x*camera.e - camera.Ox) - (radius * 3) <= mouse_pos[0] <= (self.x*camera.e - camera.Ox) + (radius * 3) and (self.y*camera.e - camera.Oy) - (radius * 3) <= mouse_pos[1] <= (self.y*camera.e - camera.Oy) + (radius * 3):
                self.selected = True
                pg.time.wait(200)
            else:
                self.selected = False
            
        if self.selected:
            if self.selected:
                target_pos = (self.x*camera.e - WIN_WIDTH // 2, self.y*camera.e - WIN_HEIGHT // 2)
                t = 0.03  # можно изменять значение для изменения скорости анимации
                current_pos = (camera.Ox, camera.Oy)
                new_pos = tuple((1 - t) * current + t * target for current, target in zip(current_pos, target_pos))
                camera.Ox, camera.Oy = new_pos  
                
    def isSatellite(self):
        if self.parent is None:
            return False
        elif self.parent.obj_type == "Planet":
            return True
        else:
            return False

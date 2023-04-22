import pygame as pg
from math import sqrt
from settings import WIN_HEIGHT, WIN_WIDTH
class AstroObjects:
    def __init__(self, x, y, name, m, vx, vy, radius, color):
        self.name = name

        self.m = m
        self.vx = vx
        self.vy = vy
        
        self.x = x
        self.y = y
        
        self.radius = radius
        
        self.past_positions = []
        
        self.color = color
        
        self.selected = False
        
    def render(self, screen, camera, mouse_pos, event):
        
        if self.radius*camera.e1 <= 3:
            radius = 4
        else:
            radius = self.radius*camera.e1
        pg.draw.circle(screen, self.color,
                       (self.x*camera.zoom_level - camera.rect.x, self.y*camera.zoom_level - camera.rect.y),
                       (radius))

        if event.type == pg.MOUSEBUTTONUP:
            if (self.x*camera.zoom_level - camera.rect.x) <= mouse_pos[0] <= (self.x*camera.zoom_level - camera.rect.x) + (radius * 15) * 2 and (self.y*camera.zoom_level - camera.rect.y) <= mouse_pos[1] <= (self.y*camera.zoom_level - camera.rect.y) + (radius * 15) * 2:
                self.selected = True
            else:
                self.selected = False
        
        if self.selected:
            camera.rect.x = (self.x*camera.zoom_level - WIN_WIDTH // 2)
            camera.rect.y = (self.y*camera.zoom_level - WIN_HEIGHT // 2)
            # camera.rect.x = self.x*camera.zoom_level
            # camera.rect.y = self.y*camera.zoom_level
        print(self.selected)            
        
        self.past_positions.append((self.x, self.y))
        self.draw_trajectory(screen, camera, self.past_positions)
        
    @staticmethod
    def draw_trajectory(screen, camera, positions):
        for i in range(1, len(positions), 100):
            x1, y1 = positions[i-1]
            x2, y2 = positions[i]
            x1 = x1 * camera.zoom_level - camera.rect.x
            y1 = y1 * camera.zoom_level - camera.rect.y
            x2 = x2 * camera.zoom_level - camera.rect.x
            y2 = y2 * camera.zoom_level - camera.rect.y
            pg.draw.line(screen, (200, 200, 200), (x1, y1), (x2, y2), 3)

        
    def __str__(self):
        return self.name
    
    def __del__(self):
        print(self, 'удалён.')
        
        
        
        

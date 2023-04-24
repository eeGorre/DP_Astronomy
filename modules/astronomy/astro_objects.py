import pygame as pg
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
        self.trace = []
        self.color = color
        self.selected = False
        
        
    def render(self, screen, camera, mouse_pos, event):
        if self.radius*camera.e <= 3:
            radius = 2
        else:
            radius = self.radius*camera.e
            
        pg.draw.circle(screen, self.color,
                       (self.x*camera.e - camera.x, self.y*camera.e - camera.y),
                       (radius))

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            if (self.x*camera.e - camera.x) - 100 <= mouse_pos[0] <= (self.x*camera.e - camera.x) + (radius * 5) * 2 and (self.y*camera.e - camera.y) - 100 <= mouse_pos[1] <= (self.y*camera.e - camera.y) + (radius * 5) * 2:
                self.selected = True
                pg.time.wait(100)
            else:
                self.selected = False
            
        
        if self.selected:
            camera.x = (self.x*camera.e - WIN_WIDTH // 2)
            camera.y = (self.y*camera.e - WIN_HEIGHT // 2)        
        
        self.draw_trajectory(screen, camera, self.trace)
        
    def draw_trajectory(self, screen, camera, positions):
        self.trace.append((self.x, self.y))
        if len(self.trace) < 5000:
            for i in range(1, len(positions), 100):
                x1, y1 = positions[i-1]
                x1 = x1 * camera.e - camera.x
                y1 = y1 * camera.e - camera.y
                pg.draw.circle(screen, (60, 60, 60), (x1, y1), 1)
        else:
            del self.trace[:100]
            
import pygame as pg
from settings import WIN_WIDTH, WIN_HEIGHT

class Camera:
    def __init__(self):
        self.zoom_level = 0.000000002
        self.x = -WIN_WIDTH / 2
        self.y = -WIN_HEIGHT / 2
        self.e1 = self.zoom_level
        self.e2 = self.zoom_level
        self.rect = pg.Rect(self.x, self.y, 0, 0)
        
        self.y_pos = 0
        self.x_pos = 0

    def move(self):
        mouse_rel_pos = list(pg.mouse.get_rel())
        if pg.mouse.get_pressed()[0]:
            x = mouse_rel_pos[0]
            y = mouse_rel_pos[1]
            self.x = self.rect.x
            self.y = self.rect.y
            self.rect.x -= x
            self.rect.y -= y
            
    def zoom(self, event, keys, mouse_pos):
        if keys[pg.K_0]:
            x_pos = self.rect.x = -WIN_WIDTH // 2
            y_pos = self.rect.y = -WIN_HEIGHT // 2
 
        x_pos = (mouse_pos[0] + self.x) / 4
        y_pos = (mouse_pos[1] + self.y) / 4
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                self.rect.x += x_pos
                self.rect.y += y_pos
                self.zoom_level *= 1.0625
                self.e1 = self.zoom_level
                self.e2 = self.zoom_level
                self.rect.x += x_pos * self.zoom_level
                self.rect.y += y_pos * self.zoom_level
                
            if event.button == 5:
                self.rect.x += x_pos
                self.rect.y += y_pos
                self.zoom_level /= 1.0625
                self.e1 = self.zoom_level
                self.e2 = self.zoom_level
                self.rect.x +=  x_pos * self.zoom_level
                self.rect.y += y_pos * self.zoom_level
import pygame as pg
from settings import WIN_WIDTH, WIN_HEIGHT

class Camera:
    def __init__(self):
        self.e = 0.000000002
        self.x = -WIN_WIDTH // 2
        self.y = -WIN_HEIGHT // 2

    def move(self, mouse_rel_pos):
        if pg.mouse.get_pressed()[0]:
            self.x -= mouse_rel_pos[0]
            self.y -= mouse_rel_pos[1]
    
    def zoom(self, event, keys, mouse_pos):
        if keys[pg.K_0]:
            self.x = x_pos = -WIN_WIDTH // 2
            self.y = y_pos = -WIN_HEIGHT // 2
        
        
        if event.type == pg.MOUSEBUTTONDOWN and not keys[pg.K_t]:
            x_pos = event.pos[0]
            y_pos = event.pos[1]
            if event.button == 4:
                self.e *= 1.0625
                self.x += x_pos - WIN_WIDTH // 2
                self.y += y_pos - WIN_HEIGHT // 2
                
            if event.button == 5:
                self.e /= 1.0625
                self.x += x_pos - WIN_WIDTH // 2 
                self.y += y_pos - WIN_HEIGHT // 2


    
    
    
    # def zoom(self, event, keys, mouse_pos):
    #     if keys[pg.K_0]:
    #         self.x = x_pos = -WIN_WIDTH // 2
    #         self.y = y_pos = -WIN_HEIGHT // 2
        
        
    #     if event.type == pg.MOUSEBUTTONDOWN and not keys[pg.K_t]:
    #         x_pos = event.pos[0] + self.x
    #         y_pos = event.pos[1] + self.y
    #         if event.button == 4:
    #             self.e *= 1.0625
    #             self.x = x_pos - WIN_WIDTH // 2
    #             self.y = y_pos - WIN_HEIGHT // 2
                
    #         if event.button == 5:
    #             self.e /= 1.0625
    #             self.x = x_pos - WIN_WIDTH // 2
    #             self.y = y_pos - WIN_HEIGHT // 2
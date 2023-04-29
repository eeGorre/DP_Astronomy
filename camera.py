import pygame as pg
from settings import WIN_WIDTH, WIN_HEIGHT

class Camera:
    def __init__(self):
        self.k = 1.2 # Zoom ratio
        self.n = -120 # Zoom_step
        self.e = self.k**self.n
        self.Ox = -WIN_WIDTH // 2
        self.Oy = -WIN_HEIGHT // 2

    def move(self, mouse_shift):
        if pg.mouse.get_pressed()[0]:
            self.Ox -= mouse_shift[0]
            self.Oy -= mouse_shift[1]
    
    def zoom(self, event, keys, mouse_S):
        self.m_wx = (mouse_S[0] + self.Ox) / self.e  #позиция мыши в мире W = S + O
        self.m_wy = (mouse_S[1] + self.Oy) / self.e

        if keys[pg.K_0]:
            self.Ox = -WIN_WIDTH // 2
            self.Oy = -WIN_HEIGHT // 2
        
        if event.type == pg.MOUSEBUTTONDOWN and not keys[pg.K_t]:
            if event.button == 4:
                self.n += 0.5
                self.e = self.k**self.n
                self.Ox = self.e*self.m_wx - mouse_S[0]
                self.Oy = self.e*self.m_wy - mouse_S[1]
                
            if event.button == 5:
                self.n -= 0.5
                self.e = self.k**self.n
                self.Ox = self.e*self.m_wx - mouse_S[0]
                self.Oy = self.e*self.m_wy - mouse_S[1]
import pygame as pg
from settings import WIN_HEIGHT, WIN_WIDTH
import numpy as np


class Grid:
    def __init__(self, x, y):
        # e0 - Фактическая система координат(через нее задаются положения точек):          
        self._e01 = 1  # Длина фактического вектора x
        self._e02 = 1  # Длина фактического вектора y
        self.x = x  # Начало системы отсчета по х
        self.y = y  # Начало системы отсчета по y
        self.fnt = pg.font.SysFont('Arial', 11)
        self.division_cost = 100
        # self.division_cost = WIN_WIDTH // camera.e1 // 5
        self.input_textDV = str(self.division_cost)
        self.value = 1
        
    # Метод для рисования сетки:
    def draw_grid(self, screen, camera):
        x_offset = camera.rect.x % camera.e1
        y_offset = camera.rect.y % camera.e2

        x_lines = np.arange(WIN_WIDTH // camera.e1 + 2)
        y_lines = np.arange(WIN_HEIGHT // camera.e2 + 2)

        for i in x_lines:
            pg.draw.line(screen, (45, 45, 45),
                    (i * camera.e1 - x_offset, 0 - y_offset),
                    (i * camera.e1 - x_offset, WIN_HEIGHT - y_offset + camera.e2))
            
        for i in y_lines:
            pg.draw.line(screen, (45, 45, 45),
                    (0 - x_offset, i * camera.e2 - y_offset),
                    (WIN_WIDTH - x_offset + 2 * camera.e1, i * camera.e2 - y_offset))
        
        under_surfaceX = pg.Surface((WIN_WIDTH, 200)).convert()
        under_surfaceY = pg.Surface((48, WIN_WIDTH)).convert()
        under_surfaceX.fill((40, 40, 40))
        under_surfaceY.fill((40, 40, 40))
        
        if camera.disp_planes == 1:
            for j in np.arange(self.y - camera.rect.y, -WIN_HEIGHT, -camera.e2 * self.division_cost):               
                if (j + camera.rect.y) % (camera.e2 * self.division_cost) == 0:
                    pg.draw.line(under_surfaceY, (90, 90, 90), (self.x - camera.rect.x + 50, j), (20, j), 1)
                    screen.blit(under_surfaceY, (0 - camera.rect.x - 48, 0))

            for i in np.arange(self.x - camera.rect.x, WIN_WIDTH, camera.e1 * self.division_cost):
                if i >= self.x + 0 and i <= self.x + 50:
                    continue           
                if (i + camera.rect.x) % (camera.e1 * self.division_cost) == 0:
                    pg.draw.line(under_surfaceX, (90, 90, 90), (i, self.y - camera.rect.y - 750), (i, -WIN_HEIGHT + 785), 1)    
                    screen.blit(under_surfaceX, (0, 0 - camera.rect.y))

            for j in np.arange(self.y - camera.rect.y, -WIN_HEIGHT, -camera.e2 * self.division_cost//2):
                if i >= self.x + 0 and i <= self.x + 50:
                    continue  
                if (j + camera.rect.y) % (camera.e2 * self.division_cost) != 0:
                    pg.draw.line(under_surfaceY, (90, 90, 90), (self.x - camera.rect.x + 50, j), (35, j), 1)
                    screen.blit(under_surfaceY, (0 - camera.rect.x - 48, 0))

            for i in np.arange(self.x - camera.rect.x, WIN_WIDTH, camera.e1 * self.division_cost//2):
                if (i + camera.rect.x) % (camera.e1 * self.division_cost) != 0:
                    pg.draw.line(under_surfaceX, (90, 90, 90), (i, self.y - camera.rect.y - 750), (i, -WIN_HEIGHT + 770), 1)
                    screen.blit(under_surfaceX, (0, 0 - camera.rect.y))

        elif camera.disp_planes == 2:
            for i in np.arange(self.x - camera.rect.x, WIN_WIDTH, camera.e1 * self.division_cost):
                if i >= self.x + 0 and i <= self.x + 50:
                    continue  
                if (i + camera.rect.x) % (camera.e1 * self.division_cost) == 0:
                    pg.draw.line(under_surfaceX, (90, 90, 90), (i, self.y - camera.rect.y - 750), (i, -WIN_HEIGHT + 785), 1)
                    screen.blit(under_surfaceX, (0, 0 - camera.rect.y))

            for i in np.arange(self.x - camera.rect.x, -WIN_WIDTH, -camera.e1 * self.division_cost):
                if i >= self.x and i <= self.x + 50:
                    continue 
                if (i + camera.rect.x) % (camera.e1 * self.division_cost) == 0:
                    pg.draw.line(under_surfaceX, (90, 90, 90), (i, self.y - camera.rect.y - 750), (i, -WIN_HEIGHT + 785), 1)
                    screen.blit(under_surfaceX, (0, 0 - camera.rect.y))

            for i in np.arange(self.x - camera.rect.x, WIN_WIDTH, camera.e1 * self.division_cost//2):
                if i >= self.x + 0 and i <= self.x + 50:
                    continue  
                if (i + camera.rect.x) % (camera.e1 * self.division_cost) != 0:
                    pg.draw.line(under_surfaceX, (90, 90, 90), (i, self.y - camera.rect.y - 750), (i, -WIN_HEIGHT + 770), 1)
                    screen.blit(under_surfaceX, (0, 0 - camera.rect.y))

            for i in np.arange(self.x - camera.rect.x, -WIN_WIDTH, -camera.e1 * self.division_cost//2):
                if i >= self.x + 0 and i <= self.x + 50:
                    continue  
                if (i + camera.rect.x) % (camera.e1 * self.division_cost) != 0:
                    pg.draw.line(under_surfaceX, (90, 90, 90), (i, self.y - camera.rect.y - 750), (i, -WIN_HEIGHT + 770), 1)
                    screen.blit(under_surfaceX, (0, 0 - camera.rect.y))

        elif camera.disp_planes == 3: 
            for j in np.arange(self.y - camera.rect.y, -WIN_HEIGHT, -camera.e2 * self.division_cost):
                if (j + camera.rect.y) % (camera.e2 * self.division_cost) == 0:
                    pg.draw.line(under_surfaceY, (90, 90, 90), (self.x - camera.rect.x + 50, j), (20, j), 1)
                    screen.blit(under_surfaceY, (0 - camera.rect.x - 48, 0))
            
            for j in np.arange(self.y - camera.rect.y, WIN_HEIGHT, camera.e2 * self.division_cost):
                if (j + camera.rect.y) % (camera.e2 * self.division_cost) == 0:
                    pg.draw.line(under_surfaceY, (90, 90, 90), (self.x - camera.rect.x + 50, j), (20, j), 1)
                    screen.blit(under_surfaceY, (0 - camera.rect.x - 48, 0))

            for j in np.arange(self.y - camera.rect.y, -WIN_HEIGHT, -camera.e2 * self.division_cost//2):
                if (j + camera.rect.y) % (camera.e2 * self.division_cost) != 0:
                    pg.draw.line(under_surfaceY, (90, 90, 90), (self.x - camera.rect.x + 50, j), (35, j), 1)
                    screen.blit(under_surfaceY, (0 - camera.rect.x - 48, 0))

            for j in np.arange(self.y - camera.rect.y, WIN_HEIGHT, camera.e2 * self.division_cost//2):
                if (j + camera.rect.y) % (camera.e2 * self.division_cost) != 0:
                    pg.draw.line(under_surfaceY, (90, 90, 90), (self.x - camera.rect.x + 50, j), (35, j), 1)
                    screen.blit(under_surfaceY, (0 - camera.rect.x - 48, 0))

    def draw_axis(self, screen, camera):
        pg.draw.line(screen, (95,135,30), (self.x - camera.rect.x, 0), (self.x - camera.rect.x, 2*-camera.e1-camera.rect.y), 1) # +Y
        pg.draw.line(screen, (250,50,80), (WIN_WIDTH, self.y - camera.rect.y), (2*camera.e1-camera.rect.x, self.y - camera.rect.y), 1) # +X
        pg.draw.rect(screen, (50, 50, 150), (0 - camera.rect.x - camera.e1/2, 0 - camera.rect.y - camera.e2/2, camera.e1, camera.e2))
        
        if camera.disp_planes == 0 or camera.disp_planes == 2:
            pg.draw.line(screen, (250,50,80), (0, self.y - camera.rect.y), (2*-camera.e1-camera.rect.x, self.y - camera.rect.y), 1) #-X
        if camera.disp_planes == 0 or camera.disp_planes == 3:
            pg.draw.line(screen, (95,135,30), (self.x - camera.rect.x, 2*camera.e1-camera.rect.y), (self.x - camera.rect.x,  WIN_HEIGHT), 1) #-Y
    
    def draw_values(self, screen, camera):
        for i in np.arange(self.x, WIN_WIDTH+camera.rect.x, camera.e1 * self.division_cost):      #+X
            value = i // camera.e1
            if value != 0:
                value_text = self.fnt.render(str(int(value)//self.value), 1, (180, 180, 180))
                if -1*camera.rect.y >= WIN_HEIGHT-15:
                    screen.blit(value_text, (i-camera.rect.x, WIN_HEIGHT - 12))
                elif -1 * camera.rect.y <= 0:
                    screen.blit(value_text, (i-camera.rect.x, 5))
                else:
                    screen.blit(value_text, (i-camera.rect.x, self.y-camera.rect.y+5))
                
        for j in np.arange(self.y, -WIN_HEIGHT+camera.rect.y, -camera.e2 * self.division_cost):  #+Y   
            value_text = self.fnt.render(str(int(-j // camera.e2)//self.value), 1, (180, 180, 180))
            value = j // camera.e1
            if value != 0:
                if -1*camera.rect.x <= 23:
                    screen.blit(value_text, (5, j-camera.rect.y))
                elif -1*camera.rect.x >= WIN_WIDTH+7:
                    screen.blit(value_text, (WIN_WIDTH-14, j-camera.rect.y)) 
                else: 
                    screen.blit(value_text, (self.x-camera.rect.x-20, j-camera.rect.y)) 
                
        if camera.disp_planes == 0 or camera.disp_planes == 2:    
            for i in np.arange(self.x, -WIN_WIDTH+camera.rect.x, -camera.e1 * self.division_cost):       #-X
                value_text = self.fnt.render(str(int(i // camera.e1)//self.value), 1, (180, 180, 180))   
                value = i // camera.e1
                if value != 0:
                    if -1*camera.rect.y >= WIN_HEIGHT-15:
                        screen.blit(value_text, (i-camera.rect.x, WIN_HEIGHT - 12))
                    elif -1 * camera.rect.y <= 0:
                        screen.blit(value_text, (i-camera.rect.x, 5))
                    else:
                        screen.blit(value_text, (i-camera.rect.x, self.y-camera.rect.y+5))
            
        if camera.disp_planes == 0 or camera.disp_planes == 3:
            for j in np.arange(self.y, WIN_HEIGHT+camera.rect.y, camera.e2 * self.division_cost):        #-y
                value_text_y = self.fnt.render(str(int(-j // camera.e2)//self.value), 1, (180, 180, 180))
                value = j // camera.e1
                if value != 0:
                    if -1*camera.rect.x <= 23:
                        screen.blit(value_text_y, (5, j-camera.rect.y))
                    elif -1*camera.rect.x >= WIN_WIDTH+7:
                        screen.blit(value_text_y, (WIN_WIDTH-14, j-camera.rect.y)) 
                    else:
                        screen.blit(value_text_y, (self.x-camera.rect.x-20, j-camera.rect.y))

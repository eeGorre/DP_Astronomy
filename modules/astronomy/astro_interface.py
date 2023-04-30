import pygame as pg
from settings import WIN_HEIGHT, WIN_WIDTH
from math import sqrt

class Astro_Interface:
    def __init__(self, obj):
        self.objects = obj
        self.fnt = pg.font.SysFont('Arial', 13)
        self.fnt2 = pg.font.SysFont('Arial', 15)
        self.fnt3 = pg.font.SysFont('Arial', 18)
        self.hide = False

    def mouse_coords(self, camera, screen):
        
        self.pos = pg.mouse.get_pos()
        mouse_coords_hud = self.fnt.render(f'{round(((0 + camera.Ox)+self.pos[0])/camera.e, 2), -round(((0 + camera.Oy) + self.pos[1])/camera.e, 2)}', 1, (200, 200, 200))
        screen.blit(mouse_coords_hud, (self.pos[0]+self.mouse_coords_font_size//2,self.pos[1]-self.mouse_coords_font_size-2))

    def obj_name(self, screen, camera):  
        if self.hide == False:  
            for obj in self.objects:
                if obj.obj_type != 'Sputnik':
                    planet_name = self.fnt.render(obj.name, 1, (130, 130, 130))
                    screen.blit(planet_name, ((obj.x + obj.radius) * camera.e - camera.Ox, (obj.y - obj.radius) * camera.e - camera.Oy))
                
    def obj_trace(self, screen, camera):
        if self.hide == False: 
            for obj in self.objects:
                if obj.obj_type != 'Sputnik':
                    obj.trace.append((obj.x, obj.y))
                    if len(obj.trace) < 5000:
                        for i in range(1, len(obj.trace), 100):
                            x1, y1 = obj.trace[i-1]
                            x1 = x1 * camera.e - camera.Ox
                            y1 = y1 * camera.e - camera.Oy
                            pg.draw.line(screen, (100, 100, 100), (x1, y1), (x1, y1), 1)
                    else:
                        del obj.trace[:100]
                
                
                
    def obj_menu(self, screen, camera):
        for obj in self.objects:
            if obj.selected:
                pg.draw.rect(screen, (0, 0, 0), (WIN_WIDTH*0.78, 0, WIN_WIDTH, WIN_HEIGHT))
                pg.draw.line(screen, (70, 70, 70), [WIN_WIDTH*0.78, WIN_HEIGHT], [WIN_WIDTH*0.78, 0], 2)
                pg.draw.line(screen, (40, 40, 40), [WIN_WIDTH*0.78, WIN_HEIGHT*0.05], [WIN_WIDTH, WIN_HEIGHT*0.05], 1)
                
                obj_quantity = self.fnt2.render(f'Всего в симуляции {len(self.objects)} объектов', 1, (135, 135, 135))
                screen.blit(obj_quantity, (WIN_WIDTH*0.79, WIN_HEIGHT*0.014))
                
                pg.draw.line(screen, (40, 40, 40), [WIN_WIDTH*0.78, WIN_HEIGHT*0.15], [WIN_WIDTH, WIN_HEIGHT*0.15], 1)
                
                obj_select = self.fnt2.render(f'Выбран объект {obj.name}', 1, (135, 135, 135))
                screen.blit(obj_select, (WIN_WIDTH*0.79, WIN_HEIGHT*0.085))
                pg.draw.circle(screen, (obj.color), [WIN_WIDTH*0.97, WIN_HEIGHT*0.1], 23)
                
                pg.draw.line(screen, (40, 40, 40), [WIN_WIDTH*0.78, WIN_HEIGHT*0.22], [WIN_WIDTH, WIN_HEIGHT*0.22], 1)
                
                obj_features = self.fnt3.render(f'Характеристики объекта', 1, (135, 135, 135))
                screen.blit(obj_features, (WIN_WIDTH*0.79, WIN_HEIGHT*0.17))
                
                pg.draw.line(screen, (40, 40, 40), [WIN_WIDTH*0.78, WIN_HEIGHT*0.6], [WIN_WIDTH, WIN_HEIGHT*0.6], 1)
                
                obj_radius = self.fnt2.render(f'Радиус: {obj.radius//1000} км', 1, (135, 135, 135))
                obj_mass = self.fnt2.render(f'Масса: {int(obj.m//1_000_000_000_000_000)} гигатонн', 1, (135, 135, 135))
                obj_temperature = self.fnt2.render(f'Температура: TBA', 1, (135, 135, 135))
                obj_density = self.fnt2.render(f'Плотность: TBA', 1, (135, 135, 135))
                obj_age = self.fnt2.render(f'Возраст: TBA', 1, (135, 135, 135))
                obj_luminosity = self.fnt2.render(f'Светимость TBA', 1, (135, 135, 135))
                obj_rotation_period = self.fnt2.render(f'Период вращения: TBA', 1, (135, 135, 135))
                obj_speed = self.fnt2.render(f'Скорость: {round(((obj.vx**2 + obj.vy**2)**0.5)/1000, 3)} км/c', 1, (135, 135, 135))
                
                screen.blit(obj_radius, (WIN_WIDTH*0.79, WIN_HEIGHT*0.23))
                screen.blit(obj_mass, (WIN_WIDTH*0.79, WIN_HEIGHT*0.265))
                screen.blit(obj_temperature, (WIN_WIDTH*0.79, WIN_HEIGHT*0.3))
                screen.blit(obj_density, (WIN_WIDTH*0.79, WIN_HEIGHT*0.335))
                screen.blit(obj_age, (WIN_WIDTH*0.79, WIN_HEIGHT*0.37))
                screen.blit(obj_luminosity, (WIN_WIDTH*0.79, WIN_HEIGHT*0.405))
                screen.blit(obj_rotation_period, (WIN_WIDTH*0.79, WIN_HEIGHT*0.440))
                screen.blit(obj_speed, (WIN_WIDTH*0.79, WIN_HEIGHT*0.475))
                
                print(self.hide)
                
    
                
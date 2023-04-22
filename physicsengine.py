import numpy as np
import pygame as pg


class PhysicsEngine:
    def __init__(self, obj):
        self.objects = obj
        
        self.M = 5.97 * (10**24)
        self.G = 6.67 * (10**-11)
        self.R = 6371 * 1000
        self.g = (self.G * (self.M / (self.R ** 2))) * 6
        self.mu = 1.5
         
    def apply_force(self):
         for obj in self.objects:
            obj.ax += obj.force_x / obj.mass
            obj.ay += obj.force_y / obj.mass
    
    
    
    def collision(self, disp_planes):
        for i in range(len(self.objects)):
            for j in range(i+1, len(self.objects)):
                obj1 = self.objects[i]
                obj2 = self.objects[j]
                if obj1.rect.colliderect(obj2.rect):
                    v_rel = [obj1.vx - obj2.vx, obj1.vy - obj2.vy]  # относитльная скорость между объектами
                    separation = np.subtract([obj1.x, obj1.y],
                                             obj2.x, obj2.y)  # определение расстояния между центрами объектов
                    distance = np.linalg.norm(separation)  # тут очень легко, всего лишь вычисление евклидовой нормы вектора
                    separation_norm = separation / distance
                    v_rel_dot_separation = np.dot(v_rel, separation_norm)  # вычисляем точечное произведение между двумя массивами произведение(так вот где оно нужно)
                    if v_rel_dot_separation > 0:
                        e = min(obj1.restitution, obj2.restitution)  # коэфицент упругости
                        impulse_magnitude = -(1 + e) * v_rel_dot_separation / (1/obj1.mass + 1/obj2.mass) # тут всё и так понятно
                        impulse = impulse_magnitude * separation_norm 
                        obj1.vx += impulse[0] / obj1.m  # Формула  
                        obj1.vy += impulse[1] / obj1.m  # нахождения
                        obj2.vx -= impulse[0] / obj2.m  # скорости через
                        obj2.vy -= impulse[1] / obj2.m  # импульс

            for obj in self.objects:
                if disp_planes == 1:
                    if obj.y >= -obj.height_obj * 3:
                        obj.y = -obj.height_obj * 3
                        obj.ay = 0
                        obj.vy = 0
                    if obj.x <= obj.width_obj * 3:
                        obj.x = obj.width_obj * 3
                if disp_planes == 2:
                    if obj.y >= -obj.height_obj * 3:
                        obj.y = -obj.height_obj * 3
                        obj.ay = 0
                        obj.vy = 0
                if disp_planes == 3:
                    if obj.x <= obj.width_obj * 3:
                        obj.x = obj.width_obj * 3
    
    def gravitation(self, disp_planes):
        for obj in self.objects:
            if obj.gravitation:
                if disp_planes == 1 or disp_planes == 2:
                    if int(obj.y) <= 0:
                        obj.vy += self.g * clock
                        obj.y += obj.vy * clock + 0.5 * self.g * clock**2

                if disp_planes == 3:
                    obj.ay += 100 * clock
                    obj.y += obj.ay * clock
                    if int(obj.y) > 0:
                        obj.ay -= 1000 * clock
                    if int(obj.y) < 0:
                        obj.ay += 1000 * clock
                    if int(obj.y) == 0:
                        obj.ay /= 1
                        
                    obj.x += obj.vx * clock

    def update(self, disp_planes):
        for obj in self.objects:
            if disp_planes != 3:
                if obj.y == -obj.height_obj * 3:
                    friction = -self.mu * obj.vx, -self.mu * obj.vy
                    obj.vx += (friction[0] + obj.ax) * clock
                else:
                    obj.vx += obj.ax * clock
                obj.vy += obj.ay * clock
                obj.x += obj.vx * clock
                obj.y += obj.vy * clock

            
def handler(c):
    global clock, mouse_pos
    
    mouse_pos = pg.mouse.get_pos()
    clock = c.get_time() / 1000
    

from math import pi, sqrt
import random

class Physics:
    def __init__(self, obj):
        self.objects = obj
        self.G = 6.67 * (10**-11)

    def move(self, delta_time, camera):
        try: # проверяем на наличие ошибок
            for i in range(len(self.objects)):
                for j in range(i+1, len(self.objects)):
                    objA = self.objects[i]
                    objB = self.objects[j]
                    if objA.m != 0 and objB.m != 0:
                        # Вычисляем расстояние между планетами
                        r = (((objB.x - objA.x) ** 2 + (objB.y - objA.y) ** 2) ** 0.5)

                        # Вычисляем силу, с которой планеты взаимодействуют друг с другом
                        f = self.G * objA.m * objB.m / r ** 2

                        # Вычисляем проекции силы на оси координат
                        fx = f * (objB.x - objA.x) / r
                        fy = f * (objB.y - objA.y) / r
                        
                        # Изменяем скорость каждой планеты, учитывая силу, с которой она взаимодействует с другой планетой
                        objA.vx += fx * delta_time / objA.m
                        objA.vy += fy * delta_time / objA.m
                        objB.vx -= fx * delta_time / objB.m
                        objB.vy -= fy * delta_time / objB.m

                        if r <= objA.radius + objB.radius:
                            if objA.m >= objB.m:
                                objA.m += objB.m
                                objA.radius = (objA.radius**2+objB.radius**2)**(0.5)
                                objA.vx = (objA.m*objA.vx+objB.m*objB.vx)/(objA.m+objB.m)
                                objA.vy = (objA.m*objA.vy+objB.m*objB.vy)/(objA.m+objB.m)
                                self.objects.remove(objB)
                                objA.fcv = sqrt(self.G*(objA.m/objA.radius))
                                objA.scv = sqrt(2) * (sqrt(self.G*(objA.m/objA.radius)))

                            if objB.m > objA.m:
                                objB.m += objA.m
                                objB.radius = (objB.radius**2+objA.radius**2)**(0.5)
                                objB.vx = (objB.m*objB.vx+objA.m*objA.vx)/(objB.m+objA.m)
                                objB.vy = (objB.m*objB.vy+objA.m*objA.vy)/(objB.m+objA.m)
                                self.objects.remove(objA)  
                                objB.fcv = sqrt(self.G*(objB.m/objB.radius))
                                objB.scv = sqrt(2) * (sqrt(self.G*(objB.m/objB.radius)))
                                
                            
            # # Изменяем координаты каждой планеты, учитывая ее скорость
            for obj in self.objects:
                obj.x += obj.vx * delta_time
                obj.y += obj.vy * delta_time
        except: # если ошибка есть, то скипаем её и циклим цикл дальше
            pass     
           
    def satelliteDetection(self):
        for i in range(len(self.objects)):
            for j in range(i+1, len(self.objects)):
                obj1 = self.objects[i]
                obj2 = self.objects[j]
                
                distance = sqrt((obj1.x - obj2.x)**2 + (obj1.y - obj2.y)**2)
                velocity = sqrt(obj1.vx**2 + obj1.vy**2) - sqrt(obj2.G * obj2.m / distance)
                orbital_velocity = sqrt(obj1.G * obj2.m / distance)
                
                if obj1.isSatellite() and obj2.isSatellite():
                    continue
                
                if obj1.isSatellite():
                    if velocity > orbital_velocity:
                        obj1.obj_type = "Satellite"
                        obj1.parent = obj2
                        
                if obj2.isSatellite():
                    if velocity > orbital_velocity:
                        obj2.obj_type = "Satellite"
                        obj2.parent = obj1
                
        
from math import pi
import random

class Physics:
    def __init__(self, obj):
        self.objects = obj
        self.G = 6.67 * (10**-11)

    def move(self, delta_time, camera):
        try:
            for i in range(len(self.objects)):
                for j in range(i+1, len(self.objects)):
                    obj1 = self.objects[i]
                    obj2 = self.objects[j]
                    if obj1.m != 0 and obj2.m != 0:
                        # Вычисляем расстояние между планетами
                        r = (((obj2.x - obj1.x) ** 2 + (obj2.y - obj1.y) ** 2) ** 0.5)

                        # Вычисляем силу, с которой планеты взаимодействуют друг с другом
                        f = self.G * obj1.m * obj2.m / r ** 2

                        # Вычисляем проекции силы на оси координат
                        fx = f * (obj2.x - obj1.x) / r
                        fy = f * (obj2.y - obj1.y) / r

                        # Изменяем скорость каждой планеты, учитывая силу, с которой она взаимодействует с другой планетой
                        obj1.vx += fx * delta_time / obj1.m
                        obj1.vy += fy * delta_time / obj1.m
                        obj2.vx -= fx * delta_time / obj2.m
                        obj2.vy -= fy * delta_time / obj2.m

                        if r <= obj1.radius + obj2.radius:
                            if obj1.m >= obj2.m:
                                obj1.m += obj2.m
                                obj1.radius = (obj1.radius**2+obj2.radius**2)**(0.5)
                                obj1.vx = (obj1.m*obj1.vx+obj2.m*obj2.vx)/(obj1.m+obj2.m)
                                obj1.vy = (obj1.m*obj1.vy+obj2.m*obj2.vy)/(obj1.m+obj2.m)
                                self.objects.remove(obj2)

                            if obj2.m > obj1.m:
                                obj2.m += obj1.m
                                obj2.radius = (obj2.radius**2+obj1.radius**2)**(0.5)
                                obj2.vx = (obj2.m*obj2.vx+obj1.m*obj1.vx)/(obj2.m+obj1.m)
                                obj2.vy = (obj2.m*obj2.vy+obj1.m*obj1.vy)/(obj2.m+obj1.m)
                                self.objects.remove(obj1)  
                            
   
                            
            # # Изменяем координаты каждой планеты, учитывая ее скорость
            for obj in self.objects:
                obj.x += obj.vx * delta_time
                obj.y += obj.vy * delta_time
                
        except:
            pass
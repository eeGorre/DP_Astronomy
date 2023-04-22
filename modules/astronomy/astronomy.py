from modules.astronomy.astro_objects import AstroObjects
from modules.astronomy.physics import Physics
from modules.astronomy.astro_interface import Astro_Interface
from math import sqrt

class Astronomy:
    def __init__(self):
        self.G = 6.67 * (10**-11) # Гравитационная постоянная в СИ
        self.AU = 150*10**9 # Астрономическая единица в CИ

        self.Sun = AstroObjects(0,
                                0,
                                "Sun",
                                2*10**30, 
                                0, 0, 
                                695_700_000,
                                (255, 255, 115))
        
        self.Mercury = AstroObjects(0.4*self.AU,
                                    0,
                                    "Mercury",
                                    3.3*10**23, 
                                    0, sqrt(self.G*self.Sun.m / (0.71*self.AU)), 
                                    2_439_500,
                                    (195, 185, 160))
        
        self.Venus = AstroObjects(0.71*self.AU,
                                    0,
                                    "Venus",
                                    4.9*10**24, 
                                    0, sqrt(self.G*self.Sun.m / (0.71*self.AU)), 
                                    6_051_500,
                                    (210, 170, 115))

        self.Earth = AstroObjects(self.AU,
                                    0,
                                    "Earth",
                                    6*10**24, 
                                    0, sqrt(self.G*self.Sun.m / self.AU), # для солнечной системы: sqrt(self.G*self.Sun.m / self.AU)
                                    6_371_000,
                                    (0, 220, 255))
        
        self.Moon = AstroObjects(self.Earth.x + 385_000_000,
                                 0,
                                 "Moon",
                                 7.3*10**22,
                                 0, sqrt(self.G*self.Sun.m / self.AU) + sqrt(self.G*self.Earth.m / 385_000_000),
                                 1737*10**3,
                                 (120,120,120))


        self.Mars = AstroObjects(1.55 * self.AU,
                                    0,
                                    "Mars",
                                    6.4*10**23, 
                                    0, sqrt(self.G*self.Sun.m / (1.55*self.AU)), 
                                    3_390_000,
                                    (255, 105, 65))
        
        self.Ceres = AstroObjects(2.984 * self.AU,
                                    0,
                                    "Ceres",
                                    9.39*10**20, 
                                    0, sqrt(self.G*self.Sun.m / (2.984 * self.AU)), 
                                    463_500,
                                    (165, 160, 160))

        self.Jupiter = AstroObjects(5.2 * self.AU,
                                    0,
                                    "Jupiter",
                                    1.9*10**27, 
                                    0, sqrt(self.G*self.Sun.m / (5.2 * self.AU)), 
                                    69_911_000,
                                    (250, 215, 120))

        self.Saturn = AstroObjects(9.55 * self.AU,
                                    0,
                                    "Saturn",
                                    5.7*10**26, 
                                    0, sqrt(self.G*self.Sun.m / (9.55 * self.AU)), 
                                    58_232_000,
                                    (235, 155, 95))
        
        self.Uranus = AstroObjects(19.22 * self.AU,
                                    0,
                                    "Uranus",
                                    8.7*10**25, 
                                    0, sqrt(self.G*self.Sun.m / (19.22 * self.AU)), 
                                    25_362_000,
                                    (235, 155, 95))

        self.Neptune = AstroObjects(30*self.AU,
                                    0,
                                    "Neptune",
                                    10**26, #10**26
                                    0, sqrt(self.G*self.Sun.m / (30 * self.AU)), 
                                    24_620_000,
                                    (0, 20, 165))
        
        self.Triton = AstroObjects(self.Neptune.x + 354_760_000, #354_760_000 - радиус орбиты вокруг Нептуна
                                   0,
                                   "Triton",
                                   2.14*10**22,
                                   0, sqrt(self.G*self.Sun.m / (30 * self.AU)) + sqrt(6.67 * (10**-11)*self.Neptune.m / 354_760_000),
                                   1_353_400, #1353400
                                   (255, 210, 210))
        
        self.Light = AstroObjects(0,
                                  0,
                                  "Light",
                                  0,
                                  300_000, 0,
                                  1,
                                  (255, 255, 255))
        
        self.objects = [self.Sun,self.Mercury, self.Venus, self.Earth, self.Moon, self.Ceres, self.Mars, self.Jupiter, self.Uranus, self.Neptune, self.Triton]
        self.astro_interface = Astro_Interface(self.objects)
        self.physics = Physics(self.objects)
        
        
        # self.objects = [self.Sun, self.Mercury, self.Venus, self.Earth, self.Moon, self.Mars, self.Ceres, self.Jupiter, self.Saturn, self.Uranus, self.Neptune, self.Triton]
        
        
    def level(self, screen, camera, delta_time, mouse_pos, event):
        screen.fill((0, 0, 0))
               
        
        self.physics.move(delta_time, camera)
        self.astro_interface.obj_name(screen, camera)

        for obj in self.objects:
            obj.render(screen, camera, mouse_pos, event)
            

        
        
        
        
        

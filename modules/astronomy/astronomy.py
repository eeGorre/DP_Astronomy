from modules.astronomy.astro_objects import AstroObjects
from modules.astronomy.physics import Physics
from modules.astronomy.astro_interface import Astro_Interface
from settings import WIN_WIDTH, WIN_HEIGHT
import pygame as pg
from math import sqrt
import random



class Astronomy:
    def __init__(self):
        self.G = 6.67 * (10**-11) # Гравитационная постоянная в СИ
        self.AU = 150*10**9 # Астрономическая единица в CИ
        self.LY = 63_241.077*self.AU
        
        self.bg = pg.image.load('bg.png')
        
        self.Sun = AstroObjects(0,
                                0,
                                "Sun",
                                2*10**30, 
                                0, 0, 
                                695_700_000,
                                'Star',
                                (255, 255, 200))
        
        self.Mercury = AstroObjects(0.4*self.AU,
                                    0,
                                    "Mercury",
                                    3.3*10**23, 
                                    0, sqrt(self.G*self.Sun.m / (0.71*self.AU)), 
                                    2_439_500,
                                    'Planet',
                                    (195, 185, 160))
        
        self.Venus = AstroObjects(0.71*self.AU,
                                    0,
                                    "Venus",
                                    4.9*10**24, 
                                    0, sqrt(self.G*self.Sun.m / (0.71*self.AU)), 
                                    6_051_500,
                                    'Planet',
                                    (210, 170, 115))

        self.Earth = AstroObjects(self.AU,
                                    0,
                                    "Earth",
                                    6*10**24, 
                                    0, sqrt(self.G*self.Sun.m / self.AU), # для солнечной системы: sqrt(self.G*self.Sun.m / self.AU)
                                    6_371_000,
                                    'Planet',
                                    (0, 220, 255))
        
        self.Moon = AstroObjects(self.Earth.x + 385_000_000,
                                 0,
                                 "Moon",
                                 7.3*10**22,
                                 0, sqrt(self.G*self.Sun.m / self.AU) + sqrt(self.G*self.Earth.m / 385_000_000),
                                 1737*10**3,
                                 'Sputnik',
                                 (120,120,120))

        self.Mars = AstroObjects(1.55 * self.AU,
                                    0,
                                    "Mars",
                                    6.4*10**23, 
                                    0, sqrt(self.G*self.Sun.m / (1.55*self.AU)), 
                                    3_390_000,
                                    'Planet',
                                    (255, 105, 65))
        
        self.Ceres = AstroObjects(2.984 * self.AU,
                                    0,
                                    "Ceres",
                                    9.39*10**20, 
                                    0, sqrt(self.G*self.Sun.m / (2.984 * self.AU)), 
                                    463_500,
                                    'Planet',
                                    (165, 160, 160))

        self.Jupiter = AstroObjects(5.2 * self.AU,
                                    0,
                                    "Jupiter",
                                    1.9*10**27, 
                                    0, sqrt(self.G*self.Sun.m / (5.2 * self.AU)), 
                                    69_911_000,
                                    'Planet',
                                    (250, 215, 120))

        self.Ganymede = AstroObjects(5.2 * self.AU + 1_070_400_000,
                                    0,
                                    "Ganymede",
                                    1.48*10**23, 
                                    0, sqrt(self.G*self.Sun.m / (5.2 * self.AU)) + sqrt(self.G*self.Jupiter.m / 1_070_400_000), 
                                    2_634_000,
                                    'Sputnik',
                                    (215, 215, 175))
        
        self.Callisto = AstroObjects(5.2 * self.AU + 1_882_709_000,
                                    0,
                                    "Callisto",
                                    1.1*10**23, 
                                    0, sqrt(self.G*self.Sun.m / (5.2 * self.AU)) + sqrt(self.G*self.Jupiter.m / 1_882_709_000), 
                                    4_821_000,
                                    'Sputnik',
                                    (95, 150, 135)) 

        self.Io = AstroObjects(5.2 * self.AU - 421_700_000 ,
                                    0,
                                    "Io",
                                    8.9*10**22, 
                                    0, sqrt(self.G*self.Sun.m / (5.2 * self.AU)) + sqrt(self.G*self.Jupiter.m / 421_700_000), 
                                    3_643_000,
                                    'Sputnik',
                                    (245, 235, 130))
        
        self.Europa = AstroObjects(5.2 * self.AU - 671_034_000,
                                    0,
                                    "Europa",
                                    4.8*10**22,
                                    0, sqrt(self.G*self.Sun.m / (5.2 * self.AU)) + sqrt(self.G*self.Jupiter.m / 671_034_000), 
                                    3_122_000,
                                    'Sputnik',
                                    (165, 175, 140))
        
        self.Saturn = AstroObjects(9.55 * self.AU,
                                    0,
                                    "Saturn",
                                    5.7*10**26, 
                                    0, sqrt(self.G*self.Sun.m / (9.55 * self.AU)), 
                                    58_232_000,
                                    'Planet',
                                    (235, 155, 95))
        
        self.Uranus = AstroObjects(19.22 * self.AU,
                                    0,
                                    "Uranus",
                                    8.7*10**25, 
                                    0, sqrt(self.G*self.Sun.m / (19.22 * self.AU)), 
                                    25_362_000,
                                    'Planet',
                                    (0, 135, 230))

        self.Neptune = AstroObjects(30*self.AU,
                                    0,
                                    "Neptune",
                                    10**26,
                                    0, sqrt(self.G*self.Sun.m / (30 * self.AU)), 
                                    24_620_000,
                                    'Planet',
                                    (0, 20, 165))
        
        self.Triton = AstroObjects(self.Neptune.x + 354_760_000,
                                   0,
                                   "Triton",
                                   2.14*10**22,
                                   0, sqrt(self.G*self.Sun.m / (30 * self.AU)) + sqrt(6.67 * (10**-11)*self.Neptune.m / 354_760_000),
                                   1_353_400, 
                                   'Sputnik',
                                   (255, 210, 210))
        
        '''
        Альфа центавра
        '''
        
        self.Alpha_Centauri_A = AstroObjects(-0.21 * self.AU,
                                     0,
                                     "Alpha Centauri A",
                                     1.1*10**31, 
                                     0, sqrt(self.G*self.Sun.m / (0.21*self.AU)), 
                                     1_227_000_000,
                                     'Star',
                                     (255, 255, 200))

        self.Alpha_Centauri_B = AstroObjects(-0.4 * self.AU - 23.7 * self.AU,
                                            0,
                                            "Alpha Centauri B",
                                            9.4*10**30, 
                                            0, sqrt(self.G*self.Sun.m / ((0.21+23.7)*self.AU)), 
                                            864_938_000,
                                            'Star',
                                            (255, 255, 200))

        self.Alpha_Centauri_C = AstroObjects(-0.7 * self.AU - 23.9 * self.AU,
                                            0,
                                            "Alpha Centauri C",
                                            1.2*10**29, 
                                            0, sqrt(self.G*self.Sun.m / ((0.21+23.9)*self.AU)), 
                                            3_474_000,
                                            'Planet',
                                            (165, 160, 160))

        
        
        
        
        self.objects = [self.Sun,self.Mercury, self.Venus, self.Earth, self.Moon, self.Ceres, self.Mars,
                        self.Jupiter, self.Uranus, self.Neptune, self.Triton, self.Europa, self.Ganymede,
                        self.Io, self.Callisto]
        
        self.astro_interface = Astro_Interface(self.objects)
        self.physics = Physics(self.objects)
        
    def level(self, screen, camera, delta_time, mouse_pos, event):
        self.bg = pg.transform.scale(self.bg, (WIN_WIDTH, WIN_HEIGHT))
        screen.blit(self.bg, (0, 0)) 
        
        self.physics.move(delta_time, camera)
        
        self.pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN: 
            if event.button == 3:
                new_object = AstroObjects(
                    (mouse_pos[0] + camera.x) / camera.e,
                    (mouse_pos[1] + camera.y) / camera.e,
                    'Gleboid',
                    1.3 * 10**22,
                    0, 0,
                    1_188_000,
                    'Asteroid',
                    (0, 200, 0)
                )
                self.objects.append(new_object)
                pg.time.wait(75)
        
        for obj in self.objects:
            obj.render(screen, camera, mouse_pos, event)
            
        self.astro_interface.obj_name(screen, camera)
        self.astro_interface.obj_menu(screen, camera)
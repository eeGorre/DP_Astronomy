from object import Object
import pygame as pg
from interface import Interface
from physicsengine import PhysicsEngine
import random


class Hub():
    def __init__(self, grid):
        self.object1 = Object(0, 0, 0, 0, 350, "Красный", grid,
                              'cube',  100, 0, 6, 6, (255, 0, 0))
        self.object2 = Object(0, 0, 0, 0, 350, "Зелёный", grid,
                              'cube', 250, 0, 6, 6, (0, 255, 0))
        self.object3 = Object(0, 0, 0, 0, 350, "Синий", grid,
                              'cube', 350, 0, 6, 6, (0, 0, 255))
        self.object4 = Object(0, 0, 0, 0, 350, "НЕГР", grid,
                              'cube', 500, 0, 6, 6, (0, 0, 0))
        
        self.objects = [self.object1, self.object2, self.object3, self.object4]
        self.gui_object1 = Interface()
        self.gui_object2 = Interface()
        self.gui_object3 = Interface()
        self.gui_object4 = Interface()
            
    def level(self, screen, camera, grid, event):
        self.physics = PhysicsEngine(self.objects)
        grid.draw_grid(screen, camera)
        grid.draw_values(screen, camera)
        grid.draw_axis(screen, camera)
        
        self.pos = pg.mouse.get_pos()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 3: 
            r, g, b = [pg.Color(random.randint(0, 255)) for i in range(3)]
            new_object = Object(0, 0, 0, 0, 12, "New", grid, 'cube',
                                self.pos[0]-720, self.pos[1], 6, 6, (r, g, b))
            self.objects.append(new_object)

        for obj in self.objects:
            obj.core(screen, camera, self.gui_object1)

        self.gui_object1.object_menu(screen, self.object1)
        self.gui_object2.object_menu(screen, self.object2)
        self.gui_object3.object_menu(screen, self.object3)
        self.gui_object4.object_menu(screen, self.object4)
  
        self.physics.gravitation(camera.disp_planes)
        self.physics.collision(camera.disp_planes)
        self.physics.update(camera.disp_planes)
        self.physics.apply_force()
        

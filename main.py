import pygame as pg
from pygame.locals import DOUBLEBUF, FULLSCREEN
import sys
 
from settings import WIN_WIDTH, WIN_HEIGHT, FPS
from camera import Camera
from interface import Interface
from modules.astronomy.astronomy import Astronomy
from modules.astronomy.astro_objects import AstroObjects
from grid import Grid


class Programm:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT),
                                           DOUBLEBUF, 16, )  # FULLSCREEN|
        self.screen.set_alpha(None)
        self.clock = pg.time.Clock()

        self.grid = Grid(0, 0)
        self.astronomy = Astronomy()
        self.camera = Camera()
        self.interface = Interface() 

        self.time_k = 1000
        self.pause = False
        
    def run(self):
        while 1:                   
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                
                
                mouse_pos = pg.mouse.get_pos()
                keys = pg.key.get_pressed()    
                self.interface.handler(event, self.clock)
                self.camera.zoom(event, keys, mouse_pos)    
                
                if event.type == pg.KEYDOWN and event.key == pg.K_p:
                    self.pause = not self.pause
                    
                if self.pause:
                    self.time_k = 0
                else:
                    self.time_k = 1000
                    
            self.camera.move()                               
            self.clock.tick(FPS)    
            self.delta_time = self.clock.get_time() * self.time_k

            # self.hub.level(self.screen, self.camera, self.grid, event)
            self.astronomy.level(self.screen, self.camera, self.delta_time, mouse_pos, event)
            
            self.interface.show_fps(self.clock)
            self.interface.camera_menu(self.screen, self.camera, self.grid)
            self.interface.mouse_coords(self.camera, self.screen)

            pg.display.flip()
            
if __name__ == '__main__':
    programm = Programm()
    programm.run()

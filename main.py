import pygame as pg
from pygame.locals import DOUBLEBUF, FULLSCREEN
from settings import WIN_WIDTH, WIN_HEIGHT, FPS
from camera import Camera
from interface import Interface
from modules.astronomy.astronomy import Astronomy

pg.mixer.init()
pg.mixer.music.load('OST/Unofficial/FasterThanLight.mp3')
pg.mixer.music.play(-1)


class Programm:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIN_WIDTH, WIN_HEIGHT),
                                           DOUBLEBUF, 16)  # FULLSCREEN|
        self.clock = pg.time.Clock()
        self.astronomy = Astronomy()
        self.camera = Camera()
        self.interface = Interface() 
        self.pause = False
        self.time_k = 100
        self.time_k_saved = self.time_k
    
    def run(self):
        while 1:                   
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                mouse_pos = pg.mouse.get_pos()
                keys = pg.key.get_pressed()    
                self.interface.handler(event, self.clock)
                self.camera.zoom(event, keys, mouse_pos)    
                
                if event.type == pg.KEYDOWN and event.key == pg.K_p:
                    self.pause = not self.pause
                    if self.pause:
                        self.time_k_saved = self.time_k
                        self.time_k = 0
                    else:
                        self.time_k = self.time_k_saved
                    
                if event.type == pg.MOUSEBUTTONDOWN and keys[pg.K_t]:
                    if event.button == 4:
                        self.time_k *= 1.03125
                    if event.button == 5:
                        self.time_k /= 1.03125
            
            
                                   
            mouse_rel_pos = list(pg.mouse.get_rel())
            
            self.camera.move(mouse_rel_pos)                               
            self.clock.tick(FPS)   
            
            self.delta_time = self.clock.get_time() * self.time_k
            
            self.astronomy.level(self.screen, self.camera, self.delta_time, mouse_pos, event)
            
            self.interface.show_fps(self.clock)
            self.interface.mouse_coords(self.camera, self.screen)
            self.interface.time(self.time_k, self.screen)

            
            
            pg.display.update()
            
if __name__ == '__main__':
    programm = Programm()
    programm.run()
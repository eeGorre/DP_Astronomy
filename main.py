import pygame as pg
from pygame.locals import DOUBLEBUF, FULLSCREEN
from settings import WIN_WIDTH, WIN_HEIGHT, FPS
from camera import Camera
from interface import Interface
from modules.astronomy.astronomy import Astronomy
import time 
from threading import Thread

pg.mixer.init()
pg.mixer.music.load('OST/Unofficial/FasterThanLight.mp3')
pg.mixer.music.play(-1)

seconds = 0

def seconds_counter():
    global seconds
    while True:
        seconds += 1
        time.sleep(1)
thread = Thread(target=seconds_counter)
thread.start()

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

                mouse_S = pg.mouse.get_pos() # Позиция курсора на экране (S = Screen)
                keys = pg.key.get_pressed()    
                self.interface.handler(event, self.clock)
                self.camera.zoom(event, keys, mouse_S)    
                
                if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                    self.pause = not self.pause
                    if self.pause:
                        self.time_k_saved = self.time_k
                        self.time_k = 0
                    else:
                        self.time_k = self.time_k_saved
                    
                if event.type == pg.MOUSEBUTTONDOWN and keys[pg.K_t]:
                    if 2591999 >= self.time_k * 1000:
                        if event.button == 4:
                            self.time_k *= 1.03125
                    if self.time_k * 1000 > 1:
                        if event.button == 5:
                            self.time_k /= 1.03125
        
            mouse_shift = list(pg.mouse.get_rel())
            self.delta_time = self.clock.get_time() * self.time_k
            self.camera.move(mouse_shift)                               
            self.clock.tick(FPS)   
            self.astronomy.level(self.screen, self.camera, self.delta_time, mouse_S, event, keys)
            self.interface.show_fps(self.clock)
            self.interface.mouse_coords(self.camera, self.screen)
            self.interface.time(self.time_k, self.screen)
            pg.display.update()
            
if __name__ == '__main__':
    programm = Programm()
    programm.run()
    
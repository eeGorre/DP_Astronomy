import pygame as pg
import time

pg.init()


timer = 0


def process_input_text(input_text, active):
    global timer
    keys = pg.key.get_pressed()
    current_time = time.perf_counter()
    
    if timer == 0 or current_time - timer >= 0.2:
        if active:
            if keys[pg.K_1]:
                input_text += '1'      
                timer = current_time
            if keys[pg.K_2]:
                input_text += '2'
                timer = current_time
            if keys[pg.K_3]:
                input_text += '3'
                timer = current_time
            if keys[pg.K_4]:
                input_text += '4'
                timer = current_time
            if keys[pg.K_5]:
                input_text += '5'
                timer = current_time
            if keys[pg.K_6]:
                input_text += '6'
                timer = current_time
            if keys[pg.K_7]:
                input_text += '7'
                timer = current_time
            if keys[pg.K_8]:
                input_text += '8'
                timer = current_time
            if keys[pg.K_9]:
                input_text += '9'
                timer = current_time
            if keys[pg.K_0]:
                input_text += '0'
                timer = current_time
            if keys[pg.K_MINUS]:
                input_text += '-'
                timer = current_time
            if keys[pg.K_PERIOD]:
                input_text += '.'
                timer = current_time
            
            if keys[pg.K_BACKSPACE]:
                input_text = input_text[:-1]
                timer = current_time
    
    return input_text
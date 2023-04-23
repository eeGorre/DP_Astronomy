import pygame as pg


class Object:
    menu_alpha = 0
    def __init__(self, vx, vy, ax, ay, m, name, grid, image_name=None,
                 x=0, y=0, width=6, height=6, color=(125, 125, 125)):
        self.grid = grid
        self.width_obj = width if width != 0 else 1
        self.height_obj = height if height != 0 else 1
        self.x = x
        self.y = -y
        self.vx = vx
        self.vy = -vy
        self.ax = ax
        self.ay = -ay
        self.mass = m
        
        self.restitution = 0.8
        self.force_x = 0
        self.force_y = 0
        self.second = 1000
        
        self.selected = False
        self.gravitation = True
        self.pause = False
        
        self.image = pg.image.load("assets/cube.png").convert()
        self.name = name
        
        self.xy = 12
        self.fnt3 = pg.font.SysFont('Arial', self.xy)

        self.rgb = 10
        self.fnt4 = pg.font.SysFont('Arial', self.rgb)

        self.color = color
        self.RED = color[0]
        self.GREEN = color[1]
        self.BLUE = color[2]

        self.input_textX, self.input_textY = str(self.x), str(self.y)
        self.input_textW, self.input_textH = str(self.width_obj), str(self.height_obj)
        self.input_textRED, self.input_textGREEN, self.input_textBLUE = str(self.RED), str(self.GREEN), str(self.BLUE)
        self.input_textAY, self.input_textAX = str(self.ay), str(self.ax)
        self.input_textVX, self.input_textVY = str(self.vx), str(self.vy)
        self.input_textFX, self.input_textFY = str(self.force_x), str(self.force_y)
        self.input_textMass = str(self.mass)
        self.input_textName = self.name
        
        self.timer = 0.5
        
        self.vector_up = pg.image.load("assets/VectorUp.png").convert_alpha()
        self.vector_down = pg.image.load("assets/VectorDown.png").convert_alpha()
        
        self.past_positions = []
        
    def core(self, screen, camera, gui):
        self.test_obj = pg.Surface((self.width_obj*camera.e1, self.height_obj*camera.e2))
        try:
            self.test_obj.fill((self.RED, self.GREEN, self.BLUE))
        except ValueError:
            print('Error: invalid color')
        self.test_obj_rect = self.test_obj.get_rect(center = (self.x*camera.zoom_level - camera.rect.x,
                                                     self.y*camera.zoom_level - camera.rect.y))
        screen.blit(self.test_obj, self.test_obj_rect)
        self.rect = self.test_obj_rect.copy()
        
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.test_obj_rect.collidepoint(event.pos):
                self.selected = True
            elif gui.object_hud_rect.collidepoint(event.pos) and event.button == 1:
                pass
            else:
                self.selected = False
                
        if self.selected and pg.key.get_pressed()[pg.K_g]:
            mouse_pos = pg.mouse.get_pos()
            if pg.key.get_pressed()[pg.K_x]:
                self.x = (mouse_pos[0] + camera.rect.x -  self.width_obj/2) / camera.zoom_level
            elif pg.key.get_pressed()[pg.K_y]:
                self.y = (mouse_pos[1] + camera.rect.y -  self.height_obj/2) / camera.zoom_level
            else:
                self.x = (mouse_pos[0] + camera.rect.x -  self.width_obj/2) / camera.zoom_level
                self.y = (mouse_pos[1] + camera.rect.y -  self.height_obj/2) / camera.zoom_level
                
        if self.selected:
            pg.draw.rect(self.test_obj, (230, 140, 50), (0,0, self.test_obj_rect.w, self.test_obj_rect.h),1)
            screen.blit(self.test_obj, self.test_obj_rect)
            
            if keys[pg.K_t]:
                if self.gravitation:
                    self.gravitation = False
                else:
                    self.gravitation = True

        else:
            self.menu_alpha = 0
        
        vector_up = self.vector_up.get_rect(center = (self.x*camera.zoom_level - camera.rect.x, self.y*camera.zoom_level - camera.rect.y-40))
        vector_down = self.vector_down.get_rect(center = (self.x*camera.zoom_level - camera.rect.x, self.y*camera.zoom_level - camera.rect.y+40))
        if int(self.ay) > 0:
            screen.blit(self.vector_down, vector_down)
        if int(self.ay) < 0:
            screen.blit(self.vector_up, vector_up)
        
        if keys[pg.K_p]:
            if self.pause:
                self.pause = False
            else:
                self.pause = True
        
        if self.pause:
            self.vx = 0
            self.vy = 0
            self.ax = 0
            self.ay = 0
        
        self.past_positions.append((self.x, self.y))
        if len(self.past_positions) > 1000:
            self.past_positions.pop(0)
            
        # self.draw_trajectory(screen, camera, self.past_positions)
        self.control()
        # self.move()

    def draw_trajectory(self, screen, camera, positions):
        for i in range(1, len(positions)):
            x1, y1 = positions[i-1]
            x2, y2 = positions[i]
            x1 = x1 * camera.zoom_level - camera.rect.x
            y1 = y1 * camera.zoom_level - camera.rect.y
            x2 = x2 * camera.zoom_level - camera.rect.x
            y2 = y2 * camera.zoom_level - camera.rect.y
            pg.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 2)
     
    def control(self):
        if self.selected:
            if keys[pg.K_w]:
                self.vx -= 15 * clock
            if keys[pg.K_s]:
                self.vx += 15 * clock
            if keys[pg.K_a]:
                self.vy -= 15 * clock
            if keys[pg.K_d]:
                self.vy += 15 * clock
            if keys[pg.K_SPACE]:
                self.vy -= 1

    def move(self):
        self.ay += self.ay * clock
        self.y += self.ay * clock
        
    def handler(self, e, c):
        global event, keys, clock

        event = e
        clock = c.get_time() / 1000
        keys = pg.key.get_pressed()

    def __str__(self):
        return 'Объект ' + self.name
        
    def __del__(self):
        print(f'{self} удалён.')
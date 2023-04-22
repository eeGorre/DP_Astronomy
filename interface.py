import pygame as pg
from settings import WIN_WIDTH, WIN_HEIGHT
import time
from handler import process_input_text


class Interface:
    menu_alpha = 0
    
    def __init__(self):
        self.mouse_coords_font_size = 10
        self.fnt = pg.font.SysFont('Arial', self.mouse_coords_font_size)
        self.fps_value_size = 15
        self.fnt2 = pg.font.SysFont('Arial', self.fps_value_size)
        self.xy = 17
        self.fnt3 = pg.font.SysFont('Arial', self.xy)
        self.fnt4 = pg.font.SysFont('Arial', 12)
        self.fnt5 = pg.font.SysFont('Arial', 11)

        self.aimed1 = False
        self.aimed2 = False
        self.menu_active = False
        self.hud1_active = False
        self.hud2_active = False

        self.active1 = False
        self.active2 = False
        self.active3 = False
        self.active4 = False
        self.active5 = False
        self.active6 = False
        self.active7 = False
        self.active8 = False
        self.active9 = False
        self.active10 = False
        self.active11 = False
        self.active12 = False
        self.active13 = False
        self.active14 = False
        self.active15 = False
        self.active16 = False
        self.active17 = False
        self.active18 = False
        self.active19 = False
        self.active20 = False

        self.show = 1
        self.hud_selected = 1
        self.switched = 1
        
        self.menu = pg.image.load("assets/CameraMenu.png").convert_alpha()
        self.object_hud1 = pg.image.load("assets/ObjectHud1.png").convert_alpha()
        self.object_hud21 = pg.image.load("assets/ObjectHud21.png").convert_alpha()
        self.object_hud22 = pg.image.load("assets/ObjectHud22.png").convert_alpha()
        self.object_hud_rect = self.object_hud1.get_rect(topleft = (WIN_WIDTH-363, 232))
        self.object_hud_rect2 = self.object_hud21.get_rect(topleft = (WIN_WIDTH-363, 232))
        self.arrow = pg.image.load("assets/Arrow.png").convert_alpha()
        self.NotActive = pg.image.load("assets/NotActive.png").convert_alpha()
        self.Active = pg.image.load("assets/Active.png").convert_alpha()
        self.aimed = pg.image.load("assets/Aimed.png").convert_alpha()
        self.area_active = pg.image.load("assets/AreaActive.png").convert_alpha()
        self.area_active2 = pg.image.load("assets/AreaActive2.png").convert_alpha()  
        self.area_active3 = pg.image.load("assets/AreaActive3.png").convert_alpha()
        self.area_active4 = pg.image.load("assets/Input.png").convert_alpha()
        self.area_active_mini = pg.image.load("assets/AreaActiveMini.png").convert_alpha()
        self.switcher = pg.image.load("assets/Switcher.png").convert_alpha()
        
    def mouse_coords(self, camera, screen):
        self.pos = pg.mouse.get_pos()
        mouse_coords_hud = self.fnt.render(f'{round(((0 + camera.rect.x)+self.pos[0])/camera.e1,2), -round(((0 + camera.rect.y) + self.pos[1])/camera.e2,2)}', 1, (200, 200, 200))
        screen.blit(mouse_coords_hud, (self.pos[0]+self.mouse_coords_font_size//2,self.pos[1]-self.mouse_coords_font_size-2))
        
    def show_fps(self, clock):
        pg.display.set_caption("FPS: {:.2f}".format(clock.get_fps()))

    def camera_menu(self, screen, camera, grid):
        input11 = self.area_active3.get_rect(topleft = (300, 60))
        input12 = self.area_active3.get_rect(topleft = (300, 90))
        input13 = self.area_active4.get_rect(topleft = (300, 90))

        if self.menu_active or keys[pg.K_TAB]:
            self.menu.set_alpha(self.menu_alpha)
            screen.blit(self.menu, (15, 15))
            if self.menu_alpha < 255:
                self.menu_alpha += 900 * clock

            if self.active11:
                screen.blit(self.area_active3, input11)
            if self.active12:
                screen.blit(self.area_active4, input12)
            if self.active13:
                screen.blit(self.area_active4, input13)

            if event.type == pg.MOUSEBUTTONDOWN:
                if input11.collidepoint(mouse_pos):
                    self.active11 = True
                else:
                    self.active11 = False

                if input12.collidepoint(mouse_pos):
                    self.active12 = True
                else:
                    self.active12 = False

                if input13.collidepoint(mouse_pos):
                    self.active13 = True
                else:
                    self.active13 = False
            
            division_cost = self.fnt4.render(grid.input_textDV, True,  (120, 120, 120))
            screen.blit(division_cost, (305, 62))

            meters = self.fnt4.render('Метры', True, (120, 120, 120))
            km = self.fnt5.render('Киллометры', True, (120, 120, 120))

            if self.show == 1:
                screen.blit(meters, (315, 94))
                if self.active13:
                    screen.blit(km, (305, 118))
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                        width, height = 73, 46
                        x, y = 315, 113
                        if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                            self.show = 2

            elif self.show == 2:
                screen.blit(km, (305, 94))
                if self.active13:
                    screen.blit(meters, (315, 118))
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                        if event.button == 1:
                            width, height = 73, 46
                            x, y = 315, 113
                            if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                                self.show = 1

            grid.input_textDV = process_input_text(grid.input_textDV, self.active11)

            if self.show == 1:
                try:
                    grid.division_cost = int(grid.input_textDV)
                    grid.value = 1
                except ValueError:
                    pass

            if self.show == 2:
                try:
                    grid.division_cost = int(grid.input_textDV) * 1000
                    grid.value = 1000
                except ValueError:
                    pass
            
            # if keys[pg.K_RETURN]:
            #     try:
            #         if self.active11:
            #             grid.division_cost = int(grid.input_textDV)
            #     except ValueError:
            #         pass
            
            S0 = self.fnt3.render('0', True, (160, 160, 160))
            S1 = self.fnt3.render('1', True, (160, 160, 160))
            S2 = self.fnt3.render('2', True, (160, 160, 160))
            S3 = self.fnt3.render('3', True, (160, 160, 160))

            if camera.disp_planes == 0:
                screen.blit(self.Active, (45, 145))

                for i in range(145, 500, 95):
                    screen.blit(self.NotActive, (i-100, 145))

                if mouse_buttons[0] == 1:
                    width, height = 50, 50
                    y = 145

                    x = 145
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 1
                        camera.x = -48
                        camera.y = -WIN_HEIGHT + 48

                    x = 230
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 2
                        camera.x = -WIN_WIDTH//2
                        camera.y = -WIN_HEIGHT + 48
                        
                    x = 335
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 3
                        camera.x = -48
                        camera.y = -WIN_HEIGHT//2

            if camera.disp_planes == 1:
                screen.blit(self.Active, (140, 145))

                for i in range(145, 500, 95):
                    screen.blit(self.NotActive, (i-100, 145))
                
                if mouse_buttons[0] == 1:
                    width, height = 50, 50
                    y = 145

                    x = 45
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 0
                        camera.x = -WIN_WIDTH//2
                        camera.y = -WIN_HEIGHT//2

                    x = 230
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 2
                        camera.x = -WIN_WIDTH//2
                        camera.y = -WIN_HEIGHT + 48

                    x = 335
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 3
                        camera.x = -48
                        camera.y = -WIN_HEIGHT//2

            if camera.disp_planes == 2:
                screen.blit(self.Active, (235, 145))

                for i in range(145, 500, 95):
                    screen.blit(self.NotActive, (i-100, 145))

                if mouse_buttons[0] == 1:
                    width, height = 50, 50
                    y = 145

                    x = 45
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 0
                        camera.x = -WIN_WIDTH//2
                        camera.y = -WIN_HEIGHT//2

                    x = 145
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 1
                        camera.x = -48
                        camera.y = -WIN_HEIGHT + 48

                    x = 335
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 3
                        camera.x = -48
                        camera.y = -WIN_HEIGHT//2
            
            if camera.disp_planes == 3:
                screen.blit(self.Active, (330, 145))

                for i in range(145, 500, 95):
                    screen.blit(self.NotActive, (i-100, 145))

                if mouse_buttons[0] == 1:
                    width, height = 50, 50
                    y = 145

                    x = 45
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 0
                        camera.x = -WIN_WIDTH//2
                        camera.y = -WIN_HEIGHT//2

                    x = 145
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 1
                        camera.x = -48
                        camera.y = -WIN_HEIGHT + 48

                    x = 235
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        camera.disp_planes = 2
                        camera.x = -WIN_WIDTH//2
                        camera.y = -WIN_HEIGHT + 48 

            if mouse_buttons[0] == 1:
                width, height = 17, 59
                y = 95
                x = 405
                if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                    self.menu_active = False

            screen.blit(S0, (65, 160))
            screen.blit(S1, (160, 160))
            screen.blit(S2, (255, 160))
            screen.blit(S3, (350, 160))

        else:
            screen.blit(self.arrow, (0, 83))
            self.menu_alpha = 0

            if mouse_buttons[0] == 1:
                width, height = 17, 59
                y = 83
                x = 0
                if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                    self.menu_active = True

    def object_menu(self, screen, object):
        y = 298
        width, height = 81, 68

        input1 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 383))
        input2 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 440))
        input3 = self.area_active2.get_rect(topleft = (WIN_WIDTH-184, 470))
        input4 = self.area_active2.get_rect(topleft = (WIN_WIDTH-184, 528))
        input5 = self.area_active2.get_rect(topleft = (WIN_WIDTH-184, 558))
        input6 = self.area_active2.get_rect(topleft = (WIN_WIDTH-184, 618))
        input7 = self.area_active2.get_rect(topleft = (WIN_WIDTH-184, 648))
        input8 = self.area_active_mini.get_rect(topleft = (WIN_WIDTH-184, 698))
        input9 = self.area_active_mini.get_rect(topleft = (WIN_WIDTH-125, 698))
        input10 = self.area_active_mini.get_rect(topleft = (WIN_WIDTH-67, 698))
        input14 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 383))
        input15 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 441))
        input16 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 499))
        input17 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 557))
        input18 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 617))
        input19 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 383))
        input20 = self.area_active.get_rect(topleft = (WIN_WIDTH-184, 440))
        
        if object.selected:
            if self.hud_selected == 1:
                self.object_hud1.set_alpha(self.menu_alpha)
                screen.blit(self.object_hud1, (WIN_WIDTH-363, 232))
                if self.menu_alpha < 255:
                    self.menu_alpha += 900 * clock

                if self.active1:
                    screen.blit(self.area_active, input1)
                if self.active2:
                    screen.blit(self.area_active, input2)
                if self.active3:
                    screen.blit(self.area_active2, input3)
                if self.active4:
                    screen.blit(self.area_active, input4)
                if self.active5:
                    screen.blit(self.area_active2, input5)
                if self.active6:
                    screen.blit(self.area_active, input6)
                if self.active7:
                    screen.blit(self.area_active2, input7)
                if self.active8:
                    screen.blit(self.area_active_mini, input8)
                if self.active9:
                    screen.blit(self.area_active_mini, input9)
                if self.active10:
                    screen.blit(self.area_active_mini, input10)

                if event.type == pg.MOUSEBUTTONDOWN:
                    if input1.collidepoint(mouse_pos):
                        self.active1 = True
                    else:
                        self.active1 = False
                    
                    if input2.collidepoint(mouse_pos):
                        self.active2 = True
                    else:
                        self.active2 = False

                    if input3.collidepoint(mouse_pos):
                        self.active3 = True
                    else:
                        self.active3 = False

                    if input4.collidepoint(mouse_pos):
                        self.active4 = True
                    else:
                        self.active4 = False

                    if input5.collidepoint(mouse_pos):
                        self.active5 = True
                    else:
                        self.active5 = False

                    if input6.collidepoint(mouse_pos):
                        self.active6 = True
                    else:
                        self.active6 = False

                    if input7.collidepoint(mouse_pos):
                        self.active7 = True
                    else:
                        self.active7 = False

                    if input8.collidepoint(mouse_pos):
                        self.active8 = True
                    else:
                        self.active8 = False

                    if input9.collidepoint(mouse_pos):
                        self.active9 = True
                    else:
                        self.active9 = False

                    if input10.collidepoint(mouse_pos):
                        self.active10 = True
                    else:
                        self.active10 = False

                    if WIN_WIDTH <= mouse_pos[0] <= WIN_WIDTH and y <= mouse_pos[1] <= 500 + 500:
                        object.selected = False
                
                name_text = self.fnt3.render(object.input_textName, True,  (120, 120, 120))
                screen.blit(name_text, (WIN_WIDTH - 175, 386))

                x_text = self.fnt3.render(object.input_textX, True, (120, 120, 120))
                screen.blit(x_text, (WIN_WIDTH-175, 445))

                y_text = self.fnt3.render(object.input_textY, True,  (120, 120, 120))
                screen.blit(y_text, (WIN_WIDTH-175, 475))

                w_text = self.fnt3.render(object.input_textW, True,  (120, 120, 120))
                screen.blit(w_text, (WIN_WIDTH - 175, 533))

                h_text = self.fnt3.render(object.input_textH, True,  (120, 120, 120))
                screen.blit(h_text, (WIN_WIDTH - 175, 563))

                RED_text = self.fnt3.render(object.input_textRED, True,  (120, 120, 120))
                screen.blit(RED_text, (WIN_WIDTH - 177, 702))

                GREEN_text = self.fnt3.render(object.input_textGREEN, True,  (120, 120, 120))
                screen.blit(GREEN_text, (WIN_WIDTH - 118, 702))

                BLUE_text = self.fnt3.render(object.input_textBLUE, True,  (120, 120, 120))
                screen.blit(BLUE_text, (WIN_WIDTH - 58, 702))

                object.input_textName = process_input_text(object.input_textName, self.active1)
                object.input_textX = process_input_text(object.input_textX, self.active2)
                object.input_textY = process_input_text(object.input_textY, self.active3)
                object.input_textW = process_input_text(object.input_textW, self.active4)
                object.input_textH = process_input_text(object.input_textH, self.active5)
                object.input_textRED = process_input_text(object.input_textRED, self.active8)
                object.input_textGREEN = process_input_text(object.input_textGREEN, self.active9)
                object.input_textBLUE = process_input_text(object.input_textBLUE, self.active10)

                if keys[pg.K_RETURN]:
                    try:
                        if self.active1:
                            object.name = object.input_textName
                        if self.active2:
                            object.x = float(object.input_textX) * 6
                        if self.active3:
                            object.y = -float(object.input_textY) * 6
                        if self.active4:
                            object.width_obj = float(object.input_textW)
                        if self.active5:
                            object.height_obj = float(object.input_textH)
                        if self.active8:
                            object.RED = int(object.input_textRED)
                        if self.active9:
                            object.GREEN = int(object.input_textGREEN)
                        if self.active10:
                            object.BLUE = int(object.input_textBLUE)
                    except ValueError:
                        pass

                if not self.active1:
                    object.input_textName = object.name
                if not self.active2:
                    object.input_textX = str(round(object.x/6, 2))
                if not self.active3:
                    object.input_textY = str(-round(object.y/6, 2))
                if not self.active8:
                    object.input_textRED = str(object.RED)
                if not self.active9:
                    object.input_textGREEN = str(object.GREEN)
                if not self.active10:
                    object.input_textBLUE = str(object.BLUE)

                if self.aimed1:
                    screen.blit(self.aimed, (WIN_WIDTH-363, 298))
                else:
                    x = WIN_WIDTH-363
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        self.aimed1 = True
                x = WIN_WIDTH-363
                if not (x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height):
                    self.aimed1 = False

                if self.aimed2:
                    screen.blit(self.aimed, (WIN_WIDTH-281, 298))
                    if pg.mouse.get_pressed()[0]:
                        self.hud_selected = 2
                else:
                    x = WIN_WIDTH-281
                    if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                        self.aimed2 = True     
                x = WIN_WIDTH-281
                if not (x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height):
                    self.aimed2 = False
            
            
            
            
            if WIN_WIDTH-210 <= mouse_pos[0] <= WIN_WIDTH-210 + 27.5 and 720 <= mouse_pos[1] <= 720 + 20:
                    if pg.mouse.get_pressed()[0]:
                        self.switched = 1

            if WIN_WIDTH-182.5 <= mouse_pos[0] <= WIN_WIDTH-182.5 + 27.5 and 720 <= mouse_pos[1] <= 720 + 20:
                        if pg.mouse.get_pressed()[0]:
                            self.switched = 2
            
            if self.switched == 1:
                if self.hud_selected == 2:
                    self.object_hud1.set_alpha(self.menu_alpha)
                    screen.blit(self.object_hud21, (WIN_WIDTH-363, 232))
                    screen.blit(self.switcher, (WIN_WIDTH-210, 720))
                    if self.menu_alpha < 255:
                        self.menu_alpha += 3

                    


                    
                        
                    if self.active14:
                        screen.blit(self.area_active, input14)
                    if self.active15:
                        screen.blit(self.area_active, input15)
                    if self.active16:
                        screen.blit(self.area_active, input16)
                    if self.active17:
                        screen.blit(self.area_active, input17)
                    if self.active18:
                        screen.blit(self.area_active, input18)
                    
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if input14.collidepoint(mouse_pos):
                            self.active14 = True
                        else:
                            self.active14 = False
                        
                        if input15.collidepoint(mouse_pos):
                            self.active15 = True
                        else:
                            self.active15 = False
                        
                        if input16.collidepoint(mouse_pos):
                            self.active16 = True
                        else:
                            self.active16 = False
                        
                        if input17.collidepoint(mouse_pos):
                            self.active17 = True
                        else:
                            self.active17 = False
                            
                        if input18.collidepoint(mouse_pos):
                            self.active18 = True
                        else:
                            self.active18 = False
                    
                    mass_text = self.fnt3.render(object.input_textMass, True,  (120, 120, 120))
                    screen.blit(mass_text, (WIN_WIDTH - 175, 386))
                    
                    ax_text = self.fnt3.render(object.input_textAX, True,  (120, 120, 120))
                    screen.blit(ax_text, (WIN_WIDTH - 175, 562))
                    
                    ay_text = self.fnt3.render(object.input_textAY, True,  (120, 120, 120))
                    screen.blit(ay_text, (WIN_WIDTH - 175, 620))
                    
                    vx_text = self.fnt3.render(object.input_textVX, True,  (120, 120, 120))
                    screen.blit(vx_text, (WIN_WIDTH - 175, 444))
                    
                    vy_text = self.fnt3.render(object.input_textVY, True,  (120, 120, 120))
                    screen.blit(vy_text, (WIN_WIDTH - 175, 503))

                    object.input_textMass = process_input_text(object.input_textMass, self.active14)
                    object.input_textVX = process_input_text(object.input_textVX, self.active15)
                    object.input_textVY = process_input_text(object.input_textVY, self.active16)
                    object.input_textAX = process_input_text(object.input_textAX, self.active17)
                    object.input_textAY = process_input_text(object.input_textAY, self.active18)
        
                    if keys[pg.K_RETURN]:
                        try:
                            if self.active14:
                                object.mass = float(object.input_textMass)
                            if self.active15:
                                object.vx = float(object.input_textVX)
                            if self.active16:
                                object.vy = -float(object.input_textAY)
                            if self.active17:
                                object.ax = float(object.input_textAX)  
                            if self.active18:
                                object.ay = float(object.input_textAY)  
                        except ValueError:
                            pass
                    
                    if not self.active14:
                        object.input_textMass = str(round(object.mass, 2))
                    if not self.active15:
                        object.input_textVX = str(round(object.vx, 2))
                    if not self.active16:
                        object.input_textVY = str(round(object.vy, 2))
                    if not self.active17:
                        object.input_textAY = str(round(object.ax, 2))
                    if not self.active18:
                        object.input_textAY = str(round(object.ay, 2))
                    
                    
                    
                    if self.aimed1:
                        screen.blit(self.aimed, (WIN_WIDTH-363, 298))
                        if pg.mouse.get_pressed()[0]:
                            self.hud_selected = 1
                    else:
                        x = WIN_WIDTH-363
                        if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                            self.aimed1 = True
                    x = WIN_WIDTH-363
                    if not (x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height):
                        self.aimed1 = False

                    if self.aimed2:
                        screen.blit(self.aimed, (WIN_WIDTH-281, 298))
                    else:
                        x = WIN_WIDTH-281
                        if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                            self.aimed2 = True
                    x = WIN_WIDTH-281
                    if not (x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height):
                        self.aimed2 = False

            if self.switched == 2:
                if self.hud_selected == 2:
                    self.object_hud1.set_alpha(self.menu_alpha)
                    screen.blit(self.object_hud22, (WIN_WIDTH-363, 232))
                    screen.blit(self.switcher, (WIN_WIDTH-210, 720))
                    if self.menu_alpha < 255:
                        self.menu_alpha += 3

                        
                    if self.active19:
                        screen.blit(self.area_active, input19)
                    if self.active20:
                        screen.blit(self.area_active, input20)
          
                    
                    if event.type == pg.MOUSEBUTTONDOWN:
                        if input19.collidepoint(mouse_pos):
                            self.active19 = True
                        else:
                            self.active19 = False
                        
                        if input20.collidepoint(mouse_pos):
                            self.active20 = True
                        else:
                            self.active20 = False
                        
                    
                    FX_text = self.fnt3.render(object.input_textFX, True,  (120, 120, 120))
                    screen.blit(FX_text, (WIN_WIDTH - 175, 386))
                    
                    FY_text = self.fnt3.render(object.input_textFY, True,  (120, 120, 120))
                    screen.blit(FY_text, (WIN_WIDTH - 175, 445))
                    

                    object.input_textFX = process_input_text(object.input_textFX, self.active19)
                    object.input_textFY = process_input_text(object.input_textFY, self.active20)
    
        
                    if keys[pg.K_RETURN]:
                        try:
                            if self.active19:
                                object.force_x = float(object.input_textFX)
                            if self.active20:
                                object.force_y = float(object.input_textFY)
                        except ValueError:
                            pass
                    
                    if not self.active19:
                        object.input_textFX = str(round(object.force_x, 2))
                    if not self.active20:
                        object.input_textFY = str(round(object.force_y, 2))


                    if self.aimed1:
                        screen.blit(self.aimed, (WIN_WIDTH-363, 298))
                        if pg.mouse.get_pressed()[0]:
                            self.hud_selected = 1
                    else:
                        x = WIN_WIDTH-363
                        if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                            self.aimed1 = True
                    x = WIN_WIDTH-363
                    if not (x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height):
                        self.aimed1 = False

                    if self.aimed2:
                        screen.blit(self.aimed, (WIN_WIDTH-281, 298))
                    else:
                        x = WIN_WIDTH-281
                        if x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height:
                            self.aimed2 = True
                    x = WIN_WIDTH-281
                    if not (x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height):
                        self.aimed2 = False
        else:
            self.menu_alpha = 0
                  
    def handler(self, a, b):
        global event, keys, mouse_pos, mouse_buttons, current_time, clock
        
        event = a
        clock = b.get_time() / 1000
        keys = pg.key.get_pressed()
        mouse_pos = pg.mouse.get_pos()
        mouse_buttons = pg.mouse.get_pressed()
        current_time = time.perf_counter()
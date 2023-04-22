import pygame
import time
 
WIDTH = 1280  
HEIGHT = 720
FPS = 100
G = 6.67430/(10**(11))
k = 1_000_000 #метров в пикселе на начало игры
 
w_x = -600_000_000 #координаты угла игрового окна 
w_y = -450_000_000 #на общей карте
 
vrem_k = 100 # коэффициент ускорения времени на начало игры
 
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Гравитация")
clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 36)
text_FPS = font.render('FPS: '+str(FPS), True,'green')
text_vrem_k = font.render('Время: x'+str(vrem_k), True,'green')
                
class Ball():
    def __init__(self,real_x,real_y,real_r,m,colour):
        self.real_x = real_x
        self.real_y = real_y
        self.real_r = real_r
        self.m = m
        self.colour = colour
        self.speed = [0,0]
        self.a = [0,0]
        self.f = [0,0]
        self.trace_count = 0
        self.trace = []
        self.status = True # шар ещё существует
 
    def update(self):
        self.a[0] = (self.f[0]/self.m)*(vrem_k**2)/FPS**2
        self.a[1] = (self.f[1]/self.m)*(vrem_k**2)/FPS**2
 
        self.speed[0] += self.a[0]
        self.speed[1] += self.a[1]
        
        self.real_x += self.speed[0]
        self.real_y += self.speed[1]
 
        # траектория:
        self.trace_count += (self.speed[0]**2+self.speed[1]**2)**0.5
        if self.trace_count/k >= 5:
            self.trace_count = 0
            self.trace.append((self.real_x,
                                self.real_y))
        if len(self.trace)>1000:
            self.trace.pop(0)
            
    def draw(self):
        pygame.draw.circle(screen,
                           self.colour,
                           ((self.real_x - w_x)/k,
                            (self.real_y - w_y)/k),
                           self.real_r/k
                           )
        for i in self.trace:
            pygame.draw.circle(screen,
                           self.colour,
                           ((i[0] - w_x)/k,
                                (i[1] - w_y)/k),
                            1)
 
balls = []        
 
#Земля:
p = Ball(0,0,6371000,5.9722*10**24,'blue')
balls.append(p)
 
#Луна:
p = Ball(-363104000,0,1737100,7.35*10**22,'grey')
balls.append(p)
p.speed[1] = 1080*vrem_k/FPS
 
#МКС:
'''p = Ball(0,6_371_000+415_000,45,440_075,'yellow')
balls.append(p)
p.speed[0] = 7700*vrem_k/FPS'''
 
#Солнце
p = Ball(149.6*10**9,0,696_000_000,1.9891*10**30,'red')
balls.append(p)
balls[0].speed[1]+= 29782.77*vrem_k/FPS
balls[1].speed[1]+= 29782.77*vrem_k/FPS
 
tick = 0
tm = time.time()
running = True
while running:
    clock.tick(FPS)
    tick+=1
    if tick == 100:
        tick = 0
        text_FPS = font.render('FPS: '+str(int((100/(time.time() - tm)))), True,
                  'green')
        
        tm = time.time()
        
    #обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Найдём место на реальной карте,
            #куда хочет попасть игрок:
            xx = event.pos[0]
            yy = event.pos[1]
            jump_x = w_x + xx*k
            jump_y = w_y + yy*k
            
            if event.button == 4:
                k = k*0.85
 
                w_x = jump_x - xx*k
                w_y = jump_y - yy*k
                
            if event.button == 5:
                k = k/0.85
        
                w_x = jump_x - xx*k
                w_y = jump_y - yy*k
 
            if event.button == 3:
                #Юпитер:
                #balls.append(Ball(jump_x,jump_y,71492000,1.8986*10**27,'orange'))
 
                #Солнце:
                #balls.append(Ball(jump_x,jump_y,696_000_000,1.9891*10**30,'red'))
 
                #Чёрная дыра
                #balls.append(Ball(jump_x,jump_y,10_000_000,1.9891*10**30*4000000,'pink'))
 
                #Земля
                balls.append(Ball(jump_x,jump_y,6371000,5.9722*10**24,'blue'))
 
            if event.button == 2:
                if vrem_k == 100_0000:
                    vrem_k = 1
                    for i in balls:
                        i.speed[0]/=100_0000
                        i.speed[1]/=100_0000
                else:
                    vrem_k *= 10
                    for i in balls:
                        i.speed[0]*=10
                        i.speed[1]*=10
                        
                text_vrem_k = font.render('Время: x'+str(vrem_k), True,'green')
                
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0] == True:
                w_x -= event.rel[0]*k
                w_y -= event.rel[1]*k
            
    collisions = []
    #считаем действующие силы на каждое тело
    for i in range(len(balls)):
        for j in range(i+1,len(balls)):
            dx = balls[j].real_x-balls[i].real_x
            dy = balls[j].real_y-balls[i].real_y
            d = (dx**2+dy**2)**0.5
            ff = G*balls[i].m*balls[j].m/d**2
            
            balls[i].f[0] += dx*ff/d
            balls[i].f[1] += dy*ff/d
 
            balls[j].f[0] -= dx*ff/d
            balls[j].f[1] -= dy*ff/d
 
            if balls[i].real_r > d - balls[j].real_r:
                collisions.append((i,j))
                
    #обработаем столкновения:
    for i in collisions:
        t1 = balls[i[0]]
        t2 = balls[i[1]]
        if t1.status and t2.status:
            t1.status = False
            t2.status = False
            if t1.real_r > t2.real_r:
                c = t1.colour
            else:
                c = t2.colour
                
            t = Ball((t1.real_x*t1.m+t2.real_x*t2.m)/(t1.m+t2.m),
                            (t1.real_y*t1.m+t2.real_y*t2.m)/(t1.m+t2.m),
                            (t1.real_r**3+t2.real_r**3)**(1/3),
                            t1.m + t2.m,
                            c)
            t.speed[0] = (t1.m*t1.speed[0]+t2.m*t2.speed[0])/(t1.m+t2.m)
            t.speed[1] = (t1.m*t1.speed[1]+t2.m*t2.speed[1])/(t1.m+t2.m)
            balls.append(t)
    
 
 
    tt = []
    for ball in balls:
        if ball.status:
            tt.append(ball)
    balls = tt
            
    for ball in balls:
        ball.update()
        ball.f = [0,0]
        
    #рисуем
    screen.fill('black')
    
    for ball in balls:
        ball.draw()
        
    screen.blit(text_FPS, (10, 10))
    screen.blit(text_vrem_k, (10, 50))
    pygame.display.update()
pygame.quit()

# 
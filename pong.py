import pygame
import random
import time

pygame.init()
win =  pygame.display.set_mode((900,500))

pygame.display.set_caption('Ping_Pong')
pygame.mixer.music.load("c3c37baf3cd71bd.mp3")

x = 53
y = 168
x2 = 830
y2 = 168
x3 = 450
y3 = 250
x4 = 830
y4 = 480 
width = 21
heigth = 130
scr = 0
scr2 = 0
score = 0
score2 = 0
speed = 7
speed2 = 8
y_sped = -3
WHITE = (255, 255, 255)

f1 = pygame.font.SysFont('ofont.ru_CGF Arch ReactorRUS', 100)
f4 = pygame.font.SysFont('ofont.ru_CGF Arch ReactorRUS', 90)
f3 = pygame.font.SysFont('ofont.ru_CGF Arch ReactorRUS', 90)
f2 = pygame.font.SysFont('ofont.ru_CGF Arch ReactorRUS', 100)
text1 = f1.render(str(score), False, (WHITE))
text2 = f2.render(str(score2), False, (WHITE))
 
win.blit(text1, (420, 480))
win.blit(text2, (480, 480))

def start():
    global x
    global x2
    global x3
    global y
    global y2
    global y3
    global speed
    global y_sped
    global speed2
    x = 53
    y = 168
    x2 = 830
    y2 = 168
    x3 = 450
    y3 = 250
    speed2 = 8
    a = random.randint(1,2)
    b = random.randint(1,2)
    if a == 1:
        speed2 *= -1
    if b == 1:
        y_sped *= -1
    pygame.draw.rect(win, WHITE, (0, 499, 900, 1))
    pygame.draw.rect(win, WHITE, (0, 0.9, 900, 1))
    rec2 = pygame.draw.rect(win, (255, 255, 255), (x2, y2, width, heigth)) 
    rec = pygame.draw.rect(win, (255, 255, 255), (x, y, width, heigth))
    pygame.draw.line(win, WHITE, [450, 500], [450, -1], 3)
    cir = pygame.draw.circle(win, WHITE, (x3, y3), 12)

def drawing():
    pygame.draw.rect(win, WHITE, (0, 499, 900, 1))
    pygame.draw.rect(win, WHITE, (0, 0.9, 900, 1))
    rec2 = pygame.draw.rect(win, (255, 255, 255), (x2, y2, width, heigth)) 
    rec = pygame.draw.rect(win, (255, 255, 255), (x, y, width, heigth))
    pygame.draw.line(win, WHITE, [450, 500], [450, -1], 3)
    cir = pygame.draw.circle(win, WHITE, (x3, y3), 12)

def goal1():
    global score
    global scr
    time.sleep(0.2)
    time.sleep(0.2)
    time.sleep(0.2)
    time.sleep(0.2)
    scr += 1 
    score = scr
    text1 = f1.render(str(score), False, (WHITE))
    win.blit(text1, (384, 25))

def goal2():
    global score2
    global scr2 
    time.sleep(0.2)
    time.sleep(0.2)
    time.sleep(0.2)
    time.sleep(0.2)
    scr2 += 1 
    score2 = scr2
    text2 = f2.render(str(score), False, (WHITE))
    win.blit(text2, (480, 25))



run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    if x3 <= x+width:
        if y3 > y:
            if y3 < y+heigth:
                pygame.mixer.music.play(1)
                speed2 *= -1

    if x3 >= x2:
        if y3 > y2:
            if y3 < y2+heigth:
                pygame.mixer.music.play(1)
                speed2 *= -1
                

    if y3 < 13 or y3 > 500 - 13:
        y_sped *= -1
        pygame.mixer.music.play(1)

    x3 += speed2
    y3 += y_sped 


    keys2 = pygame.key.get_pressed()
    if keys2[pygame.K_w] and y > 5:
        y -= speed
    if keys2[pygame.K_s] and y < 500 - heigth - 7:
        y += speed
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y2 > 5:
        y2 -= speed
    if keys[pygame.K_DOWN] and y2 < 500 - heigth - 7:
        y2 += speed
    if event.type == pygame.K_1 and event.key == pygame.K_ESCAPE:
        run = False

    win.fill((0, 100, 0))
    text1 = f1.render(str(score), False, (WHITE))
    text2 = f2.render(str(score2), False, (WHITE))
    text3 = f3.render('Победил Игрок 1', True, (WHITE))
    text4 = f4.render('Победил Игрок 2', True, (WHITE))
    win.blit(text1, (384, 25))
    win.blit(text2, (480, 25))
    if scr == 5:
        win.blit(text3, (230, 200))
        time.sleep(9)
        run = False
    if scr2 == 5:
        time.sleep(9)
        win.blit(text4, (230, 200))
        run = False
    if x3 >= 890:
        goal1()
        time.sleep(0.5)
        start()
    if x3 <= 15:
        goal2()
        time.sleep(0.5)
        start()
        
    drawing()
    pygame.display.update()

pygame.quit()
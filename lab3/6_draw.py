import pygame
from pygame.draw import *

GREY = (200, 200, 200)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (240, 240, 200)
pi = 3.14

pygame.init()

FPS = 30
screen = pygame.display.set_mode((450, 500))
surface = pygame.Surface((450,500), pygame.SRCALPHA)
surface2 = pygame.Surface((450,500))

surface2.fill((180, 210, 240))
# surface.fill((255,0,0, 20))
# screen.blit(surface, (0,0))

#rect(screen, (180, 210, 240), (0, 0, 500, 350))
rect(surface2, GREY, (0, 250, 500, 350))
rect(surface2, BLACK, (-5, 250, 510, 300), 1)

# halo

for i in range(0, 255, 1):
    circle(surface, (240, 240, 200, i), (300, 90), 100 - 2 * i)
screen.blit(surface, (0, 0))

for i in range(0, 255, 1):
    circle(surface, (240, 240, 200, i), (190, 90), 30 - 0.4 * i)
screen.blit(surface, (0, 0))

for i in range(0, 255, 1):
    circle(surface, (240, 240, 200, i), (410, 90), 30 - 0.4 * i)
screen.blit(surface, (0, 0))

for i in range(0, 255, 1):
    circle(surface, (240, 240, 200, i), (300, 200), 30 - 0.4 * i)
screen.blit(surface, (0, 0))

circle(surface, (240, 240, 200, 50), (300, 90), 120, 20)
screen.blit(surface, (0, 0))
line(surface, (240, 240, 200, 100),(180, 90), (420, 90), 15)
screen.blit(surface, (0, 0))
line(surface, (240, 240, 200, 100),(300, 0), (300, 210), 15)
screen.blit(surface, (0, 0))
circle(screen, (240, 240, 200), (300, 90), 15)
circle(screen, (240, 240, 200), (190, 90), 10)
circle(screen, (240, 240, 200), (410, 90), 10)
circle(screen, (240, 240, 200), (300, 200), 10)

# rotated_surface = pygame.transform.rotate(surface, 20)
# rect = rotated_surface.get_rect(center = (100, 100))
# screen.blit(rotated_surface, (rect.x, rect.y))



# fishing rod

line(surface2, BLACK, (180, 290), (200, 240), 3)

x1 = 200; y1 = 240; h = 20
for i in range(12):
    x2 = x1 + 13
    y2 = y1 - h
    line(surface2, BLACK, (x1, y1), (x2, y2), 3)
    x1 = x2; y1 = y2; h -= 1

# hole

ellipse(surface2, (40, 55, 55), (240, 315, 180, 60))
ellipse(surface2, BLACK, (240, 315, 180, 60), 1)

ellipse(surface2, (50, 100, 80), (260, 335, 140, 40))
ellipse(surface2, BLACK, (260, 335, 140, 40), 1)

line(surface2, BLACK, (355, 65), (355, 350))

# bear
ellipse(surface2, GREY, (100, 120, 100, 65))
ellipse(surface2, BLACK, (100, 120, 100, 65), 1)
ellipse(surface2, GREY, (20, 170, 160, 260))
ellipse(surface2, BLACK, (20, 170, 160, 260), 1)
ellipse(surface2, GREY, (100, 360, 100, 80))
ellipse(surface2, BLACK, (100, 360, 100, 80), 1)
ellipse(surface2, GREY, (165, 415, 80, 30))
ellipse(surface2, BLACK, (165, 415, 80, 30), 1)
ellipse(surface2, GREY, (150, 230, 60, 30))
ellipse(surface2, BLACK, (150, 230, 60, 30), 1)

ellipse(surface2, GREY, (100, 125, 20, 7))
ellipse(surface2, GREY, (100, 125, 20, 20))
ellipse(surface2, GREY, (100, 125, 20, 20))

arc(surface2, BLACK, (100, 125, 20, 7), 0, pi/2, 1)
arc(surface2, BLACK, (100, 125, 20, 25), pi/2, pi, 1)
arc(surface2, BLACK, (100, 125, 20, 20), pi, 3*pi/2, 1)

line(surface2, BLACK, (110, 145), (120, 128), 1)
#pygame.draw.arc(surface2, BLACK, (101, 115, 20, 30), 3*pi/2, 2*pi, 1)

circle(surface2, BLACK, (145, 143), 4)
circle(surface2, BLACK, (200, 150), 4)

# bear mouth

x1 = 166; y1 = 170; h = 0
line(surface2, BLACK, (146, 170), (x1, y1))
for i in range(6):
    x2 = x1 + 5
    y2 = y1 - h
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    x1 = x2; y1 = y2; h += 0.5



# fish fins 1

a1 = []

x1 = 330; y1 = 410; h = 6
for i in range(8):
    x2 = x1 - 4
    y2 = y1 - h
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a1.append((x1, y1)); a1.append((x2, y2))
    x1 = x2; y1 = y2; h -= 1

a2 = []
x1 = 330; y1 = 400; h = -9
for i in range(8):
    x2 = x1 - h
    y2 = y1 - 3
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a2.append((x1, y1)); a2.append((x2, y2))
    x1 = x2; y1 = y2; h += 2

a2.reverse()
a1 = a1 + a2

polygon(surface2, (180, 140, 140), a1)
polygon(surface2, BLACK, a1, 1)

# fish fins 2

a1 = []

x1 = 310; y1 = 420; h = 6
for i in range(5):
    x2 = x1 - 2
    y2 = y1 + h
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a1.append((x1, y1)); a1.append((x2, y2))
    x1 = x2; y1 = y2; h -= 1

a2 = []
x1 = 320; y1 = 435; h = -5
for i in range(5):
    x2 = x1 - h
    y2 = y1 - 4
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a2.append((x1, y1)); a2.append((x2, y2))
    x1 = x2; y1 = y2; h += 2

a1 = a1 + a2

polygon(surface2, (180, 140, 140), a1)
polygon(surface2, BLACK, a1, 1)

# fish fins 2

a1 = []

x1 = 350; y1 = 410; h = 6
for i in range(5):
    x2 = x1 + 2
    y2 = y1 + h
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a1.append((x1, y1)); a1.append((x2, y2))
    x1 = x2; y1 = y2; h -= 1

a2 = []
x1 = 375; y1 = 415; h = -7
for i in range(5):
    x2 = x1 + h
    y2 = y1 - 4
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a2.append((x1, y1)); a2.append((x2, y2))
    x1 = x2; y1 = y2; h += 2

a1 = a1 + a2

polygon(surface2, (180, 140, 140), a1)
polygon(surface2, BLACK, a1, 1)

# fish
a1 = []

x1 = 300; y1 = 420; h = 10
for i in range(8):
    x2 = x1 + 10
    y2 = y1 - h
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a1.append((x1, y1)); a1.append((x2, y2))
    x1 = x2; y1 = y2; h -= 2

a1.reverse()

x1 = 300; y1 = 420; h = 3
for i in range(8):
    x2 = x1 + 10
    y2 = y1 + h
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a1.append((x1, y1)); a1.append((x2, y2))
    x1 = x2; y1 = y2; h -= 1.7

polygon(surface2, (150, 150, 150), a1)
polygon(surface2, BLACK, a1, 1)

# fish tail

a1 = []

x1 = 300; y1 = 420; h = 0
for i in range(8):
    x2 = x1 - 5
    y2 = y1 + h
    line(surface2, BLACK, (x1, y1), (x2, y2), 1)
    a1.append((x1, y1)); a1.append((x2, y2))
    x1 = x2; y1 = y2; h -= 0.4

a1.append((280, 440))
a1.append((300, 420))

polygon(surface2, (150, 150, 150), a1)
polygon(surface2, BLACK, a1, 1)

# fish eye

circle(surface2, (100, 100, 180), (360, 400), 5)
circle(surface2, BLACK, (360, 400), 5, 1)
ellipse(surface2, WHITE, [355, 398, 5, 3])


surface3 = surface2.copy()
pygame.transform.flip(surface3, True, False)

screen.blit(surface3, (0, 0))
screen.blit(surface, (0, 0))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
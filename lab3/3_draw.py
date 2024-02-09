import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((230, 200, 220))

circle(screen, (255, 255, 0), (200, 190), 100)
circle(screen, (255, 0, 0), (160, 170), 20)
circle(screen, (0, 0, 0), (160, 170), 9)
circle(screen, (255, 0, 0), (240, 170), 15)
circle(screen, (0, 0, 0), (240, 170), 7)

polygon(screen, (0, 0, 0), [(180, 160), (184, 152), (119, 119), (115, 128)])
polygon(screen, (0, 0, 0), [(220, 170), (217, 162), (277, 140), (280, 148)])
polygon(screen, (0, 0, 0), [(150, 250), (250, 250), (250, 230), (150, 230)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
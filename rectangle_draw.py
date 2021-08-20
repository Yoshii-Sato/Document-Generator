"""Place a rectangle with the mouse."""

import pygame
from pygame.locals import *

RED = (255,0,0)
BLUE = (0,0,255)
GRAY = (127,127,127)

pygame.init()
screen = pygame.display.set_mode((600,600))

start = (0, 0)
size = (0, 0)
drawing = False
rect_list = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key == K_d:
                running = False
            if event.key == K_c:
                screen.fill(GRAY)

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]
            rect = pygame.Rect(start, size)
            rect_list.append(rect)
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start[0], end[1] - start[1]

    screen.fill(GRAY)
    for rect in rect_list:
        pygame.draw.rect(screen, RED, rect, 3)
    pygame.draw.rect(screen, BLUE, (start, size), 2)
    pygame.draw.ellipse(screen, RED, (350, 20, 120, 100), 1)
    pygame.display.update()

pygame.quit()
# pygame.draw.rect(img, color, (x,y,w,h))
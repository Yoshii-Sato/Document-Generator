import pygame
from pygame.locals import *

RED = (255, 0, 0)
GREEN = (0,255,0)
GRAY = (150, 150, 150)

pygame.init()
w, h = 640, 240
screen = pygame.display.set_mode((w, w))
running = True

img = pygame.image.load('pictures/bird.png')
img.convert()
rect = img.get_rect()
rect.center = w//2, h//2

img0 = pygame.image.load('pictures/bird.png')
img0.convert()
rect0 = img0.get_rect()
pygame.draw.rect(img0, GREEN, rect0, 1)

center = w//2, h//2
img = img0rect = img.get_rect()
rect.center = center

angle = 0
scale = 1

moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == KEYDOWN:
            if event.key == K_d:
                running = False

        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

        if event.type == KEYDOWN:
            if event.key == K_r:
                if event.mod & KMOD_SHIFT:
                    angle -= 10
                else:
                    angle += 10
                img = pygame.transform.rotozoom(img0, angle, scale)
            elif event.key == K_s:
                if event.mod & KMOD_SHIFT:
                    scale /= 1.1
                else:
                    scale *= 1.1
                img = pygame.transform.rotozoom(img0, angle, scale)
    
    # rect = img.get_rect()
    # rect.center = center

    screen.fill(GRAY)
    screen.blit(img, rect)
    pygame.draw.rect(screen, RED, rect, 1)
    pygame.display.update()

pygame.quit()
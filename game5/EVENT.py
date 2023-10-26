import random
import sys
import pygame

from background import draw_bg
from game_parameters import *     #import everything


#Initialize Pygame
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Beech")

#Main loop
running = True
background = screen.copy()
draw_bg(background)

while running:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("you pressed da down key")
            if event.key == pygame.K_UP:
                print("you pressed da up key")
            if event.key == pygame.K_LEFT:
                print("you pressed da left key")
            if event.key == pygame.K_RIGHT:
                print("you pressed da rite key")

    # draw bg
    screen.blit(background, (0, 0))

    # update the display
    pygame.display.flip()

    # limit time frame
    # clock.tick(60)

pygame.quit()
sys.exit()
import pygame
import sys
import random

#Initialize Pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64
#
# #define colors
# BLUE = (0,0,255)
# BROWN = (224,161,52)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Beech")

#load game font
custom_font = pygame.font.Font("assets/fonts/Brainfish_Rush.ttf", size=128)

#define function for bg
def draw_bg(surf):
    #load our tiles
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()
    #png transparency to get rid of unnecessary bg
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    #fill screen
    for x in range(0,screen_width,tile_size):
        for y in range(0,screen_height,tile_size):
            surf.blit(water, (x,y))
    #draw sand
    for x in range(0,screen_width,tile_size):
        surf.blit(sand, (x,screen_height-tile_size))

    #add seagrass randomly at bottom
    for _ in range(7):
        x = random.randint(0, screen_width)
        surf.blit(seagrass, (x, screen_height-tile_size*2))

    #draw text
    text = custom_font.render('chomp', True, (255,0,0))
    surf.blit(text, (screen_width/2 - text.get_width()/2,screen_height/2 - text.get_height()/2))

    #draw fishes
    def draw_fishes
#Main loop
running = True
background = screen.copy()
draw_bg(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.quit:
            running = False
    #draw bg
    screen.blit(background, (0,0))

    # update display
    pygame.display.flip()

pygame.quit
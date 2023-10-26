import pygame
import random
from game_parameters import *

def draw_bg(surf):
    #load our tiles
    water = pygame.image.load("../assets/sprites/water.png").convert() #"../" looks for out of the current directory
    sand = pygame.image.load("../assets/sprites/sand.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
    #png transparency to get rid of unnecessary bg
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))
    # load game font
    custom_font = pygame.font.Font("../assets/fonts/Brainfish_Rush.ttf", size=80)

    #fill screen
    for x in range(0,SCREEN_WIDTH,TILE_SIZE):
        for y in range(0,SCREEN_HEIGHT,TILE_SIZE):
            surf.blit(water, (x,y))
    #draw sand
    for x in range(0,SCREEN_WIDTH,TILE_SIZE):
        surf.blit(sand, (x,SCREEN_HEIGHT-TILE_SIZE))

    #add seagrass randomly at bottom
    for _ in range(7):
        x = random.randint(0, SCREEN_WIDTH)
        surf.blit(seagrass, (x, SCREEN_HEIGHT-TILE_SIZE*2))

    #draw text
    text = custom_font.render('chomp', True, (255,0,0))
    surf.blit(text, (SCREEN_WIDTH/2 - text.get_width()/2,text.get_height()/4))

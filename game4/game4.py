import pygame
import sys
import random
import time

clock = pygame.time.Clock()

from fish import Fish, fishes
#importing a class and a sprite group

#Initialize Pygame
pygame.init()

#screen dimensions
screen_width = 800
screen_height = 600
tile_size = 64

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Beech")

#load game font
custom_font = pygame.font.Font("../assets/fonts/Brainfish_Rush.ttf", size=128)

def draw_bg(surf):
    #load our tiles
    water = pygame.image.load("../assets/sprites/water.png").convert() #"../" looks for out of the current directory
    sand = pygame.image.load("../assets/sprites/sand.png").convert()
    seagrass = pygame.image.load("../assets/sprites/seagrass.png").convert()
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

#Main loop
running = True
background = screen.copy()
draw_bg(background)
for _ in range(5):
    fishes.add(Fish(random.randint(screen_width, screen_width*1.5), random.randint(tile_size, screen_height - tile_size)))

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
    #draw bg
    screen.blit(background, (0,0))

    #update fish location
    fishes.update()

    #check if any fish off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width: #use tile_size
            fishes.remove(fish) #remove fish from sprite group
            fishes.add(Fish(random.randint(screen_width, screen_width * 1.5),
                            random.randint(tile_size, screen_height - tile_size)))

    #draw fish
    fishes.draw(screen)

    #update the display
    pygame.display.flip()

    #limit time frame
    clock.tick(60)

pygame.quit()
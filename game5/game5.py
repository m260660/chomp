import pygame
import sys
import random
from game_parameters import *
#from EVENT import *
from background import draw_bg
from fish import Fish, fishes
from player import Player

#initialize pygame
pygame.init()

#create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Beech")

#clock object
clock = pygame.time.Clock()

#Main loop
running = True
background = screen.copy()
draw_bg(background)

#draw fish on screen
for _ in range(5):
    fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH*1.5), random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

#create a player fish
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

while running:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            running = False
        #control fish with keyboard
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                print("you pressed da down key")
                player.move_down()
            if event.key == pygame.K_UP:
                print("you pressed da up key")
                player.move_up()
            if event.key == pygame.K_LEFT:
                print("you pressed da left key")
                player.move_left()
            if event.key == pygame.K_RIGHT:
                print("you pressed da rite key")
                player.move_right()

    # draw bg
    screen.blit(background, (0, 0))

    #draw green fish
    fishes.update()
    #draw orange player fish
    player.update()

    # check if any fish off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:  # use tile_size
            fishes.remove(fish)  # remove fish from sprite group
            fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50),
                            random.randint(TILE_SIZE, SCREEN_HEIGHT - 2*TILE_SIZE)))

    fishes.draw(screen)
    player.draw(screen)

    # update the display
    pygame.display.flip()

    # limit time frame
    clock.tick(60)

pygame.quit()
sys.exit()
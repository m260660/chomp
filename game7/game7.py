import pygame
import sys
import random
from game_parameters import *
#from EVENT import *
from background import draw_bg
from fish import Fish, fishes, add_fish
from player import Player
from enemy import *


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
add_fish(5)

#draw da enemies on screen
add_enemies(6)

#create a player fish
player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#initialize score
score = 0
score_font = pygame.font.Font("../assets/fonts/Black_Crayon.ttf", size=80)
#text = score_font.render(f'{score}', True, (255,0,0))

#chomp sound
chomp = pygame.mixer.Sound("../assets/sounds/chomp.wav")

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

            #Event.key includes letters, but event.type is just up and down motions

    # draw bg
    screen.blit(background, (0, 0))

    #draw green fish
    fishes.update()
    #draw enemies
    enemies.update()
    #draw orange player fish
    player.update()

    #check for player and green fish collisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        #play chomp sound
        pygame.mixer.Sound.play(chomp)
        #score = score + 1
        score += len(result)
        # draw more green fish on screen
        add_fish(len(result))

    # check for player and enemy collisions
    result = pygame.sprite.spritecollide(player, enemies, True)
    if result:
        # play chomp sound
        pygame.mixer.Sound.play(chomp) #change sound
        # score = score + 1
        # score += len(result)
        # draw more green fish on screen
        add_enemies(len(result))

    # check if any fish off the screen
    for fish in fishes:
        if fish.rect.x < -fish.rect.width:  # use tile_size
            fishes.remove(fish)  # remove fish from sprite group
            add_fish(1)
            # fishes.add(Fish(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50), same as line above
            #                 random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

    # check if any fish off the screen
    for enemy in enemies:
        if enemy.rect.x < -enemy.rect.width:  # use tile_size
            enemies.remove(enemy)  # remove fish from sprite group
            add_enemies(1)
            # enemies.add(Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 50), same as line above
            #                 random.randint(TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE)))

    #draw game objects
    fishes.draw(screen)
    player.draw(screen)
    enemies.draw(screen)

    #draw the score on the screen
    text = score_font.render(f'{score}', True, (255, 0, 0))
    screen.blit(text,(SCREEN_WIDTH-TILE_SIZE, 0))

    # update the display
    pygame.display.flip()

    # limit time frame
    clock.tick(60)

pygame.quit()
sys.exit()
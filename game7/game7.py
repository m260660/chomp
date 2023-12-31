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
hurt = pygame.mixer.Sound("../assets/sounds/hurt.wav")
bubbles = pygame.mixer.Sound("../assets/sounds/bubbles.wav")

#add alternate fish image
life_icon = pygame.image.load("../assets/sprites/orange_fish_alt.png").convert()
life_icon.set_colorkey((0,0,0)) #Anything black in the image is now transparent

#set the number of lives
lives = NUM_LIVES

while lives > 0 and running: #lets user play until over AND quit if they are done
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
        # play hurt sound
        pygame.mixer.Sound.play(hurt)
        #play hurt sound
        lives -= 1
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

    #draw lives in lower left corner
    for i in range(lives):
        screen.blit(life_icon, (i*TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))

    # update the display
    pygame.display.flip()

    # limit time frame
    clock.tick(60)
#once all lives are gone
#create new bg when game over
screen.blit(background,(0,0))

#show game over message and show final score
message = score_font.render("GAME OVER!",True, (255,0,0))
screen.blit(message, (SCREEN_WIDTH/2 - message.get_width()/2, SCREEN_HEIGHT/2 - message.get_height()/2))
score_text = score_font.render(f"Score: {score}", True, (0,255,0))
screen.blit(score_text, (SCREEN_WIDTH/2 -score_text.get_width()/2, SCREEN_HEIGHT/2 - 3*score_text.get_height()/2))

#update display
pygame.display.flip()

#play game over sound effect
pygame.mixer.Sound.play(bubbles)

#wait for user to exit game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

pygame.quit()
sys.exit()
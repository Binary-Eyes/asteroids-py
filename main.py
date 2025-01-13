import pygame
from constants import *
from pygame import display
from pygame import time
from player import Player

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    deltaTime = 0.0
    gameClock = time.Clock();
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update frame
        deltaTime = gameClock.tick(60.0)/1000.0
        player.update(deltaTime)

        # draw frame
        screen.fill((0,0,0))        
        player.draw(screen)
        display.flip()

if __name__ == "__main__":
    main()
    
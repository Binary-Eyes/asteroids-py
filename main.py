import pygame
from pygame import display
from pygame import time
from constants import *

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    deltaTime = 0.0
    gameClock = time.Clock();
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        display.flip()
        deltaTime = gameClock.tick(60.0)/1000.0


if __name__ == "__main__":
    main()
    
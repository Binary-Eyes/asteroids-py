import pygame
from constants import *
from pygame import display
from pygame import time
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print('Starting asteroids!')
    print(f'Screen width: {SCREEN_WIDTH}')
    print(f'Screen height: {SCREEN_HEIGHT}')
    pygame.init()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    deltaTime = 0.0
    gameClock = time.Clock();
    screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # update frame
        deltaTime = gameClock.tick(60.0)/1000.0
        for entry in updatable:
            entry.update(deltaTime)

        for entry in asteroids:
            collision_detected = entry.check_collision(player)
            if collision_detected:
                print('Game Over!')
                return

        # draw frame
        screen.fill((0,0,0))
        for entry in drawable:
            entry.draw(screen)

        display.flip()

if __name__ == "__main__":
    main()
    
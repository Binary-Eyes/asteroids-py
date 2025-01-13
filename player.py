import pygame
import circleshape
from constants import *

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0

     # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, deltaTime):
        keys = pygame.key.get_pressed()
        
        # rotate
        if keys[pygame.K_a]:
            self.rotation -= PLAYER_TURN_SPEED*deltaTime
        if keys[pygame.K_d]:
            self.rotation += PLAYER_TURN_SPEED*deltaTime
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        
        # move
        thrust = 0
        if keys[pygame.K_w]:
            thrust = +1
        if keys[pygame.K_s]:
            thrust = -1
        velocity = forward*thrust*deltaTime
        self.position += velocity*PLAYER_SPEED


    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

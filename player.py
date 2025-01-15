import pygame
import circleshape
from constants import *
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0.0
        self.velocity = pygame.Vector2(0, 0)
        self.forward = pygame.Vector2(0, 1)

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
        if keys[pygame.K_LEFT]:
            self.rotation -= PLAYER_TURN_SPEED*deltaTime
        if keys[pygame.K_RIGHT]:
            self.rotation += PLAYER_TURN_SPEED*deltaTime
        self.forward = pygame.Vector2(0,1).rotate(self.rotation)
        
        # move
        thrust = 0
        if keys[pygame.K_UP]:
            thrust = +1
        if keys[pygame.K_DOWN]:
            thrust = -1
        
        self.velocity += self.forward*deltaTime*thrust*PLAYER_THRUST
        self.position += self.velocity

        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = self.forward*PLAYER_SHOT_SPEED

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

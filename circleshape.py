import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def check_collision(self, other):
        combined = self.radius + other.radius
        return self.position.distance_to(other.position) <= combined

    def update(self, deltaTime):
        pass

    def draw(self, screen):
        pass

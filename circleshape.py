from pygame.sprite import Sprite
from pygame import Vector2

class CircleShape(Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "container"):
            super().__init__(self.containers)
        else:
            super().__init__()
        
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, deltaTime):
        pass

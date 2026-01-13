import pygame

class CircleShape(pygame.sprite.Sprite):
    containers = ()

    def __init__(self, x, y, radius):
        super().__init__()
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.velocity = pygame.Vector2(0, 0)

        for group in self.containers:
            group.add(self)

    def update(self, dt):
        self.position += self.velocity * dt

    def collides_with(self, other) -> bool:
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
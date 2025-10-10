import pygame
from circleshape import CircleShape
from constants import *


class PowerUp(CircleShape):
    containers = ()

    def __init__(self, x, y, kind="shield"):
        super().__init__(x, y, SHIELD_RADIUS, containers=PowerUp.containers)
        self.kind = kind
        self.lifetime = 20.0  # seconds before disappearing
        # small drift so it moves slowly
        import random
        angle = random.uniform(0, 360)
        speed = random.uniform(10, 30)
        self.velocity = pygame.Vector2(0, 1).rotate(angle) * speed

    def draw(self, screen):
        if self.kind == "shield":
            pygame.draw.circle(screen, (50, 150, 255), self.position, self.radius)
            pygame.draw.circle(screen, (200, 230, 255), self.position, self.radius - 4, 2)
        else:
            pygame.draw.circle(screen, "yellow", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
import pygame
from constants import *
from circleshape import *
from player import *

class Shot(CircleShape):
    containers = ()  # Will be set in main.py
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS, containers=Shot.containers)
        self.velocity = pygame.Vector2(0, 1).rotate(rotation) * PLAYER_SHOOT_SPEED
        

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt
      
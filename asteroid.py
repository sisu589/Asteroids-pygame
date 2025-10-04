import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    containers = ()  # Will be set in main.py
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, containers=Asteroid.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
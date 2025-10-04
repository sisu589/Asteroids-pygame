import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def split(self):
        import random
        # Remove this asteroid
        self.kill()
        # If this is a small asteroid, do not split further
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)
        # Create two new velocity vectors, rotated by +/- random_angle
        vel1 = self.velocity.rotate(random_angle) * 1.2
        vel2 = self.velocity.rotate(-random_angle) * 1.2
        # Compute new radius
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # Create two new asteroids at the same position
        a1 = Asteroid(self.position.x, self.position.y, new_radius)
        a2 = Asteroid(self.position.x, self.position.y, new_radius)
        a1.velocity = vel1
        a2.velocity = vel2
    containers = ()  # Will be set in main.py
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius, containers=Asteroid.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, (200, 200, 200), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
import pygame
import random

class Explosion(pygame.sprite.Sprite):
    def __init__(self, position, radius, groups):
        super().__init__(*groups)
        self.position = pygame.Vector2(position)
        self.radius = radius
        self.lifetime = 0.4  # seconds
        self.timer = 0
        self.fragments = []
        # Generate rock fragments
        for _ in range(12):
            angle = random.uniform(0, 360)
            speed = random.uniform(80, 180)
            frag_vec = pygame.Vector2(1, 0).rotate(angle) * speed
            self.fragments.append((frag_vec, angle))

    def update(self, dt):
        self.timer += dt
        if self.timer > self.lifetime:
            self.kill()

    def draw(self, screen):
        for frag_vec, angle in self.fragments:
            # Fragments move outward
            offset = frag_vec * (self.timer / self.lifetime)
            frag_pos = self.position + offset
            pygame.draw.circle(screen, (180, 180, 180), frag_pos, max(2, self.radius // 8))

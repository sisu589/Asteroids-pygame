from pickle import SHORT_BINSTRING
import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot  

class Player(CircleShape):
    def __init__(self, x: int, y: int, containers=None, shots_group=None):
        super().__init__(x, y, PLAYER_RADIUS, containers=containers)
        self.shots_group = shots_group
        self.rotation = 0
        self.shoot_timer = 0
        # Shield state
        self.shield_time_left = 0.0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        points = self.triangle()
        pygame.draw.polygon(screen, "white", points, 2)
        # draw shield if active
        if self.shield_time_left > 0:
            pygame.draw.circle(screen, (50, 150, 255), self.position, self.radius + 8, 3)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()

        # update shield timer
        if self.shield_time_left > 0:
            self.shield_time_left -= dt
            if self.shield_time_left <= 0:
                self.shield_time_left = 0

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        shot = Shot(self.position.x, self.position.y, self.rotation)
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    def apply_powerup(self, powerup):
        # currently only shield powerup supported
        if powerup.kind == "shield":
            self.shield_time_left = SHIELD_DURATION
            powerup.kill()
        
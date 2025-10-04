import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()


def main():
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create the player object outside the game loop
    player = Player(SCREEN_HEIGHT / 2, SCREEN_WIDTH /2, containers=(updatable, drawable))
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while True:        
        screen.fill((0,0,0)) # Clear the screen black

        # update all updatable objects
        updatable.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

        # Calculate delta time in seconds
        dt = clock.tick(60) / 1000 # Delta Time in seconds
        
        
        # Handle Evnets
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
                    
if __name__ == "__main__":
    main()














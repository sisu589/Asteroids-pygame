import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


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
    player = Player(SCREEN_HEIGHT / 2, SCREEN_WIDTH /2, containers=(updatable, drawable), shots_group=shots)
    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()


    while True:        
        screen.fill((0,0,0)) # Clear the screen black

        
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                pygame.quit()
                exit()
            # Check for collisions between asteroids and shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()
                    shot.kill()

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














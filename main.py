import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from explosion import Explosion

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
explosions = pygame.sprite.Group()
powerups = pygame.sprite.Group()

# Score setup
score = 0
pygame.font.init()
font = pygame.font.SysFont(None, 36)


def main():
    global score
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))

    # initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Load background image
    background = pygame.image.load("asteroids_background.jpg").convert()
    clock = pygame.time.Clock()
    dt = 0
    
    
    # Create the player object outside the game loop
    player = Player(SCREEN_HEIGHT / 2, SCREEN_WIDTH /2, containers=(updatable, drawable), shots_group=shots)
    Shot.containers = (shots, drawable, updatable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    PowerUp_containers = (powerups, drawable, updatable)
    # set PowerUp containers on the class
    try:
        from powerup import PowerUp
        PowerUp.containers = PowerUp_containers
    except Exception:
        pass
    asteroid_field = AsteroidField()


    while True:
        # Draw background image
        screen.blit(background, (0, 0))
        
        updatable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                # If player has an active shield, consume it and destroy the asteroid
                if player.shield_time_left > 0:
                    Explosion(asteroid.position, asteroid.radius, (explosions, drawable, updatable))
                    asteroid.kill()
                    continue
                print("Game over!")
                pygame.quit()
                exit()
            # Check for collisions between asteroids and shots
            for shot in shots:
                if asteroid.collides_with(shot):
                    Explosion(asteroid.position, asteroid.radius, (explosions, drawable, updatable))
                    asteroid.split()
                    shot.kill()
                    score += 10

        for sprite in drawable:
            sprite.draw(screen)
        

        # Calculate delta time in seconds
        dt = clock.tick(60) / 1000 # Delta Time in seconds
        
        # Render the score 
        # Create a surface with the score text
        score_surface = font.render(f"Score: {score}", True, (255, 255, 255))
        # Blit the score surface onto the main screen at the top-left corner
        screen.blit(score_surface, (10, 10))
        # Render shield HUD if active
        if player.shield_time_left > 0:
            # show one decimal place
            shield_text = f"Shield: {player.shield_time_left:.1f}s"
            shield_surface = font.render(shield_text, True, (150, 200, 255))
            # place it to the right of the score
            screen.blit(shield_surface, (10, 10 + score_surface.get_height() + 4))

        pygame.display.flip() # Update the full display Surface to the screen
        # Handle Evnets
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # check player pickup of powerups
        for pu in powerups:
            if pu.collides_with(player):
                player.apply_powerup(pu)
                
                    
if __name__ == "__main__":
    main()














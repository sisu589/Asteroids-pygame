import pygame
from constants import *
from circleshape import *
from player import *

def main():
    print("Starting Asteroids!")
    print("Screen width: " + str(SCREEN_WIDTH))
    print("Screen height: " + str(SCREEN_HEIGHT))
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    # Create the play object outside the game loop
    player = Player(SCREEN_HEIGHT / 2, SCREEN_WIDTH /2)
    while True:
        
        screen.fill((0,0,0)) # Clear the creen black
        player.draw(screen)
        pygame.display.flip() # update the display
        dt = clock.tick(60) / 1000 # Delta Time in seconds
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
                    
if __name__ == "__main__":
    main()














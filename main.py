# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    pygame.time.Clock
    clock = pygame.time.Clock()     # Create a Clock instance outside the loop
    dt = 0                          # Delta time initialized to 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0))      # Fills the screen with black
        pygame.display.flip()       # Updates the screen with what we've drawn
        dt = clock.tick(60) / 1000  # Calculate delta time, in seconds
        
        


if __name__ == "__main__":
    main()
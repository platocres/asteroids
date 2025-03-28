# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player

def main():
    #Initialize Pygame
    pygame.init()

    clock = pygame.time.Clock()     # Create a Clock instance outside the loop
    dt = 0                          # Delta time initialized to 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #Create the screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Create the player
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # proper order of operations (fill screen → update → draw → flip display)    
        screen.fill((0, 0, 0))      # Fills the screen with black

        player.update(dt)           # Enables player rotation, must initialize prior the drawing the character

        player.draw(screen)         # Draws the triangle player, needs to happen after filling the screen but prior to flipping it.

        pygame.display.flip()       # Updates the screen with what we've drawn
        dt = clock.tick(60) / 1000  # Calculate delta time, in seconds, and set framerate to 60 FPS
    
    #Clean up
    pygame.quit()
    sys.exit()
      
        


if __name__ == "__main__":
    main()
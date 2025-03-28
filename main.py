#If you're reading this, you're either a nerd or you're trying to confirm that I (Brandon Jones) wrote this code. Either way, welcome.

# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()                                                   # Initialize Pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Create the screen
    clock = pygame.time.Clock()                                     # Create a Clock instance outside the loop
    dt = 0                                                          # Delta time initialized to 0

    # Pygame Object Groups
    updatable = pygame.sprite.Group()                               # Updatable objects group
    drawable = pygame.sprite.Group()                                # Drawable objects group
    asteroids = pygame.sprite.Group()                               # Asteroid objects group
    shots = pygame.sprite.Group()                                   # Shooting objects group

    # Sprite Containers
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    # Welcome Message
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Creates the player
    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    running = True                                          # A loop used to enter, run, and exit the game
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))                              # Fills the screen with black
        updatable.update(dt)                                # Calls the updatable objects, enables player rotation,
                                                            # must initialize prior the drawing the character

        for asteroid in asteroids:                          # Checks for collisions between player and asteroids
            if player.collisions(asteroid):                 # Calls the collisions method in the CircleShape class
                print("Game over!")
                import sys
                sys.exit()                                  # Exit the program immediately
        
            for bullet in shots:
                if asteroid.collisions(bullet):
                    bullet.kill()
                    asteroid.split()


        for obj in drawable:                                # Calls the drawable objects, draws the triangle player, needs to happen after filling the screen but prior to flipping it.
            obj.draw(screen)

        pygame.display.flip()                               # Updates the screen with what we've drawn
        dt = clock.tick(60) / 1000                          # Calculate delta time, in seconds, and set framerate to 60 FPS
    
    #Clean up
    pygame.quit()
    
      
        


if __name__ == "__main__":
    main()
from circleshape import CircleShape
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Overrides the parent class's (CircleShape) draw method
        # Draws the asteroid
        pygame.draw.circle(screen, pygame.Color("white"), (int(self.position.x), int(self.position.y)), self.radius, 2)
    
    def update(self, dt):
        # Overrides the parent class's (CircleShape) update method
        # Moves the asteroid by velocity * dt
        self.position += self.velocity * dt
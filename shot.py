from circleshape import CircleShape
import pygame
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # Overrides the parent class's (CircleShape) draw method
        # Draws the bullet
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        # Overrides the parent class's (CircleShape) update method
        # Moves the asteroid by velocity * dt
        self.position += self.velocity * dt
    
    
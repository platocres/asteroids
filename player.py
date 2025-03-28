import pygame
import circleshape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 #The rotation field
    
    # Defining the player triangle and its position/rotation
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    # Drawing the triangle representing the player
    def draw(self, screen):
        pygame.draw.polygon(screen, 'white', self.triangle(), 2)
    
    # Rotates the player
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:    # Rotate left
            self.rotate(-dt)    
        if keys[pygame.K_d]:    # Rotate right
            self.rotate(dt)   
        if keys[pygame.K_w]:    # Move up
            self.move(dt)
        if keys[pygame.K_s]:    # Move down
            self.move(-dt)

    # Moves the player forward
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
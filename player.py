import pygame
import circleshape
from constants import *
from shot import Shot

class Player(circleshape.CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0 # The rotation field
        self.shoot_timer = 0 # Used to limit the rate of fire
    
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
        if keys[pygame.K_SPACE]:  # Shoot when spacebar is pressed
            self.shoot()
        
        if self.shoot_timer > 0:
            self.shoot_timer -= dt
    

    # Moves the player forward
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    # Defines how the player shoots
    def shoot(self):
        if self.shoot_timer > 0:                                                            # Limits rate of fire
            return  # Don't shoot if on cooldown
        shot = Shot(self.position.x, self.position.y)                                       # Create a new shot at the player's position
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED     # Create a velocity vector pointing upward
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

        
        
        
        
       
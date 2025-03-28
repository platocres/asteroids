import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    #Logic to detect collisions between the player and the asteroids
    def collisions(self, other_shape):
        # Calculate distance between centers
        # The distance_to method is a built-in method of the pygame.Vector2 class that calculates the Euclidean distance between two vectors.
        distance = self.position.distance_to(other_shape.position) 
        
        # Calculate the sum of the radii
        sum_of_radii = self.radius + other_shape.radius
        
        # If distance <= sum of radii, they're colliding
        return distance <= sum_of_radii
        
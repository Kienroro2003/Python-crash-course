import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game, increment):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.increment = increment

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the scree.
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement  flag; start with a ship that's not moving.
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """Draw the shop at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.rect.x += self.increment
        if self.moving_left:
            self.rect.x -= self.increment
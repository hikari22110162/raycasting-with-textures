import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("CAO NI MA ")

# Set up colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the egg
egg_image = pygame.image.load("ab67616d0000b273bb3213f8ffebb1e5ce25eeb5.jpg")
egg_rect = egg_image.get_rect()
egg_rect.center = (screen_width // 2, screen_height // 2)

# Set up the hidden message
hidden_message = "what are you try to say sb"

# Set up the font
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Check if the egg has been clicked
    mouse_pos = pygame.mouse.get_pos()
    if egg_rect.collidepoint(mouse_pos):
        # Display the hidden message
        text = font.render(hidden_message, True, RED)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 50))
        screen.blit(text, text_rect)

    # Draw the egg
    screen.blit(egg_image, egg_rect)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()

import pygame
import sys

# Initialize Pygame
pygame.init()

# Set screen dimensions
screen_width = 800
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title
pygame.display.set_caption("My Pygame Window")

# Set background color (RGB)
background_color = (30, 30, 60)  # Dark blue

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

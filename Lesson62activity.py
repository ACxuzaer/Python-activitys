import pygame
import sys

# Initialize pygame
pygame.init()

# Set up screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game with Background and Sound")

# Load background image
background_image = pygame.image.load("background.jpg")  # Replace with your image file path
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Load and play background music
pygame.mixer.music.load("background_music.mp3")  # Replace with your sound file path
pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.blit(background_image, (0, 0))

    # Update display
    pygame.display.update()

# Quit pygame
pygame.quit()
sys.exit()

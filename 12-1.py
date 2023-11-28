import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Sky")

# Set background color
background_color = (135, 206, 235)  # Light blue color

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with the background color
    screen.fill(background_color)

    # Update the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()

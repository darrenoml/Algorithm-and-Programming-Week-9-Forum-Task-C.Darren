import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Game Character")

# Load character image
character_image = pygame.image.load('D:\Downloads\Big Boss.bmp')  # Replace 'character.bmp' with your image path
character_rect = character_image.get_rect()
character_rect.center = (screen_width // 2, screen_height // 2)

# Set background color to match character's background (if needed)
background_color = (135, 206, 235)  # Light blue color
screen.fill(background_color)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Blit character image to the center of the screen
    screen.blit(character_image, character_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame properly
pygame.quit()
sys.exit()

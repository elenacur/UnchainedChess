import pygame

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((400, 200))
font = pygame.font.Font(None, 36)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)

# --- Normal Text Surface ---
text_surface_normal = font.render("Hello Pygame!", True, BLACK)
text_rect = text_surface_normal.get_rect(center=(200, 100))

# --- Highlighted Text Surface ---
# Renders the text with a yellow background
text_surface_highlight = font.render("Hello Pygame!", True, BLACK, YELLOW)

# Blitting logic (e.g., in your game loop)
is_highlighted = True # Change this based on game state (e.g., mouse hovering)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Simple example: toggle highlight on key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_highlighted = not is_highlighted

    screen.fill(WHITE)

    if is_highlighted:
        screen.blit(text_surface_highlight, text_rect)
    else:
        screen.blit(text_surface_normal, text_rect)

    pygame.display.flip()
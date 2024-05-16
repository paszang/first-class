import pygame
import sys
import time

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Game Countdown')

# Set up font
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def countdown(seconds):
    for i in range(seconds, 0, -1):
        window.fill(black)
        draw_text(str(i), font, white, window, width // 2, height // 2)
        pygame.display.flip()
        time.sleep(1)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
    window.fill(black)
    draw_text('Go!', font, white, window, width // 2, height // 2)
    pygame.display.flip()
    time.sleep(1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Main function
def main():
    countdown(3)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        window.fill(black)
        draw_text('The Game Has Started!', small_font, white, window, width // 2, height // 2)
        pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()

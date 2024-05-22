import pygame
import random
import sys 
from pygame.locals import *


# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("king kong Game")

# Paddle
paddle_width = 100
paddle_height = 10
paddle_x = (screen_width - paddle_width) // 2
paddle_y = screen_height - 20

# Ball
ball_radius = 10
ball_x = random.randint(ball_radius, screen_width - ball_radius)
ball_y = 50
ball_dx = 3
ball_dy = 3

# Score
score = 0

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

countdown = 3
while countdown > 0:
    for event in pygame.event.get():
         if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    text = font.render(str(countdown), True, white)
    text_rect = text.get_rect(center=(400, 300))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(1000)
    countdown -= 1
countdown_time=3
# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_x -= 5
    if keys[pygame.K_RIGHT]:
        paddle_x += 5

    # Ball movement
    ball_x += ball_dx
    ball_y += ball_dy

       # Ball collision with walls
    if ball_x <= ball_radius or ball_x >= screen_width - ball_radius:
        ball_dx = -ball_dx
    if ball_y <= ball_radius:
        ball_dy = -ball_dy

    # Ball collision with paddle
    if ball_y >= paddle_y - ball_radius and paddle_x <= ball_x <= paddle_x + paddle_width:
        ball_dy = -ball_dy
        score += 1

    # Check if ball falls off the screen
    if ball_y >= screen_height:
        game_over = True
        screen.blit("hahaha game over")

    # Fill the screen
    screen.fill(black)

    # Draw paddle
    pygame.draw.rect(screen, white, (paddle_x, paddle_y, paddle_width, paddle_height))

    # Draw ball
    pygame.draw.circle(screen, white, (ball_x, ball_y), ball_radius)

    # Display score
    score_text = font.render("Score: " + str(score), True, white)
    screen.blit(score_text, (10, 10))

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    clock.tick(100)

# Quit Pygame
pygame.quit()



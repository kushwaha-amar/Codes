import pygame
import time
import random

pygame.init()

# Set up display
width, height = 800, 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Snake properties
snake_block = 10
snake_speed = 15

# Snake initialization
snake_list = []
snake_length = 1
snake_head = [width // 2, height // 2]
snake_direction = "RIGHT"
change_to = snake_direction

# Food initialization
food_size = 10
food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]

# Score
score = 0

# Main game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and not snake_direction == "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and not snake_direction == "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and not snake_direction == "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and not snake_direction == "LEFT":
                change_to = "RIGHT"

    # Change the snake direction
    if change_to == "UP":
        snake_direction = "UP"
    elif change_to == "DOWN":
        snake_direction = "DOWN"
    elif change_to == "LEFT":
        snake_direction = "LEFT"
    elif change_to == "RIGHT":
        snake_direction = "RIGHT"

    # Move the snake
    if snake_direction == "UP":
        snake_head[1] -= snake_block
    elif snake_direction == "DOWN":
        snake_head[1] += snake_block
    elif snake_direction == "LEFT":
        snake_head[0] -= snake_block
    elif snake_direction == "RIGHT":
        snake_head[0] += snake_block

    # Check for collisions with walls
    if (
        snake_head[0] >= width or snake_head[0] < 0 or
        snake_head[1] >= height or snake_head[1] < 0
    ):
        game_over = True

    # Check for collisions with itself
    for segment in snake_list:
        if segment == snake_head:
            game_over = True

    # Check for collisions with food
    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        score += 1
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        snake_length += 1

    # Update the snake list
    snake_list.append(list(snake_head))
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Draw background
    win.fill(black)

    # Draw snake
    for segment in snake_list:
        pygame.draw.rect(win, green, [segment[0], segment[1], snake_block, snake_block])

    # Draw food
    pygame.draw.rect(win, red, [food_pos[0], food_pos[1], food_size, food_size])

    # Update display
    pygame.display.update()

    # Control the snake's speed
    clock.tick(snake_speed)

# Quit the game
pygame.quit()

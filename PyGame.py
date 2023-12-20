import pygame
import time
import random

snake_speed = 15
window_x = 720
window_y = 480

# pygame setup
pygame.init()
screen = pygame.display.set_mode((720,480))
fps = pygame.time.Clock()


snake_position = [100,50]
snake_body = [[100, 50],
              [90,50],
              [80,50],
              [70,50]]

245, 66, 66

# Generates a random position for the fruit
fruit_position = [random.randrange(1, (window_x//10)) * 10,
                   random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

direction = "RIGHT"
change_to = direction

score = 0

# Displays score function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font,size)
    score_surface = score_font.render("Score: " + str(score), True, color)
    score_rect = score_surface.get_rect()
    screen.blit(score_surface, score_rect)

def game_over():
    my_font = pygame.font.SysFont("Times new roman", 50)
    game_over_surface = my_font.render("Your score is: " + str(score), True, (245, 66, 66))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (360, 120)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()



# Establishes the four direction keys
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = "UP"
            if event.key == pygame.K_DOWN:
                change_to = "DOWN"
            if event.key == pygame.K_LEFT:
                change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                change_to = "RIGHT"

    
    # The following code is to avoid going in the opposite direction instantly, (left, right) (down,up)
    if change_to == "UP" and direction != "DOWN":
        direction = "UP"
    if change_to == "DOWN" and direction != "UP":
        direction = "DOWN"
    if change_to == "LEFT" and direction != "RIGHT":
        direction = "LEFT"
    if change_to == "RIGHT" and direction != "LEFT":
        direction = "RIGHT"

                
# Establishes co-ordinates for movement
    if direction == "UP":
        snake_position[1] -= 10
    if direction == "DOWN":
        snake_position[1] += 10
    if direction == "LEFT":
        snake_position[0] -= 10
    if direction == "RIGHT":
        snake_position[0] += 10

    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_position = fruit_position = [random.randrange(1, (window_x//10)) * 10, random.randrange(1, (window_y//10)) * 10]
 
    else:
        snake_body.pop()

 
    screen.fill((0,0,0))

    for position in snake_body:
        pygame.draw.rect(screen, (245, 66, 66), pygame.Rect(position[0], position[1], 10, 10))

    pygame.draw.rect(screen, (((0, 255, 0))), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    if snake_position[0] < 0 or snake_position[0] > window_x - 10:
        game_over()

    if snake_position[1] < 0 or snake_position[1] > window_y - 10:
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    show_score(1, (255, 255, 255), "Comic Sans", 20)    
        

    pygame.display.update()
    fps.tick(snake_speed)
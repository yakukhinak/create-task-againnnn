import pygame
import os
import sys
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#make game screen

clock = pygame.time.Clock()
#defines clock to make time control easier

pygame.display.set_caption("Falling block game")
#set project name
font = pygame.font.SysFont("cambria", 50)
smallFont = pygame.font.SysFont("cambria", 20)
#Makes variable for fonts

#colors
BLACK = (0, 0, 0)
YELLOW = (255, 255, 210)
PINK = (255, 0, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW2 = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
RED= (255, 0, 0)


squares = [] 
square_colors = [PINK, GREEN, BLUE, YELLOW2, PURPLE, ORANGE, RED]
#lists used later in the code

last_spawn_time = 0
b_rect_x = 400
b_rect_y = 530

f_rect_y = 0
falling_speed = 5
color = ""
score = 0
button_rect = None
game_over = False
#varaiables used later in the code


#PPR
def falling_squares(delay):
    global last_spawn_time, color, f_rect_x, score, button_rect
    if current_time - last_spawn_time > delay:
        f_rect_x = random.randint(1, SCREEN_WIDTH - 50) 
        squares.append([f_rect_x, 0]) 
        last_spawn_time = current_time 
        color = random.choice(square_colors)
        
       
    for square in squares[:]: 
        square[1] += falling_speed 
        pygame.draw.rect(screen, color, (square[0], square[1], 50, 50))
        score_text = font.render(f"Score: {score}", True, BLACK)
        screen.blit(score_text, (10, 10))
        if pygame.draw.rect(screen, color, (square[0], square[1], 50, 50)).colliderect(pygame.draw.rect(screen, BLACK, (b_rect_x, b_rect_y, 50, 50))):
            score += 1
            squares.remove(square)
        if square[1] > SCREEN_HEIGHT:
            text = font.render("You died", True, BLACK)
            screen.blit(text, (300, 250))
            button = font.render("Play Again", True, BLACK)
            button_rect = button.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
            pygame.draw.rect(screen, GREEN, button_rect)
            pygame.draw.rect(screen, BLACK, button_rect, 2) 
            screen.blit(button, button_rect)
            break
            

#Resets game after you click play again
def reset_game():
    global squares, score, falling_speed, b_rect_x, game_over, score_text
    squares = []
    score = 0
    falling_speed = 5
    b_rect_x = 400
    game_over = False
    game_started = True
    



game_started = False 

#game loop(what actuallly runs when the game starts)
running = True
while running:
    first= True

    screen.fill(YELLOW)
    #Fills background with yellow
    current_time = pygame.time.get_ticks() 
    #tracks the current time in the game

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
            #lets you close the window when you are done playing
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and not game_started:
                game_started = True
        
        if event.type == pygame.MOUSEBUTTONDOWN and game_over:
            if button_rect and button_rect.collidepoint(event.pos):
                reset_game()
                time.sleep(1)
        #lets you start and restart the game
        
    
    
    if not game_started:
        screen.blit(font.render("press enter to play", True, BLACK), (200, 100))
        screen.blit(font.render("Use arrow keys to move", True, BLACK), (150, 150))
        #shows the starting texts before the game starts
    if game_started:
        falling_squares(1500) 
        #Runs the main function and also the main game loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game_started = True
                score = 0
                reset_game()
                #restarts game if button clicked

    if pygame.key.get_pressed()[pygame.K_LEFT]:
         if b_rect_x > 0:
            b_rect_x -= 15
         else:
            b_rect_x = 1
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
         if b_rect_x < SCREEN_WIDTH:
            b_rect_x += 15
         else:
            b_rect_x = SCREEN_WIDTH - 60
    #user input for moving the block left and right

    pygame.draw.rect(screen, BLACK, (b_rect_x, b_rect_y, 50, 50))
    # draws the block that you control
    falling_speed += 0.005
    #changes the speed of the falling blocks as time goes on to make the game harder
    pygame.display.flip() 
    clock.tick(60) 
pygame.quit()
sys.exit()
#end the game
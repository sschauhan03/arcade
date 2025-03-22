"""
Following the tutorial at https://python.plainenglish.io/game-development-3-creating-your-first-game-with-pygame-a-simple-pong-game-02236d654f97
"""

### Imports
import pygame
# print(pygame.ver)

### Sample Loop: Pygame Structure
# pygame.init()
# screen = pygame.display.set_mode((640,480))
# running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     pygame.display.flip()

# pygame.quit()

# Initialize
pygame.init()

# Set Up Game Screen
screen = pygame.display.set_mode((800,600))

# Define Paddles
paddle_left = pygame.Rect(30,250,10,100)
paddle_right = pygame.Rect(760,250,10,100)

# Define Ball
ball = pygame.Rect(390,290,20,20)

# Scoring System
score_font = pygame.font.Font(None,36)
score_text = score_font.render('0 - 0',True,(255,255,255))
screen.blit(score_text,(375,10))

# Set Up Paddle Controls
def handle_paddle_movement(keys,paddle_left,paddle_right):
    if keys[pygame.K_w]:
        paddle_left.y -= 5 # move left paddle up
    if keys[pygame.K_s]:
        paddle_left.y += 5 # move left paddle down
    if keys[pygame.K_UP]:
        paddle_right.y -= 5 # move right paddle up
    if keys[pygame.K_DOWN]:
        paddle_right.y += 5 # move right paddle down

# Ensure Paddles Stay Within the Screen
def constrain_paddle(paddle):
    if paddle.y < 0:
        paddle.y = 0
    elif paddle.y > 500:
        paddle.y = 500

# Initial Ball Speed
ball_speed_x = 3
ball_speed_y = 3

# Initial Score
score_left = 0
score_right = 0

# Game Loop
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused # toggle pause
            elif event.key == pygame.K_n:
                running = False # end game

    keys = pygame.key.get_pressed()

    handle_paddle_movement(keys,paddle_left,paddle_right)
    constrain_paddle(paddle_left)
    constrain_paddle(paddle_right)

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= 600:
        ball_speed_y *= -1
    if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
        ball_speed_x *= -1

    if ball.left <= 0 or ball.right >= 800:
        ball.center = (400,300)
        ball_speed_x *= -1

    if ball.right >= 800:
        score_left += 1
    elif ball.left <= 0:
        score_right += 1
    
    font = pygame.font.Font(None,36)
    score_text = font.render(f'{score_left} - {score_right}',True,(255,255,255))
    screen.blit(score_text,(350,50))
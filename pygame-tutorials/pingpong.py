"""
Following the tutorial at https://python.plainenglish.io/game-development-3-creating-your-first-game-with-pygame-a-simple-pong-game-02236d654f97
"""

# ### Imports
import pygame
import random
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

# Set Up Clock
clock = pygame.time.Clock()

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
def handle_paddle_movement(keys,paddle_left,paddle_right,shift=1):
    if keys[pygame.K_w]:
        paddle_left.y -= shift # move left paddle up
    if keys[pygame.K_s]:
        paddle_left.y += shift # move left paddle down
    if keys[pygame.K_UP]:
        paddle_right.y -= shift # move right paddle up
    if keys[pygame.K_DOWN]:
        paddle_right.y += shift # move right paddle down

# Ensure Paddles Stay Within the Screen
def constrain_paddle(paddle):
    if paddle.y < 0:
        paddle.y = 0
    elif paddle.y > 500:
        paddle.y = 500

# Initial Ball Speed
ball_speed_x = 1
ball_speed_y = 1

# Initial Score
score_left = 0
score_right = 0

# Game Loop
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # check for quit
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused  # toggle pause
            elif event.key == pygame.K_n:
                running = False  # end game

    if not paused:
        # get input
        keys = pygame.key.get_pressed() 

        # make paddle move
        handle_paddle_movement(keys, paddle_left, paddle_right,shift=3)
        constrain_paddle(paddle_left)
        constrain_paddle(paddle_right)

        # set ball speed
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # check for boundaries; change ball speed direction if boundary
        if ball.top <= 0 or ball.bottom >= 600:
            ball_speed_y *= -1
        if ball.colliderect(paddle_left) or ball.colliderect(paddle_right):
            ball_speed_x *= -1

        # if cross the edge, put ball at center with random speed
        if ball.right >= 800:
            score_left += 1
            ball.center = (400, 300)
            ball_speed_x *= random.choice([-1,1])
        elif ball.left <= 0:
            score_right += 1
            ball.center = (400, 300)
            ball_speed_x *= random.choice([-1,1])

        clock.tick(250)  # limits to 60 frames per second

    # filling the screen
    screen.fill((174, 198, 207))  # Clear screen with black
    pygame.draw.rect(screen, (255, 105, 180), paddle_left)
    pygame.draw.rect(screen, (255, 105, 180), paddle_right)
    pygame.draw.ellipse(screen, (255, 165, 0), ball)
    pygame.draw.aaline(screen, (255, 105, 180), (400, 0), (400, 600))

    # Render and draw the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f'{score_left} - {score_right}', True, (255, 255, 255))
    screen.blit(score_text, (375, 50))

    pygame.display.flip()  # 🔄 Update the full display

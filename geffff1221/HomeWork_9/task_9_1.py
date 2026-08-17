import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Guess the Number")

font = pygame.font.SysFont("Arial", 30)
small_font = pygame.font.SysFont("Arial", 24)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 150, 0)
RED = (200, 0, 0)
BLUE = (0, 0, 200)

number = randint(1, 100)
attempts = 10
user_input = ""
message = "Guess a number from 1 to 100"
game_over = False

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_RETURN:
                if user_input != "":
                    guess = int(user_input)
                    attempts = attempts - 1
                    user_input = ""

                    if guess == number:
                        message = "Congratulations! You guessed it!"
                        game_over = True
                    elif guess < number:
                        message = "The number is greater. Attempts left: " + str(attempts)
                    else:
                        message = "The number is less. Attempts left: " + str(attempts)

                    if attempts == 0 and guess != number:
                        message = "You lost! The number was " + str(number)
                        game_over = True

            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]

            elif event.unicode.isdigit():
                user_input = user_input + event.unicode

    title_text = font.render("Guess the Number Game", True, BLUE)
    screen.blit(title_text, (150, 30))

    message_text = small_font.render(message, True, BLACK)
    screen.blit(message_text, (50, 120))

    input_text = font.render("Your guess: " + user_input, True, BLACK)
    screen.blit(input_text, (50, 200))

    if not game_over:
        hint_text = small_font.render("Type a number and press ENTER", True, BLACK)
        screen.blit(hint_text, (50, 280))
    else:
        end_text = small_font.render("Close the window to exit", True, RED)
        screen.blit(end_text, (50, 280))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("What Transformer are you?")

# Define colors
BLACK = (255, 255, 255)
WHITE = (0, 0, 0)
GREEN = (0, 0, 255)

# Define fonts
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    click = False
    while True:
        screen.fill(WHITE)

        draw_text('What Transformer Are You', font, BLACK, screen, 280, 100)
        mx, my = pygame.mouse.get_pos()

        button_1 = pygame.Rect(275, 200, 250, 50)
        button_2 = pygame.Rect(275, 300, 250, 50)

        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        pygame.draw.rect(screen, GREEN, button_1)
        pygame.draw.rect(screen, GREEN, button_2)

        draw_text('Start Quiz', small_font, WHITE, screen, 290, 215)
        draw_text('Quit', small_font, WHITE, screen, 370, 315)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()

def game():
    running = True
    while running:
        screen.fill(WHITE)
        draw_text('Game Screen', font, BLACK, screen, 280, 100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

main_menu()

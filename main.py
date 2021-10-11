import pygame
import os

WIDTH, HEIGHT = 900,500
WIN= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255,255,255)
BORDER = pygame.Rect(0,0,WIDTH,HEIGHT)
FPS = 60
VEL = 5
CHARACTER_WIDTH, CHARACTER_HEIGHT = 60,60
MAIN_CHARACTER_IMAGE = pygame.image.load(
    os.path.join("Assets","explorer-pixel-rpg_icon.png"))
MAIN_CHARACTER = pygame.transform.scale(MAIN_CHARACTER_IMAGE,(CHARACTER_WIDTH,CHARACTER_HEIGHT))

def draw_window(character):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN,WHITE, BORDER)
    WIN.blit(MAIN_CHARACTER,(character.x,character.y))
    pygame.display.update()

def character_movement(keys_pressed, character):
    if keys_pressed[pygame.K_a] and character.x - VEL > 0:  # Left
        character.x -= VEL
    if keys_pressed[pygame.K_d] and character.x + VEL + character.width < WIDTH:  # Right
        character.x += VEL
    if keys_pressed[pygame.K_s] and character.y + VEL + character.height < HEIGHT:  # Down
        character.y += VEL
    if keys_pressed[pygame.K_w] and character.y - VEL > 0:  # Up
        character.y -= VEL

def main():
    character = pygame.Rect(WIDTH/2, HEIGHT/2,CHARACTER_WIDTH,CHARACTER_HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        character_movement(keys_pressed,character)
        draw_window(character)

    pygame.quit()

if __name__ == '__main__':
    main()

import pygame
from Game import Fighter

pygame.init()

# create game window
SCREEN_WIDTH = 1110
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting Game")

# framerate
clock = pygame.time.Clock()
FPS = 60

# load background image
bg_image = pygame.image.load("D:/Downloads/fairy-sci-fi-alien-landscape-animation-video.jpg").convert_alpha()

bg_image = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))


# function for drawing background
# function for drawing background
def draw_bg():
    screen.blit(bg_image, (0, 0))


# create two instances of fighters
fighter_1 = Fighter(120, 350)
fighter_2 = Fighter(910, 350)

# game loop
run = True
while run:

    clock.tick(FPS)

    # draw background
    draw_bg()

    # move fighters
    fighter_1.move(SCREEN_WIDTH)
    # fighter_2.move()

    # draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

# exit
pygame.quit()

import sys
import pygame
pygame.init()

# Load the background image
background = pygame.image.load("image-cache.jpeg")

window = pygame.display.set_mode((600, 600))

    # Blit the image onto the window
window.blit(background, (0, 0))

    # Display the window

# Head
def draw_stickman():
    pygame.draw.circle(window, (0, 0, 0), (400, 200), 40, 3)

    # Body

    pygame.draw.line(window, (0, 0, 0), (400, 240), (400, 400), 3)

    # Left arm

    pygame.draw.line(window, (0, 0, 0), (400, 280), (330, 350), 3)

    # Right arm

    pygame.draw.line(window, (0, 0, 0), (400, 280), (470, 350), 3)

    # Left leg

    pygame.draw.line(window, (0, 0, 0), (400, 400), (340, 500), 3)

    # Right leg

    pygame.draw.line(window, (0, 0, 0), (400, 400), (460, 500), 3)

    pygame.display.flip()
draw_stickman()
pygame.display.flip()
while True:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
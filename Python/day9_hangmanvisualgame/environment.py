import pygame
def my_print(window, text):
    x = 310
    y = 525
    width = 270
    height = 70

    pygame.draw.rect(window, (30, 30, 40), (x, y, width, height))
    font_size = 40
    while font_size > 10:
        font = pygame.font.Font(None, font_size)
        words = text.split(" ")
        lines = []
        current_line = ""

        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= width - 10:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "

        if current_line:
            lines.append(current_line)
        line_height = font.get_height()
        if len(lines) * line_height <= height - 10:
            break
        font_size -= 1
    # Draw each line
    total_height = len(lines) * line_height
    start_y = y + (height - total_height) / 2
    for line in lines:
        rendered_text = font.render(line, True, (255, 255, 255))

        text_rect = rendered_text.get_rect(
            center=(x + width / 2, start_y + line_height / 2)
        )
        window.blit(rendered_text, text_rect)
        start_y += line_height


def draw_stand(window, screen_length, screen_width, drawing_condition=12 ):
    pygame.draw.rect(window,(139, 69, 19), (screen_length-200, screen_width-100, 200, 20) )
    pygame.draw.rect(window, (139, 69, 19), (screen_length-100, screen_width-500, 20, 400) )
    pygame.draw.rect(window, (139, 69, 19), (screen_length-300, screen_width-500, 200, 20) )

    # Head
    if drawing_condition>=1:
        pygame.draw.ellipse(window, (0, 0, 0), (screen_length - 282.5 + 5, screen_width - 410, 60, 60), 5)

    # Eyes
    if drawing_condition >= 2:
        pygame.draw.circle(window, (0, 0, 0), (screen_length - 282.5 + 18, screen_width - 410 + 22), 4)
    if drawing_condition >= 3:
        pygame.draw.circle(window, (0, 0, 0), (screen_length - 282.5 + 42, screen_width - 410 + 22), 4)

    # Mouth
    if drawing_condition >= 4:
        pygame.draw.arc(window, (0, 0, 0), (screen_length - 282.5 + 17, screen_width - 410 + 30, 26, 15), 0, 3.14, 2)

    # Rope body
    if drawing_condition >= 5:
        pygame.draw.rect(window,(170, 130, 70),(screen_length - 250, screen_width - 480, 5, 80))

    # Rope filaments
        rope_x = screen_length - 250
        rope_top = screen_width - 480
        rope_bottom = screen_width - 400

        for y in range(rope_top, rope_bottom, 8):
        # Diagonal filament
            pygame.draw.line(
            window,
            (100, 70, 35),
            (rope_x, y),
            (rope_x + 5, y + 5),
            1
        )

        # Opposite diagonal filament
            pygame.draw.line(
            window,
            (220, 180, 110),
            (rope_x + 5, y),
            (rope_x, y + 5),
            1
        )
    if drawing_condition >= 6:
        rope_x = screen_length - 282.5
        rope_y = screen_width - 400

        pygame.draw.ellipse(
            window,
        (170, 130, 70),
        (rope_x, rope_y, 70, 40),
        3
    )

    # Filaments around the loop
        for x in range(int(rope_x + 5), int(rope_x + 65), 8):
            pygame.draw.line(
            window,
            (100, 70, 35),
            (x, rope_y + 5),
            (x + 5, rope_y + 12),
            1
        )

    if drawing_condition >= 7:
    # Body - two sticks
        pygame.draw.line(window,(0, 0, 0),(screen_length - 282.5 + 5 + 25, screen_width - 410 + 60),(screen_length - 282.5 + 5 + 25, screen_width - 410 + 130),5)
    if drawing_condition >= 8:
        pygame.draw.line(window,(0, 0, 0),(screen_length - 282.5 + 5 + 35, screen_width - 410 + 60),(screen_length - 282.5 + 5 + 35, screen_width - 410 + 130),5)

    # Left arm
    if drawing_condition >= 9:
        pygame.draw.line(window,(0, 0, 0),(screen_length - 282.5 + 5 + 25, screen_width - 410 + 75),(screen_length - 282.5 + 5 - 10, screen_width - 410 + 105),5)

    # Right arm
    if drawing_condition >= 10:
        pygame.draw.line(window,(0, 0, 0),(screen_length - 282.5 + 5+ 35, screen_width - 410 + 75),(screen_length - 282.5 + 5 + 70, screen_width - 410 + 105),5)
    # Left leg
    if drawing_condition >= 11:
        pygame.draw.line(window,(0, 0, 0),(screen_length - 282.5 + 5 + 25, screen_width - 410 + 130),(screen_length - 282.5 + 5 - 5, screen_width - 410 + 175),5 )

    # Right leg
    if drawing_condition >= 12:
        pygame.draw.line(window,(0, 0, 0),(screen_length - 282.5 + 5 + 35, screen_width - 410 + 130),(screen_length - 282.5 + 5 + 65, screen_width - 410 + 175),5)

def Screen(screen_length, screen_width):
    window = pygame.display.set_mode((screen_length, screen_width))
    return window





    return window

def menu(window):
    pygame.draw.rect(window, (30, 30, 40), (0, 0, 200, 50))
    font = pygame.font.Font(None, 36)
    text = font.render("Menu", True, (0, 255, 0))
    window.blit(text, (20, 10))

def attempts(window):
    pygame.draw.rect(window, (30, 30, 40), (400, 0, 100, 50))
    font = pygame.font.Font(None, 36)
    text = font.render("Hello", True, (255, 0, 0))
    window.blit(text, (420, 10))


def score(window):
    pygame.draw.rect(window, (30, 30, 40), (510, 0, 90, 50))
    font = pygame.font.Font(None, 36)
    text = font.render("Hello", True, (75, 0, 130))
    window.blit(text, (530, 10))

def letters(window, alphabet):
        x=20
        y=100
        w=280
        l=400
        pygame.draw.rect(window, (30, 30, 40), (x, y, w, l), 0)
        font = pygame.font.Font(None, 55)

        # 5 columns, 6 rows

        columns = 7
        rows = 4
        cell_width = w / columns
        cell_height = l / rows
        for i, letter in enumerate(alphabet):
            column = i % columns
            row = i // columns
            text = font.render(letter, True, (255, 255, 255))
            # Center the letter inside its cell
            text_rect = text.get_rect(
                center=(
                    x + column * cell_width + cell_width / 2,
                    y + row * cell_height + cell_height / 2
                )
            )

            window.blit(text, text_rect)

def get_clicked_letter(mouse_position, alphabet):

    x = 20
    y = 100
    w = 280
    l = 400

    columns = 7
    rows = 4
    cell_width = w / columns
    cell_height = l / rows
    mouse_x, mouse_y = mouse_position
    # Is the mouse inside the alphabet rectangle?
    if not (x <= mouse_x <= x + w and y <= mouse_y <= y + l):
        return None
    column = int((mouse_x - x) // cell_width)
    row = int((mouse_y - y) // cell_height)
    index = row * columns + column
    if index < len(alphabet):
        return alphabet[index]
    return None

def current_stage(window):
    pygame.draw.rect(window, (30, 30, 40), (30, 525, 270, 70))
    font = pygame.font.Font(None, 36)
    current_word = "Hello"
    text = font.render(current_word, True, (255, 255, 255))
    text_rect = text.get_rect(
        center=(30 + 270 / 2, 525 + 70 / 2)
    )
    window.blit(text, text_rect)



def play():

    pygame.init()
    screen_length = 600
    screen_width = 600
    window = Screen(screen_length, screen_width)
    background = pygame.image.load(
        "pixel-art-mountain-valley-landscape-winding-path-beautiful-pixel-art-landscape-reminiscent-classic-bit-bit-video-415807139.jpg.webp")
    background = pygame.transform.scale(background,
                                        (screen_length, screen_width))  # to force image to be at scale of screen
      # to put image at that position


    clock = pygame.time.Clock() # so as not to use all cpu
    running = True

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]


    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                user_guess = get_clicked_letter(event.pos,alphabet)
                if user_guess is not None:
                    alphabet.remove(user_guess)
                    print("You clicked:", user_guess)
        window.blit(background, (0, 0))
        draw_stand(window, screen_length, screen_width)
        # menu
        menu(window)
        # attempts_left
        attempts(window)
        # score
        score(window)
        # letters
        letters(window, alphabet)
        # current_stage
        current_stage(window)

        my_print(window,"hello my name is i come from and i would like to do, i love")

        pygame.display.flip()
        clock.tick(60)
    pygame.quit()

play()
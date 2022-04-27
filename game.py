from curses import COLOR_PAIRS
import pygame


DRAW_COLORS = {
    "Black": [0, 0, 0],
    "White": [255, 255, 255],
    "Red": [255, 0, 0],
    "Lime": [0, 255, 0],
    "Blue": [0, 0, 255],
    "Yellow": [255, 255, 0],
    "Cyan": [0, 255, 255],
    "Magenta": [255, 0, 255],
    "Purple": [128, 0, 128]
}


def main():
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(
        size, pygame.RESIZABLE)

    # Set Game View and options
    set_color = DRAW_COLORS["Black"]
    line_size = 4
    mouse_position = (0, 0)
    allow_drawing = False
    last_pos = None

    # Setup Game
    draw_line = True
    play = True
    screen.fill(DRAW_COLORS["White"])

    # Main Loop
    while play:
        drawColorPicker(screen, set_color, line_size)
        drawCurrentColor(screen, set_color)

        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                if allow_drawing:
                    if last_pos is not None:
                        pygame.draw.line(screen, set_color, last_pos,
                                         mouse_position, line_size)
                    last_pos = mouse_position
            elif event.type == pygame.MOUSEBUTTONUP:
                last_pos = None
                allow_drawing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_position[0] <= 50 and mouse_position[1] > 50:
                    pick_color = pygame.Surface.get_at(screen, mouse_position)
                    set_color = pick_color
                    pygame.mouse.get_pressed()
                if draw_line:
                    allow_drawing = True
                else:
                    pygame.draw.circle(screen, set_color, mouse_position, 20)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    clear_screen(screen)
                elif event.key == pygame.K_UP:
                    line_size = line_size+1
                elif event.key == pygame.K_DOWN:
                    if line_size > 1:
                        line_size = line_size-1
                elif event.key == pygame.K_m:
                    draw_line = not draw_line
                elif event.key == pygame.K_ESCAPE:
                    play = False
                    pygame.quit()
                    break
                elif event.key == pygame.K_SPACE:
                    pygame.display.toggle_fullscreen()  # Toggle fullscreen
                elif event.key == pygame.K_a:
                    animate_circle(screen, set_color,
                                   mouse_position[0], mouse_position[1], 0)
        pygame.display.update()
    pygame.quit()


def clear_screen(screen):
    radius = 0.1
    x, y = pygame.display.get_window_size()
    while radius <= x/2:
        pygame.draw.circle(screen, DRAW_COLORS["White"], (x/2, y/2), radius)
        radius += 5
        pygame.display.update()
    screen.fill(DRAW_COLORS["White"])


def animate_circle(screen, color, x, y, radius):
    pygame.draw.circle(screen, color, (x, y), radius)
    pygame.display.update()
    pygame.time.delay(10)
    radius += 1
    if radius <= x/2:
        animate_circle(screen, color, x, y, radius)


def drawColorPicker(screen, set_color, line_size):
    cX = 0
    cY = 0
    for col in DRAW_COLORS:
        cY += 50
        pygame.draw.rect(screen, col, [cX, cY, 50, 50])
    pygame.draw.rect(screen, DRAW_COLORS["White"], [cX, cY+50, 50, 50])
    pygame.draw.circle(screen, set_color, (cX+25, cY+75), line_size)


def drawCurrentColor(screen, set_color):
    pygame.draw.rect(screen, set_color, [0, 0, 50, 50])


if __name__ == "__main__":
    main()

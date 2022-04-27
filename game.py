import pygame


colors = {
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
        (0, 0), pygame.FULLSCREEN, pygame.RESIZABLE)

    # Set Game View and options
    set_color = colors["Black"]
    line_size = 4
    mouse_position = (0, 0)
    drawing = False
    last_pos = None

    # Setup Game
    draw_line = True
    play = True
    clock = pygame.time.Clock()
    screen.fill(colors["White"])
    while play:

        cX = 0
        cY = 0
        pygame.draw.rect(screen, set_color, [0, 0, 50, 50])

        for col in colors:
            cY += 50
            pygame.draw.rect(screen, col, [cX, cY, 50, 50])
        pygame.draw.rect(screen, colors["White"], [cX, cY+50, 50, 50])
        pygame.draw.circle(screen, set_color, (cX+25, cY+75), line_size)

        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
                pygame.quit()
            elif event.type == pygame.MOUSEMOTION:
                if (drawing):
                    if last_pos is not None:
                        pygame.draw.line(screen, set_color, last_pos,
                                         mouse_position, line_size)
                    last_pos = mouse_position
            elif event.type == pygame.MOUSEBUTTONUP:
                last_pos = None
                drawing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouse_position[0] <= 50 and mouse_position[1] > 50:
                    pick_color = pygame.Surface.get_at(screen, mouse_position)
                    set_color = pick_color
                    pygame.mouse.get_pressed()
                if draw_line:
                    drawing = True
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
        pygame.display.update()
    pygame.quit()


def clear_screen(screen):
    radius = 0.1
    x, y = pygame.display.get_window_size()
    while radius <= x/2:
        pygame.draw.circle(screen, colors["White"], (x/2, y/2), radius)
        radius += 5
        pygame.display.update()
    screen.fill(colors["White"])


if __name__ == "__main__":
    main()

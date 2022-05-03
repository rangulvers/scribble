
import pygame
from particle import Particle
from particle import particles


class Controller:
    def __init__(self):
        self.mous_pos = (0, 0)

    def keybboard(self, key):
        if key == pygame.K_c:
            self.clear_screen(settings.screen)
        elif key == pygame.K_UP:
            line_size = line_size+1
        elif key == pygame.K_DOWN:
            if line_size > 1:
                line_size = line_size-1
        elif key == pygame.K_m:
            settings.draw_line = not settings.draw_line
        elif key == pygame.K_SPACE:
            pygame.display.toggle_fullscreen()  # Toggle fullscreen
        elif key == pygame.K_a:
            self.animate_circle(settings.screen, settings.set_color,
                                self.mous_pos[0], self.mous_pos[1], 0)
        elif key == pygame.K_p:           # play particle effect
            self.create_particles(self.mous_pos)

    def mouse(self):
        pass

    def clear_screen(self, screen):
        radius = 0.1
        x, y = pygame.display.get_window_size()
        while radius <= x/2:
            pygame.draw.circle(
                screen, settings.DRAW_COLORS["White"], (x/2, y/2), radius)
            radius += 5
            pygame.display.update()
        screen.fill(settings.DRAW_COLORS["White"])

    def white_canvas(self, screen):
        screen.fill(settings.DRAW_COLORS["White"])

    def animate_circle(self, screen, color, x, y, radius):
        pygame.draw.circle(screen, color, (x, y), radius)
        pygame.display.update()
        pygame.time.delay(10)
        radius += 1
        if radius <= x/2:
            self.animate_circle(screen, color, x, y, radius)

    def drawColorPicker(self, screen, set_color, line_size):
        cX = 0
        cY = 0
        for col in settings.DRAW_COLORS:
            cY += 50
            pygame.draw.rect(screen, col, [cX, cY, 50, 50])
        pygame.draw.rect(screen, settings.DRAW_COLORS["White"], [
                         cX, cY+50, 50, 50])
        pygame.draw.circle(screen, set_color, (cX+25, cY+75), line_size)

    def drawCurrentColor(self, screen, set_color):
        pygame.draw.rect(screen, set_color, [0, 0, 50, 50])

    def create_particles(self, pos):
        for part in range(2):
            particles.add(
                Particle(pos[0], pos[1], settings.DRAW_COLORS, False, [1, 3], speed=5))


class Settings:
    def __init__(self):
        self.size = width, height = 800, 600
        self.screen = pygame.display.set_mode(
            self.size, pygame.RESIZABLE)
        self.DRAW_COLORS = {
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
        self.set_color = self.DRAW_COLORS["Black"]
        self.line_size = 4
        self.mouse_position = (0, 0)
        self.allow_drawing = False
        self.last_pos = None
        self.draw_line = True
        self.play_game = True
        self.particle_life_time = 2500


settings = Settings()
controller = Controller()

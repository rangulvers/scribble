import pygame
import random


class Particle():
    def __init__(self, startx, starty, col):
        self.x = startx
        self.y = starty
        self.col = col
        self.colors = col
        self.livetime = pygame.time.get_ticks()

    def __del__(self):
        pass

    def move(self):
        if self.y > pygame.display.get_window_size()[1]:
            self.livetime = 0

        else:
            self.y += random.randint(1, 10)

        self.x += random.randint(-10, 10)

    def draw(self):
        color = self.colors[random.choice(list(self.colors))]
        pygame.draw.circle(
            pygame.display.get_surface(), color, (self.x, self.y), random.randint(1, 4))

    def live(self):
        return pygame.time.get_ticks()-self.livetime

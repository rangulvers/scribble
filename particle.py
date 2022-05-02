import re
import pygame
import random


class Particle:
    def __init__(self, startx, starty, col, falling=True, size=[1, 4]):
        self.x = startx
        self.y = starty
        self.falling = falling
        self.size = size
        self.colors = col
        self.livetime = pygame.time.get_ticks()

    def __del__(self):
        pass

    def move(self):
        if self.falling:
            if self.y > pygame.display.get_window_size()[1]:
                self.livetime = 0
            else:
                self.y += random.randint(1, 10)
        else:
            if self.y <= 0:
                self.livetime = 0
            else:
                self.y -= random.randint(1, 10)
        self.x += random.randint(-10, 10)

    def draw(self):
        pygame.draw.circle(
            pygame.display.get_surface(), self.get_color(), (self.x, self.y), self.get_particle_size())

    def life(self):
        return pygame.time.get_ticks()-self.livetime

    def get_color(self):
        return self.colors[random.choice(list(self.colors))]

    def get_particle_size(self):
        return random.randint(self.size[0], self.size[1])

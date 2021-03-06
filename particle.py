
import pygame
import random


class Particle:
    def __init__(self, startx, starty, col, falling=True, size=[1, 4], spread=[-5, 5], speed=20, lifespan=2500):
        self.x = startx
        self.y = starty
        self.falling = falling
        self.size = size
        self.spread = spread
        self.speed = speed
        self.colors = col
        self.birth_time = pygame.time.get_ticks()
        self.lifespan = lifespan
        self.is_alive = True

    def __del__(self):
        pass

    def move(self):
        if self.falling:
            if self.y > pygame.display.get_window_size()[1]:
                self.is_alive = False
            else:
                self.y += self.get_speed()
        else:
            if self.y <= 0:
                self.is_alive = False
            else:
                self.y -= self.get_speed()
        self.x += self.get_spread()
        self.check_live_time()

    def draw(self):
        pygame.draw.circle(
            pygame.display.get_surface(), self.get_color(), (self.x, self.y), self.get_particle_size())
        self.move()

    def life(self):
        return pygame.time.get_ticks()-self.birth_time

    def get_color(self):
        return self.colors[random.choice(list(self.colors))]

    def get_particle_size(self):
        return random.randint(self.size[0], self.size[1])

    def get_spread(self):
        return random.randint(self.spread[0], self.spread[1])

    def get_speed(self):
        return random.randint(1, self.speed)

    def check_live_time(self):
        if (pygame.time.get_ticks() - self.birth_time) > self.lifespan or self.is_alive == False:
            particles.rem(self)
            del self


class ParticleArray:
    def __init__(self):
        self.particles = []

    def add(self, obj):
        self.particles.append(obj)

    def rem(self, obj):
        self.particles.pop(self.particles.index(obj))


particles = ParticleArray()

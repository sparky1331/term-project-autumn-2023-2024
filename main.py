import pygame
import math


FPS = 60

WIDTH = 800
HEIGHT = 600

TURQOISE = 0x40E0D0

k = 0.2


class Car:
    def __init__(self, screen: pygame.Surface, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.points = 0
        self.mass = 2
        self.angle = 1
        self.thrust = 0
        self.ax = 0
        self.ay = 0

    def move(self):
        """Перемещение машинки"""
        self.dragx = k * self.vx
        self.dragy = k * self.vy
        self.ax = (self.thrust * math.cos(self.angle) - self.dragx) / self.mass
        self.ay = (self.thrust * math.sin(self.angle) - self.dragy) / self.mass
        self.vx += self.ax
        self.vy += self.ay
        self.x += self.vx
        self.y += self.vy


pygame.init()

DISPLAYSURFACE = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

mainLoop = True

while mainLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainLoop = False
    pygame.display.update()

pygame.quit()

import pygame, math

pygame.init()

size = width, height = (600, 600)
canvas = pygame.display.set_mode(size)

gravity = 9.8

class Pendulum:
    def __init__(self, length, initial_theta, initial_speed):
        self.length = length
        self.initial_theta = initial_theta
        self.initial_speed = initial_speed

def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
    pygame.display.update()

if __name__ == "__main__":
    main()
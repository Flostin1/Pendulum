import math
import pygame

pygame.init()

size = width, height = (600, 600)
canvas = pygame.display.set_mode(size)
clock = pygame.time.Clock()

FPS = 60
gravity = 9.8

class Pendulum:
    def __init__(self, length, initial_theta, initial_speed, color=pygame.Color('blue')):
        self.length = length
        self.theta = initial_theta
        self.speed = initial_speed
        self.damping = 0.00

        self.radius = 10
        self.color = color
        self.list = []
        self.ticks = 0
        self.initial_frame = True
    
    def render(self):
        bob_position = (self.length * math.cos(self.theta + math.pi/2) + width/2, self.length * math.sin(self.theta + math.pi/2) + height/4)
        pygame.draw.aaline(canvas, (0, 0, 150), (width/2, height/4), bob_position)
        pygame.draw.circle(canvas, self.color, (width/2, height/4), 3)

        pygame.draw.circle(canvas, self.color, bob_position, self.radius)
    
    def update(self):
        self.theta += self.speed / FPS
        self.speed -= gravity / self.length * math.sin(self.theta)
        self.speed *= (1 - self.damping / FPS)

    # Renders a graph of theta vs time for the swinging pendulum
    def graph_motion(self):
        if (len(self.list) > width):
            self.list.clear()
            self.ticks = 0
            self.initial_frame = True

        self.list.append((self.ticks, 150/math.pi * self.theta + 3/4*height))

        if (self.initial_frame):
            self.initial_frame = False
        else:
            pygame.draw.aalines(canvas, self.color, False, self.list)

        self.ticks += 1

    def run(self):
        self.update()
        self.render()
        self.graph_motion()

def main():
    pendulum = Pendulum(50, math.pi*1/2, 0, (0, 200, 0))
    pendulum2 = Pendulum(100, math.pi*1/2, 0)
    pendulum3 = Pendulum(200, math.pi*1/2, 0, (0, 200, 200))

    background = pygame.Surface(size)
    background.fill((255, 255, 255))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        canvas.blit(background, (0, 0))
        pendulum.run()
        pendulum2.run()
        pendulum3.run()
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()
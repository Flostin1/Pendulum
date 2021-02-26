import pygame, math

pygame.init()

size = width, height = (600, 600)
canvas = pygame.display.set_mode(size)
clock = pygame.time.Clock()

FPS = 60
gravity = 9.8

class Pendulum:
    def __init__(self, length, initial_theta, initial_speed):
        self.length = length
        self.theta = initial_theta
        self.speed = initial_speed

        self.radius = 15
        self.color = pygame.Color('blue')
        self.list = []
        self.ticks = 0
        self.initial_frame = True
    
    def render(self):
        pygame.draw.circle(canvas, self.color, (width/2, height/4), 3)

        pygame.draw.circle(
            canvas, 
            self.color, 
            (self.length * math.cos(self.theta + math.pi/2) + width/2, self.length * math.sin(self.theta + math.pi/2) + height/4), 
            self.radius
            )
    
    def update(self):
        self.theta += self.speed / FPS
        self.speed -= gravity / self.length * math.sin(self.theta)

    # Renders a graph of theta vs time for the swinging pendulum
    def graph_motion(self):
        self.list.append((self.ticks, 150/math.pi * self.theta + height*(3/4)))

        if (self.initial_frame):
            self.initial_frame = False
        else:
            pygame.draw.lines(canvas, (0, 200, 0), False, self.list)

        self.ticks += 1

    def run(self):
        self.update()
        self.render()
        self.graph_motion()

def main():
    pendulum = Pendulum(100, 7/8*math.pi, 0)

    background = pygame.Surface(size)
    background.fill((255, 255, 255))
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        canvas.blit(background, (0, 0))
        pendulum.run()
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
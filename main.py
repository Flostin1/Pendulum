import pygame, math

pygame.init()

size = width, height = (600, 600)
canvas = pygame.display.set_mode(size)

FPS = 60
gravity = 9.8

class Pendulum:
    def __init__(self, length, initial_theta, initial_speed):
        self.length = length
        self.theta = initial_theta
        self.speed = initial_speed
        self.radius = 20
    
    def render(self):
        pygame.draw.circle(
            canvas, 
            (0, 0, 255), 
            (self.length * math.cos(self.theta + math.pi/2) + width / 2, self.length * math.sin(self.theta + math.pi/2) + height / 2), 
            self.radius
            )
    
    def update(self):
        self.theta += self.speed / FPS
        self.speed -= gravity / self.length * math.sin(self.theta)
        print(self.theta)

    def run(self):
        self.update()
        self.render()

def main():
    pendulum = Pendulum(100, 2*math.pi/3, -5*math.pi/8)

    background = pygame.Surface(size)
    background.fill((255, 255, 255))
    clock = pygame.time.Clock()
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
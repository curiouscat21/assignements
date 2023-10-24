import pygame
import random


class BouncingBall:

    def __init__(self, screen, color, size):
        self.screen = screen
        self.color = color
        self.size = random.randint(20, 100)
        self.position = pygame.Vector2(random.randint(0, 1281), random.randint(0, 721))
        self._speedx = random.randint(1, 50)
        self._speedy = random.randint(1, 50)
        self.active = True
        self.dt = 0

    def move(self, dt):
        if not self.active:
            return
        self.position.y += self._speedy
        self.position.x += self._speedx
        if self.position.y >= 720 or self.position.y <= 0:
            self._speedy = -self._speedy
        if self.position.x >= 1280 or self.position.x <= 0:
            self._speedx = -self._speedx

    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.position, self.size)

    def fps(self):
        pygame.time.delay(random.randint(-10, 1))


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

balls = []
for _ in range(5):
    color = random.choice(["red", "green", "sky blue", "pink", "yellow", "black", "cyan", "brown", "magenta",])
    size = random.randint(30, 151)
    balls.append(BouncingBall(screen, color, size))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    for ball in balls:
        ball.move(ball.dt)
        ball.draw()
        ball.fps()

    pygame.display.flip()

    for player in balls:
        player.dt = clock.tick(150) / 1000

pygame.quit()

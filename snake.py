import pygame, random, sys

pygame.init()

SIZE = 20
WIDTH = 400
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
Clock = pygame.time.Clock()

BLACK, GREEN, RED = (0, 0, 0), (0, 200, 0), (200, 0, 0)

snake = [(100, 100)]
dx, dy = SIZE, 0
food = (200, 200)

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP and dy == 0:
                dx, dy = 0, -SIZE
            if e.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, SIZE
            if e.key == pygame.K_LEFT and dx == 0:
                dx, dy = -SIZE, 0
            if e.key == pygame.K_RIGHT and dx == 0:
                dx, dy = SIZE, 0

    head = (snake[0][0] + dx, snake[0][1] + dy)
    snake.insert(0, head)

    if head == food:
        while True:
            new_food = (random.randrange(0, WIDTH, SIZE), random.randrange(0, HEIGHT, SIZE))
            if new_food not in snake:
                food = new_food
                break
    else:
        snake.pop()

    if (head in snake[1:] or not 0 <= head[0] < WIDTH or not 0 <= head[1] < HEIGHT):
        print("Game over! Score:", len(snake) - 1)
        pygame.time.delay(1500)
        running = False

    screen.fill(BLACK)
    for x, y in snake:
        pygame.draw.rect(screen, GREEN, (x, y, SIZE, SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], SIZE, SIZE))
    pygame.display.flip()
    Clock.tick(10)

pygame.quit()
sys.exit()

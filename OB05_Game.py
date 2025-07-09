import pygame
import random
import time



# Подключение Pygame
pygame.init()

# Определение цветов, для дальнейшего использования
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Размеры экрана и блоков
BLOCK_SIZE = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Настраиваем экран
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(' Змейка ')

# Частота обновления экрана
clock = pygame.time.Clock()
FPS = 10

class Snake:
    def __init__(self):
# Начальная позиция и длина Snake
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.length = 1
        self.direction = random.choice([pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def move(self):
        head = self.get_head_position()
        x, y = head

# Управление движением
        if self.direction == pygame.K_UP:
            y -= BLOCK_SIZE
        elif self.direction == pygame.K_DOWN:
            y += BLOCK_SIZE
        elif self.direction == pygame.K_LEFT:
            x -= BLOCK_SIZE
        elif self.direction == pygame.K_RIGHT:
            x += BLOCK_SIZE

# Обновляем позицию головы
        self.positions.insert(0, (x, y))
        if len(self.positions) > self.length:
            self.positions.pop()

    def draw(self, surface):
# Рисуем Snake
        for position in self.positions:
            rect = pygame.Rect(position[0], position[1], BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(surface, self.color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
# Случайная позиция для еды
        self.position = (
            random.randint(0, (SCREEN_WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE,
            random.randint(0, (SCREEN_HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        )

    def draw(self, surface):
# Рисуем еду
        rect = pygame.Rect(self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, BLACK, rect, 1)


def main():

    snake = Snake()
    food = Food()
    score = 0

    running = True
    while running:
# Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
# Управление змейкой
                if event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT]:
                    snake.direction = event.key

# Движение змейки
        snake.move()

# Проверка столкновения с едой
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()

# Проверка столкновения с границами
        head = snake.get_head_position()
        if (head[0] < 0 or head[0] >= SCREEN_WIDTH or
                head[1] < 0 or head[1] >= SCREEN_HEIGHT):
            running = False

# Проверка столкновения с собой
        if head in snake.positions[1:]:
            running = False

# Отрисовка
        screen.fill(WHITE)
        snake.draw(screen)
        food.draw(screen)

# Отображение счета
        font = pygame.font.SysFont('Arial', 20)
        score_text = font.render(f'Счет: {score}', True, BLACK)
        screen.blit(score_text, (5, 5))

        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()



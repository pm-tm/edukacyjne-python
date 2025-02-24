import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
CELL_SIZE = 20
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BG_COLOR = (0, 0, 0)
FPS = 10  # Initial FPS

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class Snake:
    def __init__(self):
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False
        self.changed_direction = False

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x * CELL_SIZE) % SCREEN_WIDTH, (head_y + dir_y * CELL_SIZE) % SCREEN_HEIGHT)

        if new_head in self.positions[1:]:
            raise Exception("Game Over")

        self.positions.insert(0, new_head)
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False
        self.changed_direction = False

    def change_direction(self, direction):
        if not self.changed_direction and (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction
            self.changed_direction = True

    def grow_snake(self):
        self.grow = True

    def draw(self, screen):
        for pos in self.positions:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

class Food:
    def __init__(self):
        self.position = (random.randint(0, (SCREEN_WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                         random.randint(0, (SCREEN_HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

def draw_score(screen, score):
    font = pygame.font.SysFont(None, 35)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    snake = Snake()
    food = Food()
    score = 0
    fps = FPS  # Use a local variable for FPS

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    snake.change_direction(UP)
                elif event.key == pygame.K_s:
                    snake.change_direction(DOWN)
                elif event.key == pygame.K_a:
                    snake.change_direction(LEFT)
                elif event.key == pygame.K_d:
                    snake.change_direction(RIGHT)

        try:
            snake.move()
        except Exception as e:
            print(f"Game Over! Your score: {score}")
            pygame.quit()
            sys.exit()

        if snake.positions[0] == food.position:
            snake.grow_snake()
            food = Food()
            score += 1
            fps += 1  # Increase speed

        screen.fill(BG_COLOR)
        snake.draw(screen)
        food.draw(screen)
        draw_score(screen, score)
        pygame.display.flip()
        clock.tick(fps)

if __name__ == "__main__":
    main()

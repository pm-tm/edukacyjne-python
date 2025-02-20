import pygame
import sys
import random

# Constants
SCREEN_SIZE = 300
GRID_SIZE = 3
CELL_SIZE = SCREEN_SIZE // GRID_SIZE
LINE_WIDTH = 15
CIRCLE_RADIUS = CELL_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = CELL_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (84, 84, 84)

class TicTacToe:
    def __init__(self):
        self.board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.current_player = "X"
        self.game_over = False

    def draw_lines(self, screen):
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (SCREEN_SIZE, i * CELL_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE), LINE_WIDTH)

    def draw_figures(self, screen):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == "O":
                    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * CELL_SIZE + CELL_SIZE // 2), int(row * CELL_SIZE + CELL_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == "X":
                    pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE), (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE), (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + CELL_SIZE - SPACE), CROSS_WIDTH)

    def mark_square(self, row, col, player):
        self.board[row][col] = player

    def available_square(self, row, col):
        return self.board[row][col] is None

    def is_board_full(self):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] is None:
                    return False
        return True

    def check_win(self, player):
        for row in range(GRID_SIZE):
            if all([self.board[row][col] == player for col in range(GRID_SIZE)]):
                return True
        for col in range(GRID_SIZE):
            if all([self.board[row][col] == player for row in range(GRID_SIZE)]):
                return True
        if all([self.board[i][i] == player for i in range(GRID_SIZE)]):
            return True
        if all([self.board[i][GRID_SIZE - 1 - i] == player for i in range(GRID_SIZE)]):
            return True
        return False

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def ai_move(self):
        available_moves = [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE) if self.available_square(row, col)]
        move = random.choice(available_moves)
        self.mark_square(move[0], move[1], "O")

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(BG_COLOR)
    game = TicTacToe()
    game.draw_lines(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                clicked_row = mouseY // CELL_SIZE
                clicked_col = mouseX // CELL_SIZE

                if game.available_square(clicked_row, clicked_col):
                    game.mark_square(clicked_row, clicked_col, game.current_player)
                    game.draw_figures(screen)
                    if game.check_win(game.current_player):
                        game.game_over = True
                    game.switch_player()

                    if not game.game_over and game.current_player == "O":
                        game.ai_move()
                        game.draw_figures(screen)
                        if game.check_win("O"):
                            game.game_over = True
                        game.switch_player()

        pygame.display.update()

if __name__ == "__main__":
    main()
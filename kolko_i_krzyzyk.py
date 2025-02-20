import pygame
import sys
import random

# Constants for the game
SCREEN_SIZE = 300  # Size of the game window
GRID_SIZE = 3  # Number of rows and columns in the grid
CELL_SIZE = SCREEN_SIZE // GRID_SIZE  # Size of each cell in the grid
LINE_WIDTH = 15  # Width of the grid lines
CIRCLE_RADIUS = CELL_SIZE // 3  # Radius of the circle (O)
CIRCLE_WIDTH = 15  # Width of the circle (O)
CROSS_WIDTH = 25  # Width of the cross (X)
SPACE = CELL_SIZE // 4  # Space from the edge for drawing X
WIN_LINE_WIDTH = 10  # Width of the winning line

# Colors used in the game
BG_COLOR = (28, 170, 156)  # Background color
LINE_COLOR = (23, 145, 135)  # Grid line color
CIRCLE_COLOR = (239, 231, 200)  # Circle (O) color
CROSS_COLOR = (84, 84, 84)  # Cross (X) color
WIN_LINE_COLOR = (255, 0, 0)  # Winning line color

class TicTacToe:
    def __init__(self):
        # Initialize the game board, current player, game over status, and winning line
        self.board = [[None] * GRID_SIZE for _ in range(GRID_SIZE)]
        self.current_player = "X"
        self.game_over = False
        self.win_line = None

    def draw_lines(self, screen):
        # Draw the grid lines on the screen
        for i in range(1, GRID_SIZE):
            pygame.draw.line(screen, LINE_COLOR, (0, i * CELL_SIZE), (SCREEN_SIZE, i * CELL_SIZE), LINE_WIDTH)
            pygame.draw.line(screen, LINE_COLOR, (i * CELL_SIZE, 0), (i * CELL_SIZE, SCREEN_SIZE), LINE_WIDTH)

    def draw_figures(self, screen):
        # Draw the X and O figures on the board
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] == "O":
                    pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * CELL_SIZE + CELL_SIZE // 2), int(row * CELL_SIZE + CELL_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
                elif self.board[row][col] == "X":
                    pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + SPACE, row * CELL_SIZE + CELL_SIZE - SPACE), (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + SPACE), CROSS_WIDTH)
                    pygame.draw.line(screen, CROSS_COLOR, (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE), (col * CELL_SIZE + CELL_SIZE - SPACE, row * CELL_SIZE + CELL_SIZE - SPACE), CROSS_WIDTH)

    def draw_win_line(self, screen):
        # Draw the winning line if there is a winner
        if self.win_line:
            pygame.draw.line(screen, WIN_LINE_COLOR, self.win_line[0], self.win_line[1], WIN_LINE_WIDTH)

    def mark_square(self, row, col, player):
        # Mark the selected square with the current player's symbol
        self.board[row][col] = player

    def available_square(self, row, col):
        # Check if the selected square is available
        return self.board[row][col] is None

    def is_board_full(self):
        # Check if the board is full
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                if self.board[row][col] is None:
                    return False
        return True

    def check_win(self, player):
        # Check if the current player has won the game
        for row in range(GRID_SIZE):
            if all([self.board[row][col] == player for col in range(GRID_SIZE)]):
                self.win_line = ((0, row * CELL_SIZE + CELL_SIZE // 2), (SCREEN_SIZE, row * CELL_SIZE + CELL_SIZE // 2))
                return True
        for col in range(GRID_SIZE):
            if all([self.board[row][col] == player for row in range(GRID_SIZE)]):
                self.win_line = ((col * CELL_SIZE + CELL_SIZE // 2, 0), (col * CELL_SIZE + CELL_SIZE // 2, SCREEN_SIZE))
                return True
        if all([self.board[i][i] == player for i in range(GRID_SIZE)]):
            self.win_line = ((0, 0), (SCREEN_SIZE, SCREEN_SIZE))
            return True
        if all([self.board[i][GRID_SIZE - 1 - i] == player for i in range(GRID_SIZE)]):
            self.win_line = ((0, SCREEN_SIZE), (SCREEN_SIZE, 0))
            return True
        return False

    def switch_player(self):
        # Switch the current player
        self.current_player = "O" if self.current_player == "X" else "X"

    def ai_move(self):
        # Make a move for the AI (randomly select an available square)
        available_moves = [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE) if self.available_square(row, col)]
        move = random.choice(available_moves)
        self.mark_square(move[0], move[1], "O")

def main():
    # Initialize the game and create the game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
    pygame.display.set_caption("Tic Tac Toe")
    screen.fill(BG_COLOR)
    game = TicTacToe()
    game.draw_lines(screen)

    while True:
        # Main game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game.game_over:
                mouseX = event.pos[0]  # X coordinate of the mouse click
                mouseY = event.pos[1]  # Y coordinate of the mouse click
                clicked_row = mouseY // CELL_SIZE  # Determine the row clicked
                clicked_col = mouseX // CELL_SIZE  # Determine the column clicked

                if game.available_square(clicked_row, clicked_col):
                    game.mark_square(clicked_row, clicked_col, game.current_player)
                    game.draw_figures(screen)
                    if game.check_win(game.current_player):
                        game.game_over = True
                        game.draw_win_line(screen)
                    game.switch_player()

                    if not game.game_over and game.current_player == "O":
                        game.ai_move()
                        game.draw_figures(screen)
                        if game.check_win("O"):
                            game.game_over = True
                            game.draw_win_line(screen)
                        game.switch_player()

        pygame.display.update()

if __name__ == "__main__":
    main()
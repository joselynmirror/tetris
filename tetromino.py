import random

from constants.tetrominoes import TETROMINOES


class Tetromino:
    def __init__(self, dimensions, board):
        self.dimensions = dimensions
        self.board = board

    def rotate(self):
        previous_dimensions = self.dimensions
        self.dimensions = list(zip(*self.dimensions[::-1]))

        if self.board.detect_collision():
            self.dimensions = previous_dimensions

    def move(self, x, y):
        self.board.block_offset[0] += x
        if self.board.detect_collision():
            self.board.block_offset[0] -= x
            return True

        self.board.block_offset[1] += y
        if self.board.detect_collision():
            self.board.block_offset[1] -= y
            if len(self.board.current_tetromino.dimensions) > 1 and self.board.block_offset[1] <= len(self.board.current_tetromino.dimensions[1]):
                self.board.game_is_running = False
            self.board.fix_block()
            self.board.clear_rows()

            self.board.current_tetromino = self.board.next_tetromino
            self.board.next_tetromino = Tetromino(random.choice(TETROMINOES), self.board)
            self.board.block_offset = [int(self.board.columns / 2) - 1, 0]

import random

from constants.tetrominoes import TETROMINOES
from tetromino import Tetromino


class Board:
    def __init__(self, player_name):
        self.game_is_running = True
        self.score = 0
        self.rows = 20
        self.columns = 10
        self.cell_size = 32
        self.size = (self.columns * self.cell_size, self.rows * self.cell_size)
        self.grid = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.next_tetromino = Tetromino(random.choice(TETROMINOES), self)
        self.current_tetromino = Tetromino(random.choice(TETROMINOES), self)
        self.block_offset = [int(self.columns / 2) - 1, 0]
        self.player_name = player_name

    def clear_rows(self):
        for i, row in enumerate(self.grid):
            if all(row):
                self.grid.pop(i)
                self.grid.insert(0, [0 for _ in range(self.columns)])
                self.score += self.columns

    def detect_collision(self):
        if self.block_offset[0] < 0:
            return True
        if self.block_offset[0] >= self.columns - len(self.current_tetromino.dimensions[0]) + 1:
            return True

        if self.block_offset[1] > self.rows - len(self.current_tetromino.dimensions):
            return True

        for i, block_row in enumerate(self.current_tetromino.dimensions):
            for j, block_element in enumerate(block_row):
                if block_element != 0:
                    if (
                        self.grid[i + self.block_offset[1]][j + self.block_offset[0]]
                        != 0
                    ):
                        return True

    def fix_block(self):
        for i, block_row in enumerate(self.current_tetromino.dimensions):
            for j, block_element in enumerate(block_row):
                if block_element != 0:
                    self.grid[i + self.block_offset[1]][j + self.block_offset[0]] = (
                        block_element
                    )

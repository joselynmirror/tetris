import pygame

from constants.colors import COLORS, TEXT_COLOR
from constants.config import SCREEN_RESOLUTION
from constants.copy import SCORE, NEXT_TETROMINO


class Printer:
    def __init__(self, board, screen, font):
        self.board = board
        self.screen = screen
        self.font = font

    def __print_field(self):
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                rect = (
                    column * self.board.cell_size + SCREEN_RESOLUTION[0] / 2 - self.board.size[0] / 2,
                    row * self.board.cell_size + SCREEN_RESOLUTION[1] / 2 - self.board.size[1] / 2,
                    self.board.cell_size,
                    self.board.cell_size,
                )
                pygame.draw.rect(
                    self.screen,
                    COLORS[self.board.grid[row][column]],
                    rect,
                    1 if self.board.grid[row][column] == 0 else 0,
                )

    def __print_current_tetromino(self):
        for i, block_row in enumerate(self.board.current_tetromino.dimensions):
            for j, block_element in enumerate(block_row):
                pos = (
                    j * self.board.cell_size + SCREEN_RESOLUTION[0] / 2 - self.board.size[0] / 2 + self.board.block_offset[0] * self.board.cell_size,
                    i * self.board.cell_size + SCREEN_RESOLUTION[1] / 2 - self.board.size[1] / 2 + self.board.block_offset[1] * self.board.cell_size,
                    self.board.cell_size,
                    self.board.cell_size,
                )
                if block_element != 0:
                    pygame.draw.rect(
                        self.screen,
                        COLORS[block_element],
                        pos,
                        0,
                    )

    def __print_next_tetromino(self):
        text = f"{NEXT_TETROMINO}:"
        text_color = TEXT_COLOR
        text_surface = self.font.render(text, True, text_color)
        self.screen.blit(text_surface, (800, 60))

        for i, block_row in enumerate(self.board.next_tetromino.dimensions):
            for j, block_element in enumerate(block_row):
                pos = (
                    j * self.board.cell_size + SCREEN_RESOLUTION[0] / 2 + self.board.size[0] / 2 + self.board.cell_size,
                    i * self.board.cell_size + SCREEN_RESOLUTION[1] / 2 - self.board.size[1] / 2 + self.board.cell_size,
                    self.board.cell_size,
                    self.board.cell_size,
                )
                if block_element != 0:
                    pygame.draw.rect(
                        self.screen,
                        COLORS[block_element],
                        pos,
                        0,
                    )

    def __print_score(self):
        text = f"{SCORE}: {self.board.score}"
        text_color = TEXT_COLOR
        text_surface = self.font.render(text, True, text_color)
        self.screen.blit(text_surface, (100, 60))

    def print_board(self):
        self.__print_field()
        self.__print_current_tetromino()
        self.__print_next_tetromino()
        self.__print_score()

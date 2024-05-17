import pygame
from board import Board
from constants.colors import BACKGROUND_COLOR
from constants.config import WINDOW_TITLE, SCREEN_RESOLUTION, FPS
from printer import Printer
from ai import AI

pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 32)
board = Board()
printer = Printer(board, screen, font)
ai = AI(board)
time_delay = 200
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)


def main():
    while board.game_is_running:
        clock.tick(FPS)
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board.current_tetromino.move(-1, 0)
                if event.key == pygame.K_RIGHT:
                    board.current_tetromino.move(1, 0)
                if event.key == pygame.K_UP:
                    board.current_tetromino.rotate()

            if event.type == timer_event:
                # ai.best_move(board)
                board.current_tetromino.move(0, 1)

        printer.print_board()
        pygame.display.update()


main()

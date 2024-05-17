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
player_board = Board("Jugador")
ai_board = Board("IA")
player_printer = Printer(player_board, screen, font, 0)
ai_printer = Printer(ai_board, screen, font, 640)
ai = AI(ai_board)
time_delay = 200
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, time_delay)


def main():
    while player_board.game_is_running:
        clock.tick(FPS)
        screen.fill(BACKGROUND_COLOR)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player_board.current_tetromino.rotate()
                if event.key == pygame.K_DOWN:
                    player_board.current_tetromino.move(0, 1)
                if event.key == pygame.K_RIGHT:
                    player_board.current_tetromino.move(1, 0)
                if event.key == pygame.K_LEFT:
                    player_board.current_tetromino.move(-1, 0)

            if event.type == timer_event:
                player_board.current_tetromino.move(0, 1)
                # ai.best_move()

        player_printer.print_board()
        ai_printer.print_board()
        pygame.display.update()


main()

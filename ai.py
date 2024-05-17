def evaluate_board(board):
    height = 0
    lines_cleared = 0
    holes = 0

    # Calculate height
    for col in range(board.width):
        for row in range(board.height):
            if board.grid[row][col] != 0:
                height = max(height, board.height - row)
                break

    # Calculate lines cleared
    for row in range(board.height):
        if all(cell != 0 for cell in board.grid[row]):
            lines_cleared += 1

    # Calculate holes
    for col in range(board.width):
        block_found = False
        for row in range(board.height):
            if board.grid[row][col] != 0:
                block_found = True
            elif block_found and board.grid[row][col] == 0:
                holes += 1

    # You can adjust the weights as needed
    score = (-0.5 * height) + (1.0 * lines_cleared) - (0.7 * holes)
    return score


class AI:
    def __init__(self, board):
        self.board = board
        self.heightWeight = 0.510066
        self.linesWeight = 0.760666
        self.holesWeight = 0.35663
        self.bumpinessWeight = 0.184483

    def best_move(self, board):
        best_score = float('-inf')
        best_position = None
        best_rotation = 0

        original_x = board.block_offset[0]
        original_y = board.block_offset[1]
        original_rotation = board.current_tetromino.dimensions

        for rotation in range(4):
            board.current_tetromino.dimensions = (original_rotation + rotation) % 4
            for x in range(board.width):
                board.block_offset[0] = x
                board.block_offset[1] = original_y

                if board.valid_position(board.current_tetromino):
                    while board.valid_position(board.current_tetromino, offset=(0, 1)):
                        board.block_offset[1] += 1

                    board.lock_tetromino()
                    score = evaluate_board(board)
                    board.undo_lock_tetromino()

                    if score > best_score:
                        best_score = score
                        best_position = x
                        best_rotation = board.current_tetromino.dimensions

        board.block_offset[0] = original_x
        board.block_offset[1] = original_y
        board.current_tetromino.dimensions = original_rotation

        if best_position is not None:
            board.block_offset[0] = best_position
            board.current_tetromino.dimensions = best_rotation

            while board.valid_position(board.current_tetromino, offset=(0, 1)):
                board.block_offset[1] += 1
            board.lock_tetromino()

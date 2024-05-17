import copy

class AI:
    def __init__(self, board):
        self.board = board
        self.height_weight = -0.510066
        self.lines_weight = 0.760666
        self.holes_weight = -0.35663
        self.bumpiness_weight = -0.184483

    def evaluate_board(self, board):
        height = self.get_height(board)
        lines = self.count_complete_lines(board)
        holes = self.count_holes(board)
        bumpiness = self.calculate_bumpiness(board)
        
        return height * self.height_weight + lines * self.lines_weight + holes * self.holes_weight + bumpiness * self.bumpiness_weight

    def get_height(self, board):
        heights = [max([y for y in range(len(board)) if board[y][x] != 0], default=0) for x in range(len(board[0]))]
        return max(heights)

    def count_complete_lines(self, board):
        return sum([1 for row in board if all(cell != 0 for cell in row)])

    def count_holes(self, board):
        holes = 0
        for x in range(len(board[0])):
            block_found = False
            for y in range(len(board)):
                if board[y][x] != 0:
                    block_found = True
                elif block_found:
                    holes += 1
        return holes

    def calculate_bumpiness(self, board):
        heights = [max([y for y in range(len(board)) if board[y][x] != 0], default=0) for x in range(len(board[0]))]
        bumpiness = sum([abs(heights[i] - heights[i + 1]) for i in range(len(heights) - 1)])
        return bumpiness
    
    def best_move(self):
        best_score = float('-inf')
        best_rotation = 0
        best_x = 0
        
        original_board = copy.deepcopy(self.board.grid)
        original_tetromino = copy.deepcopy(self.board.current_tetromino)
        original_offset = copy.deepcopy(self.board.block_offset)

        for rotation in range(4):
            for x in range(self.board.columns):
                self.board.current_tetromino = copy.deepcopy(original_tetromino)
                for _ in range(rotation):
                    self.board.current_tetromino.rotate()
                self.board.block_offset = [x, 0]

                # Mover hacia abajo hasta que colisione
                while not self.board.detect_collision():
                    self.board.block_offset[1] += 1
                self.board.block_offset[1] -= 1

                self.board.lock_tetromino()
                score = self.evaluate_board(self.board.grid)
                
                if score > best_score:
                    best_score = score
                    best_rotation = rotation
                    best_x = x
                
                self.board.grid = copy.deepcopy(original_board)

        # Restaurar estado original y aplicar el mejor movimiento
        self.board.current_tetromino = original_tetromino
        self.board.block_offset = original_offset
        for _ in range(best_rotation):
            self.board.current_tetromino.rotate()
        self.board.block_offset[0] = best_x
        
        # Mover hacia abajo hasta que colisione
        while not self.board.detect_collision():
            self.board.block_offset[1] += 1
        self.board.block_offset[1] -= 1
        self.board.lock_tetromino()

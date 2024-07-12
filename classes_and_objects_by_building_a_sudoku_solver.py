class Board:
    def __init__(self, board):
        self.board = board
    def __str__(self):
        board_string = '\n'
        for row in self.board:
            row_string = [str(value) if value else '*' for value in row]
            board_string += ' '.join(row_string)
            board_string += '\n'
        return board_string
    def understandEmptyCellIndex(self):
        for row, content in enumerate(self.board):
            try:
                column = content.index(0)
                return row, column
            except ValueError:
                pass
        return None
    def isValidInRow(self, row_index, number):
        return number not in self.board[row_index]
    def isValidInColumn(self, column_index, number):
        return all([self.board[row_index][column_index] != number for row_index in range(len(self.board))])
    def isValidInSquare(self, row_index, column_index, number):
        start_row_index = row_index // 3 * 3
        for row_index in range(start_row_index, start_row_index + 3):
            start_column_index = column_index // 3 * 3
            for column_index in range(start_column_index, start_column_index + 3):
                if self.board[row_index][column_index] == number:
                    return False
                else: pass
        return True
    def isValidEntirely(self, empty_cell_index, number):
        row_index, column_index = empty_cell_index
        is_valid_in_row = self.isValidInRow(row_index, number)
        is_valid_in_column = self.isValidInColumn(column_index, number)
        is_valid_in_square = self.isValidInSquare(row_index, column_index, number)
        return all([is_valid_in_row, is_valid_in_column, is_valid_in_square])
    def solve(self):
        if (next_empty_cell_index := self.understandEmptyCellIndex()) is None:
            return True
        else:
            for guess in range(1, len(self.board) + 1):
                if self.isValidEntirely(next_empty_cell_index, guess):
                    row_index, column_index = next_empty_cell_index
                    self.board[row_index][column_index] = guess
                    if self.solve():
                        return True
                    else: self.board[row_index][column_index] = 0
                else: pass
            return False        
def solveSudoku(board):
    game_board = Board(board)
    print(f"\nPUZZLE TO SOLVE\n{game_board}")
    if game_board.solve():
        print(f"PUZZLE AFTERWARDS SOLVE\n{game_board}")
    else:
        print("THIS PUZZLE IS UNSOLVABLE.\n")
    return game_board
puzzle = [
    [0, 0, 2, 0, 0, 8, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 7, 6, 2],
    [4, 3, 0, 0, 0, 0, 8, 0, 0],
    [0, 5, 0, 0, 3, 0, 0, 9, 0],
    [0, 4, 0, 0, 0, 0, 0, 2, 6],
    [0, 0, 0, 4, 6, 7, 0, 0, 0],
    [0, 8, 6, 7, 0, 4, 0, 0, 0],
    [0, 0, 0, 5, 1, 9, 0, 0, 8],
    [1, 7, 0, 0, 0, 6, 0, 0, 5]
]
solveSudoku(puzzle)
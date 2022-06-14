class Board:
    def __init__(self):
        self.board = ["%"] * 9

    def display_board(self):
        for index, cell in enumerate(self.board):
            if index != 0 and index % 3 == 0:
                print()
            if index % 3 == 0:
                print("|", end="")
            print(f"{cell:^3}|", end="")

            # @staticmethod
    # def is_position_allowed(position):
        # if position not in range(1, 10):
            #raise BoardException()


    def is_cell_empty(self, position):
        return self.board[position - 1] == ""

    def is_board_full(self):
        return all(self.board)

    def fill_cell(self, position, sign):
        self.board[position - 1] = sign


if __name__ == '__main__':
    board = Board()
    print(board.board)
    board.board[7] = '*'
    board.display_board()

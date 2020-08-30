class ChessBoard(object):
    def __init__(self, size):
        # board has dimensions size x size
        self.size = size
        self.board = [["" for x in range(self.size)] for x in range(self.size)]

    def assign_queen(self, assign_row, assign_column):
        for row in range(self.size):
            for column in range(self.size):
                if row == assign_row and column == assign_column:
                    self.board[row][column] = "Q"
        return self.board

    def is_safe(self, row, column):

        # check this row on left side
        for item in range(column):
            if self.board[row][item] == "Q":
                return False

        # check upper diagonal on left side
        for i, j in zip(range(row, -1, -1), range(column, -1, -1)):
            if self.board[i][j] == "Q":
                return False

        # check lower diagonal on left side
        for i, j in zip(range(row, self.size, 1), range(column, -1, -1)):
            if self.board[i][j] == "Q":
                return False

        return True

    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                board_solution = (
                    self.board[row][column] if self.board[row][column] == "Q" else "."
                )
                print(board_solution, end="  ")
            print()
        return self.size * self.size


class SolveNQueen(ChessBoard):
    def __init__(self, size):
        self.number_of_solutions = 0
        self.size = size
        ChessBoard.__init__(self, size)

    def solve(self, column=0):
        # iterating over each row in column
        for row in range(self.size):
            # place the queen at the corresponding position, if it is safe, by updating the matrix with Q
            if self.is_safe(row, column):
                self.board[row][column] = "Q"
                # if we have not reached the last column it means that we have no solution
                if column < self.size - 1:
                    self.solve(column + 1)
                else:
                    # we have a solution and we show the board
                    self.number_of_solutions += 1
                    self.display()
                    print()
                # if not possible arrangement is found the backtrack and remove the queen
                self.board[row][column] = ""
        return self.number_of_solutions
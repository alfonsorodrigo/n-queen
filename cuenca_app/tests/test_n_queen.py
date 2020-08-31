import sys
import os

sys.path.append(os.getcwd())
import unittest
from n_queen import ChessBoard, SolveNQueen


class NQueenTestCase(unittest.TestCase):
    def setUp(self):
        self.four_dimensional_board = ChessBoard(4)
        self.eight_dimensional_board = ChessBoard(8)
        self.two_solve_n_queen = SolveNQueen(2)
        self.four_solve_n_queen = SolveNQueen(4)
        self.eight_solve_n_queen = SolveNQueen(8)
        self.nine_solve_n_queen = SolveNQueen(9)
        self.ten_solve_n_queen = SolveNQueen(10)

    def test_four_dimensional_valid(self):
        self.assertEqual(self.four_dimensional_board.display(), 16)

    def test_four_dimensional_not_valid(self):
        self.assertNotEqual(self.four_dimensional_board.display(), 0)

    def test_eight_dimensional_valid(self):
        self.assertEqual(self.eight_dimensional_board.display(), 64)

    def test_eight_dimensional_not_valid(self):
        self.assertNotEqual(self.eight_dimensional_board.display(), 0)

    def test_four_dimensional_is_not_safe_left_side(self):
        self.four_dimensional_board.assign_queen(2, 2)
        board_is_safe = self.four_dimensional_board.is_safe(2, 3)
        self.assertEqual(board_is_safe, False)

    def test_four_dimensional_is_not_safe_upper_diagonal_left_side(self):
        self.four_dimensional_board.assign_queen(1, 1)
        board_is_safe = self.four_dimensional_board.is_safe(3, 3)
        self.assertEqual(board_is_safe, False)

    def test_four_dimensional_is_not_safe_lower_diagonal_left_side(self):
        self.four_dimensional_board.assign_queen(3, 0)
        board_is_safe = self.four_dimensional_board.is_safe(0, 3)
        self.assertEqual(board_is_safe, False)

    def test_four_dimensional_is_safe_left_side(self):
        self.four_dimensional_board.assign_queen(1, 2)
        board_is_safe = self.four_dimensional_board.is_safe(1, 1)
        self.assertEqual(board_is_safe, True)

    def test_four_dimensional_is_safe_upper_diagonal_left_side(self):
        self.four_dimensional_board.assign_queen(2, 2)
        board_is_safe = self.four_dimensional_board.is_safe(1, 0)
        self.assertEqual(board_is_safe, True)

    def test_four_dimensional_is_safe_lower_diagonal_left_side(self):
        self.four_dimensional_board.assign_queen(2, 0)
        board_is_safe = self.four_dimensional_board.is_safe(0, 3)
        self.assertEqual(board_is_safe, True)

    def test_eight_dimensional_is_not_safe_left_side(self):
        self.eight_dimensional_board.assign_queen(4, 5)
        board_is_safe = self.eight_dimensional_board.is_safe(4, 6)
        self.assertEqual(board_is_safe, False)

    def test_eight_dimensional_is_not_safe_upper_diagonal_left_side(self):
        self.eight_dimensional_board.assign_queen(3, 2)
        board_is_safe = self.eight_dimensional_board.is_safe(4, 3)
        self.assertEqual(board_is_safe, False)

    def test_eight_dimensional_is_not_safe_lower_diagonal_left_side(self):
        self.eight_dimensional_board.assign_queen(4, 2)
        board_is_safe = self.eight_dimensional_board.is_safe(3, 3)
        self.assertEqual(board_is_safe, False)

    def test_eight_dimensional_is_safe_left_side(self):
        self.eight_dimensional_board.assign_queen(1, 2)
        board_is_safe = self.eight_dimensional_board.is_safe(1, 1)
        self.assertEqual(board_is_safe, True)

    def test_eight_dimensional_is_safe_upper_diagonal_left_side(self):
        self.eight_dimensional_board.assign_queen(4, 4)
        board_is_safe = self.eight_dimensional_board.is_safe(5, 6)
        self.assertEqual(board_is_safe, True)

    def test_eight_dimensional_is_safe_lower_diagonal_left_side(self):
        self.eight_dimensional_board.assign_queen(4, 4)
        board_is_safe = self.eight_dimensional_board.is_safe(3, 6)
        self.assertEqual(board_is_safe, True)

    def test_two_dimensional_solution(self):
        self.assertEqual(self.two_solve_n_queen.solve(), 0)

    def test_four_dimensional_solution(self):
        self.assertEqual(self.four_solve_n_queen.solve(), 2)

    def test_eight_dimensional_solution(self):
        self.assertEqual(self.eight_solve_n_queen.solve(), 92)

    def test_nine_dimensional_solution(self):
        self.assertEqual(self.nine_solve_n_queen.solve(), 352)

    def test_ten_dimensional_solution(self):
        self.assertEqual(self.ten_solve_n_queen.solve(), 724)


if __name__ == "__main__":
    unittest.main()

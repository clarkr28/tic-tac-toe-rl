# unit tests for the board
import unittest
from game_core import Board


class TestEmptySpaces(unittest.TestCase):

    def test_empty_board(self):
        board = Board()
        self.assertTrue(board.empty_spaces())

    def test_mixed_board(self):
        board = Board()
        board.set_cell(0, 0, 1)
        self.assertTrue(board.empty_spaces())
        board.set_cell(0, 1, 2)
        self.assertTrue(board.empty_spaces())

    def test_full_board(self):
        board = Board()
        for row in range(3):
            for col in range(3):
                board.set_cell(row, col, 1)
        self.assertFalse(board.empty_spaces())


class TestGetSet(unittest.TestCase):

    def test_get_set(self):
        board = Board()
        self.assertEqual(board.get_cell(0, 0), 0)
        board.set_cell(0, 0, 1)
        self.assertEqual(board.get_cell(0, 0), 1)
        board.set_cell(0, 0, 2)
        self.assertEqual(board.get_cell(0, 0), 2)


class TestQuantify(unittest.TestCase):

    def test_1(self):
        board = Board()
        self.assertEqual(board.quantify(1), 0)
        board.set_cell(0, 0, 2)
        self.assertEqual(board.quantify(1), 2)
        board.set_cell(0, 0, 1)
        self.assertEqual(board.quantify(1), 1)
        board.set_cell(0, 1, 2)
        self.assertEqual(board.quantify(1), 1 + 6)
        board.set_cell(0, 2, 1)
        self.assertEqual(board.quantify(1), 1 + 6 + 9)

    def test_2(self):
        board = Board()
        board.set_cell(2, 2, 1)
        self.assertEqual(board.quantify(1), 3**8)


class TestWinnerChecking(unittest.TestCase):

    def test_empty_board(self):
        board = Board()
        result = board.winner_check()
        self.assertFalse(result[0])
        self.assertEqual(len(result), 1)

    def test_top_row(self):
        board = Board()
        board.set_cell(0, 0, 1)
        board.set_cell(0, 1, 1)
        board.set_cell(0, 2, 1)
        result = board.winner_check()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 1)

    def test_middle_row(self):
        board = Board()
        board.set_cell(1, 0, 1)
        board.set_cell(1, 1, 1)
        board.set_cell(1, 2, 1)
        result = board.winner_check()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 1)

    def test_bottom_row(self):
        board = Board()
        board.set_cell(2, 0, 2)
        board.set_cell(2, 1, 2)
        board.set_cell(2, 2, 2)
        result = board.winner_check()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 2)

    def test_left_column(self):
        board = Board()
        board.set_cell(0, 0, 1)
        board.set_cell(1, 0, 1)
        board.set_cell(2, 0, 1)
        result = board.winner_check()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 1)

    def test_middle_column(self):
        board = Board()
        board.set_cell(0, 1, 1)
        board.set_cell(1, 1, 1)
        board.set_cell(2, 1, 1)
        result = board.winner_check()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 1)

    def test_right_column(self):
        board = Board()
        board.set_cell(0, 2, 1)
        board.set_cell(1, 2, 1)
        board.set_cell(2, 2, 1)
        result = board.winner_check()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 1)

    def test_diag_1(self):
        board = Board()
        board.set_cell(0, 0, 1)
        board.set_cell(1, 1, 1)
        board.set_cell(2, 2, 1)
        result = board.winner_check()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 1)

    def test_diag_2(self):
        board = Board()
        board.set_cell(0, 2, 1)
        board.set_cell(1, 1, 1)
        board.set_cell(2, 0, 1)
        result = board.winner_check()
        self.assertTrue(result[0])
        self.assertEqual(result[1], 1)



if __name__ == '__main__':
    unittest.main()

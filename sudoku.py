#Sudoku Solver Challenge Version 1.0
#Group: Justin Cordero, Andrew Austin, Michael Orland, Diana Vargas
from sudoku_sampler import sudoku_selector

class SudokuSolver:
    def __init__(self):
        self.input_data = sudoku_selector()
        # list of lists representing each row
        self.board_data = self._input_to_useable_data()
        self.board = self.print_board()  # prints formatted board to terminal
    
    def _print_solved(self, solved_board_data):
        """Updates self.board with the solved board data"""
        self.board = self.print_board(solved_board_data)

    def _find_zero(self):
        """Search through self.board_data and return coordinates of
            first zero [row_index, col_index]"""
        for row_index, row in enumerate(self.board_data):
            for col_index, num in enumerate(row):
                if num == 0:
                    coord = [row_index, col_index]
                    return coord
        return False  # no empty spaces on board

    def _is_valid(self, coord, val):
        """Takes a number(val) and coordinate on the game board (row_index, col_index) and checks
            each value in the row, col, and 3x3 grid to check if the number(val) is a valid option
            for that position. Returns a boolean"""
        row, col = coord

        # check row
        for i in range(9):
            if self.board_data[row][i] == val and col != i:
                return False
        # check column

            if self.board_data[i][col] == val and row != i:
                return False

        # check grid
        upper_limit = (row // 3) * 3
        right_limit = (col // 3) * 3
        values_in_grid = []
        for rows in self.board_data[upper_limit:upper_limit + 3]:
            for num in rows[right_limit:right_limit + 3]:
                values_in_grid.append(num)
        if val in values_in_grid:
                return False
        return True

    def solve(self, updated_board = []):
        """Solves the board using the backtracking algorithm. When there are no more empty spaces
            to check, it updates the self.board via self._print_solved method and returns True.
            If the game is unsolveable, it returns False"""
        if updated_board == []:
            updated_board = self.board_data
        else:
            self.board_data = updated_board
        # base case (board has no empty spaces - represented by 0
        empty_space = self._find_zero()
        if not empty_space:
            self._print_solved(updated_board)
            return True  # game is solved
        row, col = empty_space        
            
        # try 1-9, if guess is valid, plug into board
        for guess in range(1, 10):
            if self._is_valid((row, col), guess):
                updated_board[row][col] = guess
                if self.solve():
                    return True
                updated_board[row][col] = 0
        # if it wasn't solved backtrack and reset last guess to 0 because
        # we couldn't solve the board based on the last value we added
        return False

    def print_board(self, board_data = []):
        """Uses self.board_data to return a string that accurately represents the sudoku
        board in the terminal"""
        if board_data == []:
            board_data = self.board_data
        board_visual = ""
        for i in range(len(board_data)):  # current row
            if i % 3 == 0:
                board_visual += "---------------------\n"
            for j in range(9):  # current number in row
                if j % 3 == 0 and j != 0:
                    board_visual += "| "
                if j == 8:
                    board_visual += f"{board_data[i][j]}\n"
                else:
                    board_visual += f"{board_data[i][j]} "
        board_visual += "---------------------"
        return board_visual

    def _input_to_useable_data(self):
        """Takes the string input and converts it to one list
        which contains 9 lists of numbers from 0-9 representing
        each row of the game board (0 indicates empty space)"""
        board_chars = [char for char in self.input_data]
        string_board = [
            board_chars[i * 9:(i + 1) * 9] for i in range((len(board_chars) + 8) // 9)]
        game_board = []
        for row in string_board:
            game_board.append(list(map(int, row)))
        return game_board


game = SudokuSolver()
print(game.board)
game.solve()
print(game.board)

import os
from read_input import get_input


class CeresSearch:
    def __init__(self, input_data_path: str):
        self.input_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), input_data_path))
        self.input_data = get_input(input_data_path).splitlines()
        
        self.rows = len(self.input_data)
        self.cols = len(self.input_data[0])
        self.count = 0
   
    def is_valid_position(self, row: int, col: int) -> bool:
       return 0 <= row < self.rows and 0 <= col < self.cols
    
    def get_top_right_diagonal(self, row: int, col: int, k: int) -> list[str]:
        diagonal = []

        cr, cc = row, col

        if not self.is_valid_position(cr, cc):
            return []

        diagonal.append(self.input_data[cr][cc])
        for i in range(k - 1):
            cr -= 1
            cc += 1

            if not self.is_valid_position(cr, cc):
                return []
            diagonal.append(self.input_data[cr][cc])

        return diagonal
    
    def get_top_left_diagonal(self, row: int, col: int, k: int) -> list[str]:
        diagonal = []

        cr, cc = row, col

        if not self.is_valid_position(cr, cc):
            return []

        diagonal.append(self.input_data[cr][cc])
        for i in range(k - 1):
            cr -= 1
            cc -= 1

            if not self.is_valid_position(cr, cc):
                return []

            diagonal.append(self.input_data[cr][cc])
        return diagonal

    def get_bottom_right_diagonal(self, row: int, col: int, k: int) -> list[str]:
        diagonal = []

        cr, cc = row, col

        if not self.is_valid_position(cr, cc):
            return []

        diagonal.append(self.input_data[cr][cc])
        for i in range(k - 1):
            cr += 1
            cc += 1

            if not self.is_valid_position(cr, cc):
                return []

            diagonal.append(self.input_data[cr][cc])
        
        return diagonal

    def get_bottom_left_diagonal(self, row: int, col: int, k: int) -> list[str]:
        diagonal = []

        cr, cc = row, col
        
        if not self.is_valid_position(cr, cc):
            return []

        diagonal.append(self.input_data[cr][cc])
        for i in range(k - 1):
            cr += 1
            cc -= 1
        
            if not self.is_valid_position(cr, cc):
                return []

            diagonal.append(self.input_data[cr][cc])
        
        return diagonal

    def find_linear_xmas(self, row, col) -> None:
                
        if col + 3 < self.cols and self.input_data[row][col:col+4] == "XMAS":
            self.count += 1
        if col - 3 >= 0 and self.input_data[row][col-3:col+1] == "SAMX":
            self.count += 1
        if row - 3 >= 0 and [r[col] for r in self.input_data[row-3:row+1]] == ['S', 'A', 'M', 'X']:
            self.count += 1
        if row + 3 < self.rows and [r[col] for r in self.input_data[row:row+4]] == ['X', 'M', 'A', 'S']:
            self.count += 1
        if col + 3 < self.cols and row - 3 >= 0 and self.get_top_right_diagonal(row, col, 4) == ['X', 'M', 'A', 'S']:
            self.count += 1
        if col + 3 < self.cols and row + 3 < self.rows and self.get_bottom_right_diagonal(row, col, 4) == ['X', 'M', 'A', 'S']:
            self.count += 1
        if col - 3 >= 0 and row - 3 >= 0 and self.get_top_left_diagonal(row, col, 4) == ['X', 'M', 'A', 'S']:
            self.count += 1
        if col -3 >= 0 and row + 3 < self.rows and self.get_bottom_left_diagonal(row, col, 4) == ['X', 'M', 'A', 'S']:
            self.count += 1

    def search_linear_xmas(self) -> int:
        
        self.count = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if self.input_data[i][j] == 'X':
                    self.find_linear_xmas(i, j)
                    
        return self.count
    
    def find_cross_xmas(self, row: int, col: int) -> None:
        
        if row > 0 and row < self.rows - 1 and col > 0 and col < self.cols - 1:
            main_diagonal = self.input_data[row - 1][col - 1] + self.input_data[row][col] + self.input_data[row + 1][col + 1]
            second_diagonal = self.input_data[row + 1][col - 1] + self.input_data[row][col] + self.input_data[row - 1][col + 1]

            if (main_diagonal == "MAS" or main_diagonal == "SAM") and (second_diagonal == "MAS" or second_diagonal == "SAM"):
                self.count += 1

    def search_cross_xmas(self) -> int:
        
        self.count = 0

        for i in range(self.rows):
            for j in range(self.cols):
                if self.input_data[i][j] == 'A':
                    self.find_cross_xmas(i, j)

        return self.count
                    

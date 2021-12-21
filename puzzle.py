class Puzzle():
    """Sudoku Puzzle class"""
    def __init__(self, grid = None):
        self.grid = grid
        self.row = 0
        self.col = 0
        self.m = 9

    def solve(self, grid, row, col, num):
        for x in range(9):
            if grid[row][x] == num:
                return False
                
        for x in range(9):
            if grid[x][col] == num:
                return False
    
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if grid[i + startRow][j + startCol] == num:
                    return False
        return True
    
    def sudoku(self, grid, row, col):
        if (row == self.m - 1 and col == self.m):
            return True
        if col == self.m:
            row += 1
            col = 0
        if self.grid[row][col] > 0:
            return self.sudoku(grid, row, col + 1)
        for num in range(1, self.m + 1, 1): 
        
            if self.solve(self.grid, row, col, num):
            
                self.grid[row][col] = num
                if self.sudoku(grid, row, col + 1):
                    return True
            self.grid[row][col] = 0
        return False

    def show_puzzle(self, a):
        return a

    def final_answer(self):
        if (self.sudoku(self.grid, 0, 0)):
            return self.show_puzzle(self.grid)
        else:
            return None
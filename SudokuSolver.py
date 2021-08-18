def find_next_empty(puzzle):
    # find next row,col on the puzzzle that's not filled --> rep with -1
    # return row, col tuple or (None, None) if there is none

    # we are using 0-8 for our indices
    for r in range(9):
        for c in range(9): # range(9) --> 0,1,2,...8
            if puzzle[r][c] == 0:
                return r,c

    return None,None


def is_valid(puzzle , guess , row , col):
    # let's start with row
    row_val = puzzle[row]
    if guess in row_val:
        return False

    # now the column
    col_val = []
    for i in range(9):
        col_val.append(puzzle[i][col])
    if guess in col_val:
        return False

    # and now the square
    # we want to get where the 3x3 square starts
    # and iterate over the 3 values in the row column
    row_start = (row // 3) * 3      # 1 // 3 = 0 , 5 // 3 = 1 
    col_start = (col // 3) * 3

    for r in range(row_start , row_start + 3):
        for c in range(col_start , col_start + 3):
            if puzzle[r][c] == guess:
                return False

    #if we get here , these checks pass
    return True

def solve_sudoku(puzzle):
    #solve sudoku using backtracking
    #our puzzle is a list of list, where each inner list is a row

    #step 1: choose somewhere to make a guess
    row , col = find_next_empty(puzzle)

    # step1.1 : if there is nowhere left, then we are done because 
    # we only allowed valid inputs
    if row is None:
        return True
        
    # step 2: if there is a place to put a number, then make a guess bet 1 to 9
    for guess in range(1, 10):
        # step 3: check if a valid guess
        if is_valid(puzzle , guess , row , col):
            # step 3.1 : if this is valid , then place the guess on the puzzle
            puzzle[row][col] = guess

            # now recurse using this puzzle
            # step 4 : recursively call our function
            if solve_sudoku(puzzle):
                return True

        # step 5 : if not valid OR our guess does not solve the puzzle,
        # then we need to backtrack and try a new number
        puzzle [row][col] = 0 # reset the guess

    # step 6 : if none of the numbers that we try does not work , then the sudoku is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, 0,        0, 5, 0,       0, 0, 0],
        [0, 0, 0,        2, 0, 0,       0, 0, 5],
        [0, 0, 0,        7, 1, 9,       0, 8, 0],

        [0, 5, 0,       0, 6, 8 ,       1, 0, 0],
        [2, 0, 6,       0, 0, 3,        0, 0, 0],
        [0, 0, 0,       0, 0, 0,        0, 0, 4],

        [5, 0, 0,       0, 0, 0,       0, 0, 0],
        [6, 7, 0,       1, 0, 5,       0, 4, 0],
        [1, 0, 9,       0, 0, 0,       2, 0, 0]
    ]

    (solve_sudoku(example_board))
    print(example_board)

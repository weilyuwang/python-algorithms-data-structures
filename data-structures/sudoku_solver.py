board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(bo):
    """
    Function to print out the board on console
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                # end="" means we won't print out '\n' at the end
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])  # go to next line
            else:
                print(str(bo[i][j]) + " ", end="")  # stay on the same line


def find_empty(bo):
    """
    Return the location (i, j) of the next empty slot on the board
    """
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col
    return None


def valid(bo, num, pos):
    """
    Given a value and its location, check if it is valid
    """
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False  # if found a same number in the same row, return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False  # if found a same number in the same column, return False

    # Check box
    # 3 x 3 = 9 boxes in total, each box has an unique location index, from (0,0) to (2,2)
    # First need to find out which box the number is in
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    # Loop through the elements in the box
    for i in range(box_y * 3, box_y * 3 + 3):       # row
        for j in range(box_x * 3, box_x * 3 + 3):   # column
            if bo[i][j] == num and pos != (i, j):
                return False

    return True


def solve(bo):
    """
    Given a board, solve the sudoku and return the result (True / False)
    With Backtracking
    """
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find  # next empty slot

    for i in range(1, 10):  # from 1 to 9
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            # else, set the slot back to empty and try the next i value (backtrack)
            bo[row][col] = 0

    # If we reach to this point, then it means that no solution was found, return False
    return False


# print_board(board)
# solve(board)
# print("\n-----------------------\n")
# print_board(board)

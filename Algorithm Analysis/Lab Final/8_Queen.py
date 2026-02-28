def is_safe(board, row, col, n):
    # Row check
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Upper left diagonal check
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Lower left diagonal check
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_nq(board, col, n):
    if col >= n:  # All queens are placed
        return True

    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1   # Queen is placed
            if solve_nq(board, col + 1, n):
                return True
            board[row][col] = 0   # backtrack

    return False

# -------- Test --------
n = 4
board = [[0 for _ in range(n)] for _ in range(n)] # Initialize the board with 0s

if solve_nq(board, 0, n):
    for row in board:
        print(row)
else:
    print("No solution")
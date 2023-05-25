#!/usr/bin/python3
"""ALX interview prep"""
import sys


def is_safe(board, row, col, N):
    """Check if a queen can be placed at the given position
    without attacking any other queens on the board

    Check the current column on the same row"""
    for i in range(col):
        if board[row][i] == "Q":
            return False

    # Check the upper diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # Check the lower diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == "Q":
            return False
        i += 1
        j -= 1

    return True


def solve_nqueens(N):
    """Create an empty NxN board"""
    board = [["." for _ in range(N)] for _ in range(N)]

    def backtrack(col):
        """Base case: All queens have been placed"""
        if col >= N:
            # Print the solution
            for row in range(N):
                print("".join(board[row]))
            print()
            return

        # Try placing a queen in each row of the current column
        for row in range(N):
            if is_safe(board, row, col, N):
                # Place the queen at the current position
                board[row][col] = "Q"

                # Recursively solve for the next column
                backtrack(col + 1)

                # Remove the queen from the current position (backtracking)
                board[row][col] = "."

    # Start solving from the first column (0)
    backtrack(0)


if __name__ == "__main__":
    # Check the command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N Queens problem
    solve_nqueens(N)

#!/usr/bin/python3
"""Module implements nQueens"""
import sys

solutions = []
board_size = 0
positions = None


def get_board_size():
    """
    Retrieves and validates the board size from the command-line argument.

    Returns:
        int: The size of the chessboard.
    """
    global board_size
    board_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def is_queen_attacking(position1, position2):
    """
    Checks if two queens are attacking each other.

    Args:
        position1 (tuple): The position of the first queen (row, column).
        position2 (tuple): The position of the second queen (row, column).

    Returns:
        bool: True if the queens are attacking each other, False otherwise.
    """
    return (
        position1[0] == position2[0]
        or position1[1] == position2[1]
        or abs(position1[0] - position2[0]) == abs(position1[1] - position2[1])
    )


def is_group_existing(group):
    """
    Checks if a group of positions already exists in the list of solutions.

    Args:
        group (list): The group of positions to check.

    Returns:
        bool: True if the group already exists, False otherwise.
    """
    global solutions
    for solution in solutions:
        if all(position in solution for position in group):
            return True
    return False


def build_solution(row, group):
    """
    Builds a solution for the N Queens problem recursively.

    Args:
        row (int): The current row to consider for placing the queen.
        group (list): The group of positions selected so far.
    """
    global solutions, board_size
    if row == board_size:
        if not is_group_existing(group):
            solutions.append(list(group))  # Convert tuple to list
    else:
        for col in range(board_size):
            current_position = (row, col)
            if not any(
                is_queen_attacking(current_position, position)
                for position in group
            ):
                group.append(current_position)
                build_solution(row + 1, group)
                group.pop()


def solve_nqueens():
    """
    Solves the N Queens problem and
    stores the solutions in the `solutions` list.
    """
    global positions, board_size
    positions = [(x // board_size, x % board_size)
                 for x in range(board_size**2)]
    build_solution(0, [])


if __name__ == "__main__":
    board_size = get_board_size()
    solve_nqueens()
    for solution in solutions:
        print([list(position) for position in solution])

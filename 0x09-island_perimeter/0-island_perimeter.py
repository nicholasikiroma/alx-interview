#!/usr/bin/python3
"""ALX Interview prep - Island Perimeter"""

def boundary(grid, i, j):
    """
    Find cells with either 4, 3, 2 or 1 exposed boundary and return them
    Args:
        grid (list): 2d list
        i (int): row number
        j (int): column number
    Returns:
        tuple: (boundaries, i, j)
            boundaries (int): Number of exposed boundaries
            i (int): row number
            j (int): column number
    """
    boundaries = 0

    if i == 0 or grid[i - 1][j] == 0:
        boundaries += 1
    if i == len(grid) - 1 or grid[i + 1][j] == 0:
        boundaries += 1
    if j == 0 or grid[i][j - 1] == 0:
        boundaries += 1
    if j == len(grid[0]) - 1 or grid[i][j + 1] == 0:
        boundaries += 1

    return boundaries, i, j


def island_perimeter(grid):
    """
    Calculate and return perimeter of island in the grid
    Grid is a rectangular grid where 0s represent water and 1s represent land
    Each cell is a square with a side length of 1
    There is only one island
    Args:
        grid (list): 2d list of ints either 0 or 1
    Returns:
        int: perimeter of island
    """
    if not grid:
        return 0

    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                boundaries, _, _ = boundary(grid, i, j)
                perimeter += boundaries

    return perimeter

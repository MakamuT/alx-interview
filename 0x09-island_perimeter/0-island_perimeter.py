#!/usr/bin/python3
"""
Create a function def island_perimeter(grid)
"""


def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4

                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2

    return perimeter

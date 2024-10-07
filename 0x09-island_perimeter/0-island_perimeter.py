#!/usr/bin/python3
"""
returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    perimeter = 0
    r = len(grid)
    c = len(grid[0]) if r > 0 else 0

    for n in range(r):
        for m in range(c):
            if grid[n][m] == 1:
                perimeter += 4

                if n > 0 and grid[n - 1][m] == 1:
                    perimeter -= 2

                if m > 0 and grid[n][m - 1] == 1:
                    perimeter -= 2

    return perimeter

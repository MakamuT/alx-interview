#!/usr/bin/python3
''' solving the island perimeter problem '''


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    visited = set()

    def dfs(n, m):
        if n < 0 or m < 0 or n >= rows or m >= cols or grid[n][m] == 0:
            return 1
        if (n, m) in visited:
            return 0

        visited.add((n, m))

        perimeter = dfs(n, m + 1)
        perimeter += dfs(n + 1, m)
        perimeter += dfs(n, m - 1)
        perimeter += dfs(n - 1, m)

        return perimeter

    for n in range(rows):
        for m in range(cols):
            if grid[n][m] == 1:
                return dfs(n, m)

    return 0

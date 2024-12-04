#!/usr/bin/python3
"""Module: 0-island_perimeter"""


def island_perimeter(grid):
    """
    Calculate the total perimeter of the island in the grid.

    Grid cells contain:
    1 - Land
    0 - Water

    The perimeter is calculated by checking for water or grid boundaries
    around each land cell.
    """
    perimeter = 0
    num_of_rows = len(grid)
    num_of_cols = len(grid[0])

    for x in range(num_of_rows):
        for y in range(num_of_cols):
            if grid[x][y] == 1:
                # Check each side
                if x == 0 or grid[x - 1][y] == 0:  # Top
                    perimeter += 1
                if y == 0 or grid[x][y - 1] == 0:  # Left
                    perimeter += 1
                if x == num_of_rows - 1 or grid[x + 1][y] == 0:  # Bottom
                    perimeter += 1
                if y == num_of_cols - 1 or grid[x][y + 1] == 0:  # Right
                    perimeter += 1

    return perimeter

#!/usr/bin/python3
"""
This module contains  a function def island_perimeter(grid):
that returns the perimeter of the island described in grid
"""


def island_perimeter(grid):
    """
    island_perimeter
    described by grid
    """
    perimeter = 0
    grid_len = len(grid)
    for row in range(grid_len):
        for col in range(len(grid[row])):
            if grid[row][col] == 1:
                if row - 1 < 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if col - 1 < 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col + 1 >= len(grid[row]) or grid[row][col + 1] == 0:
                    perimeter += 1
                if row + 1 >= grid_len or grid[row + 1][col] == 0:
                    perimeter += 1
    return perimeter

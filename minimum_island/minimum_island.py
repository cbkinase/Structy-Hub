from math import inf
from collections import deque
​
​
def minimum_island(grid):
    visited = set()
    smallest = inf
​
    for i in range(len(grid)):
        row = grid[i]
​
        for j in range(len(row)):
            cell = row[j]
​
            if cell == "L":
                if (i, j) not in visited:
                    island_size = find_island_size(grid, i, j, visited)
                    smallest = min(smallest, island_size)
​
    return smallest
​
​
def find_island_size(grid, r, c, visited):
    count = 0
    queue = deque([(r, c)])
    visited.add((r, c))
    while queue:
        row, col = queue.popleft()
        count += 1
        for x, y in get_neighbors(grid, row, col):
            if (x, y) not in visited:
                queue.append((x, y))
                visited.add((x, y))
    return count
​
​
def is_valid_tile(grid, r, c):
    if r not in range(len(grid)):
        return False
    if c not in range(len(grid[0])):
        return False
    if grid[r][c] == "W":
        return False
    return True
​
​
def get_neighbors(grid, r, c):
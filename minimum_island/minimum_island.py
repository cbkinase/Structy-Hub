
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
    left = (0, -1)
    right = (0, 1)
    up = (-1, 0)
    down = (1, 0)
​
    nodes = [left, right, up, down]
    neighbors = []
​
    for r_offset, c_offset in nodes:
        new_r = r + r_offset
        new_c = c + c_offset
​
        if is_valid_tile(grid, new_r, new_c):
            neighbors.append((new_r, new_c))
​
    return neighbors
​

def island_count(grid):
  visited = set()
  count = 0
  for i in range(len(grid)):
    row = grid[i]
    for j in range(len(row)):
      cell = row[j]
      
      if cell == "W":
        continue
        
      if (i, j) not in visited:
        count += 1
        dfs(grid, i, j, visited)
  return count
​
​
def dfs(grid, r, c, visited):
  if not is_valid_tile(grid, r, c):
    return
  
  if (r, c) in visited:
    return
  
  if grid[r][c] == "W":
    return
  
  visited.add((r, c))
  
  neighbors = get_neighbors(grid, r, c)
  for new_r, new_c in neighbors:
    dfs(grid, new_r, new_c, visited)
  
​
def largest_component(graph):
  visited = set()
  counts = []
  
  for node in graph:
    visited.add(node)
    count = dfs(graph, node, 0, visited)
    counts.append(count)
        
  return len(counts) and max(counts)
​
        
def dfs(graph, node, count, visited):
  stack = [node]
  
  while stack:
    curr = stack.pop()
    count += 1
    visited.add(curr)
    
    for neighbor in graph[curr]:
      if neighbor not in visited:
        stack.append(neighbor)
        visited.add(neighbor)
    
  return count
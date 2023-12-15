def has_path(graph, src, dst):
  stack = [*graph[src]]
  
  while stack:
    curr = stack.pop()
    
    if curr == dst:
      return True
    
    if graph[curr]:
      stack.extend(graph[curr])
  return False
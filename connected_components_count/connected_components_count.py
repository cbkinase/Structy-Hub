def connected_components_count(graph):
  visited = set()
  components = 0
  
  for node in graph:
    if is_isolated(graph, node, visited):
      components += 1
      
  return components
    
  
def is_isolated(graph, current, visited):
  if current in visited:
    return False
  
  visited.add(current)
  
  for neighbor in graph[current]:
    is_isolated(graph, neighbor, visited)
    
  return True
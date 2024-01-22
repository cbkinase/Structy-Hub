from collections import defaultdict
​
​
def make_adjacency_list(edges):
  rv = defaultdict(list)
  
  for src, dest in edges:
    rv[src].append(dest)
    rv[dest].append(src)
  
  return rv
​
​
def undirected_path(edges, node_A, node_B):
  adjacency_list = make_adjacency_list(edges)
  
  visited = set()
  
  stack = [node_A]
  
  while stack:
    node = stack.pop()
    visited.add(node)
    
    if node == node_B:
      return True
    next_nodes = adjacency_list[node]
    for next_node in next_nodes:
      if next_node not in visited:
        stack.append(next_node)
  
  return False
  
  
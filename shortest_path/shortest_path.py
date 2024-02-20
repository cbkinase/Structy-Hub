#       return len(stack) - 1
    
#     if all([neighbor in visited for neighbor in graph[curr]]):
#       stack.pop()
    
#     for neighbor in graph[curr]:
#       if neighbor not in visited:
#         stack.append(neighbor)
#         visited.add(neighbor)
        
#   return -1
​
def explore_min(graph, src, dest, count=0, prev=None, visited=None):
  # Work backwards: start by finding nodes that can find dest
  if src == dest:
    return count
  
  if prev == []:
    return inf
  
  if prev is None:
    prev = []
    
  if src in prev:
    return count
  
  if visited is None:
    visited = set()
  
  # stop if any stopping point found in prev
  stopping_point = graph[src]
  if any([node in stopping_point for node in prev]):
    return count + 1
  
  to_dest = [dest in graph[node] for node in graph]
  can_reach_dest = list(compress(graph.keys(), to_dest))
​
  out = inf
  for node in can_reach_dest:
    if node not in visited:
      visited.add(node)
      out = min(out, explore_min(graph, src, node, count+1, can_reach_dest, visited))
  return out
  
​
def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  m = explore_min(graph, node_A, node_B)
  if m == inf:
    return -1
  else:
    return m
  
    
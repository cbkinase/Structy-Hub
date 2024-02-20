
#   stopping_point = graph[src]
#   if any([node in stopping_point for node in prev]):
#     return count + 1
  
#   to_dest = [dest in graph[node] for node in graph]
#   can_reach_dest = list(compress(graph.keys(), to_dest))
​
#   out = inf
#   for node in can_reach_dest:
#     if node not in visited:
#       visited.add(node)
#       out = min(out, explore_min(graph, src, node, count+1, can_reach_dest, visited))
#   return out
  
​
def shortest_path(edges, node_A, node_B):
  graph = build_graph(edges)
  visited = set([node_A])
  queue = deque([(node_A, 0)])
  
  while queue:
    print(queue)
    node, depth = queue.popleft()
    
    if node == node_B:
      return depth
    
    for neighbor in graph[node]:
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append((neighbor, depth + 1))
  
  return -1
  
  
    
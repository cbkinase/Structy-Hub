# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
def all_tree_paths(root):
  paths = []
  stack = [root]
  visited = set()
  
  while stack:
    current = stack[-1]
    
    if current.left is None and current.right is None:
        paths.append([n.val for n in stack])
​
    if current.left and current.left not in visited:
      stack.append(current.left)
      visited.add(current.left)
    elif current.right and current.right not in visited:
      stack.append(current.right)
      visited.add(current.right)
    else:
      stack.pop()
  return paths
    
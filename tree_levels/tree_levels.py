# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
​
def tree_levels(root):
  if root is None:
    return []
  
  levels = []
  queue = deque([root])
  
  while queue:
    curr_level_length = len(queue)
    level_content = []
    
    for _ in range(curr_level_length):
      curr = queue.popleft()
      level_content.append(curr.val)
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
    levels.append(level_content)
  return levels
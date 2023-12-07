# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque
​
def level_averages(root):
  if root is None:
    return []
  averages = []
  queue = deque([root])
  
  while queue:
    level = []
    curr_level_length = len(queue)
    
    for _ in range(curr_level_length):
      curr = queue.popleft()
      level.append(curr.val)
      
      if curr.left:
        queue.append(curr.left)
        
      if curr.right:
        queue.append(curr.right)
    averages.append(sum(level) / len(level))
  return averages
      
​
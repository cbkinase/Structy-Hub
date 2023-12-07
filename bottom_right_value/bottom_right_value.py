# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
from collections import deque
​
​
def bottom_right_value(root):
  queue = deque([root])
  
  while queue:
    current_level_elements = len(queue)
    
    for _ in range(current_level_elements):
      curr = queue.popleft()
      
      if curr.left:
        queue.append(curr.left)
      if curr.right:
        queue.append(curr.right)
        
  return curr.val
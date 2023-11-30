# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
import math
from collections import deque
​
​
def tree_min_value(root):
  if root is None:
    return None
  
  min_val = math.inf
  queue = deque([root])
  
  while len(queue) > 0:
    current = queue.popleft()
    
    if current.val < min_val:
      min_val = current.val
    
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
      
  return min_val
  
  
  
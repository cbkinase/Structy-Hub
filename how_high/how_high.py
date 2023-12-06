# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
from collections import deque
​
​
def how_high(root):
  if root is None:
    return -1
​
  height = 0
  queue = deque([root])
​
  while queue:
    current_level_size = len(queue)
​
    for _ in range(current_level_size):
      current = queue.popleft()
​
      if current.left:
        queue.append(current.left)
      if current.right:
        queue.append(current.right)
​
    height += 1
​
  return height - 1
​
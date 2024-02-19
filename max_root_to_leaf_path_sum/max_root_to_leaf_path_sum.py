# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
import math
​
​
# def max_path_sum(root):
#   if root is None:
#     return -math.inf
  
#   if root.left is None and root.right is None:
#     return root.val
  
#   return root.val + max(max_path_sum(root.left), max_path_sum(root.right))
​
def max_path_sum(root):
  if not root:
      return None
​
  stack = [root]
  visited = set()
  results = []
​
  while stack:
    current = stack[-1]
​
    if current.right is None and current.left is None:
         results.append(sum([node.val for node in stack]))
​
    if current.left and current.left not in visited:
      stack.append(current.left)
      visited.add(current.left)
    elif current.right and current.right not in visited:
      stack.append(current.right)
      visited.add(current.right)
    else:
      stack.pop()
​
  return max(results)
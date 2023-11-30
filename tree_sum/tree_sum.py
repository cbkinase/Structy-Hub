# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
def tree_sum(root):
  total_sum = 0
  
  if root is None:
    return total_sum
  
  stack = [root]
  
  while len(stack) > 0:
    current = stack.pop()
    total_sum += current.val
    
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
  return total_sum
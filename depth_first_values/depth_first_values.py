class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
​
# def depth_first_values(root, vals=None):
#   if vals is None:
#     vals = []
​
#   if root is not None:
#     vals.append(root.val)
#     depth_first_values(root.left, vals)
#     depth_first_values(root.right, vals)
​
#   return vals
​
def depth_first_values(root):
  if root is None:
    return []
  
  vals = []
  stack = [root]
  
  while len(stack) > 0:
    current = stack.pop()
    vals.append(current.val)
    if current.right:
      stack.append(current.right)
    if current.left:
      stack.append(current.left)
  return vals
    
    
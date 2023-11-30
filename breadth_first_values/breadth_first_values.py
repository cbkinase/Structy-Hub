# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
def breadth_first_values(root):
  if root is None:
    return []
  
  vals = []
  queue = [root]
  
  while len(queue) > 0:
    current = queue.pop(0)
    vals.append(current.val)
    
    if current.left:
      queue.append(current.left)
    if current.right:
      queue.append(current.right)
      
  return vals
​
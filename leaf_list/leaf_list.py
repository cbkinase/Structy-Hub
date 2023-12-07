# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
def leaf_list(root):
  if root is None:
    return []
  
  leaves = []
  stack = [root]
  
  while stack:
    curr = stack.pop()
    
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
    if curr.left is None and curr.right is None:
      leaves.append(curr.val)
  return leaves
​
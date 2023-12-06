# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
​
​
def path_finder(root, target):
    if not root:
        return None
​
    stack = [root]
    path = [root.val]
    visited = set()
​
    while stack:
        current = stack[-1]
​
        if current.val == target:
            return path
​
        if current.left and current.left not in visited:
            stack.append(current.left)
            path.append(current.left.val)
            visited.add(current.left)
        elif current.right and current.right not in visited:
            stack.append(current.right)
            path.append(current.right.val)
            visited.add(current.right)
        else:
            stack.pop()
            path.pop()
​
    return None
​
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
    visited = set()
​
    while stack:
        current = stack[-1]
​
        if current.val == target:
            return [node.val for node in stack]
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
    return None
​
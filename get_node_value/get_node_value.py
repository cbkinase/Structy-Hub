# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def get_node_value(head, index):
  curr_idx = 0
  curr = head
  
  while curr is not None:
    if curr_idx == index:
      return curr.val
    curr_idx += 1
    curr = curr.next
​
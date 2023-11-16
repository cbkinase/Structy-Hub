# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def zipper_lists(head_1, head_2):
  detached = None
  curr = head_1
  subsequent = head_2
  prev = None
  
  while curr is not None:
    detached = curr.next    
    curr.next = subsequent  
    subsequent = detached
    prev = curr
    curr = curr.next
    
  if detached:
    prev.next = detached
    
  return head_1
​
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def reverse_list(head):
  pass
  pass
  prev_node = None
  curr = head
  nxt = curr.next
  
  while nxt is not None:
    # Get the next node
    nxt = curr.next
    
    # Point the next node in the LL to the previous node
    curr.next = prev_node
    prev_node = curr
    
    # Move forward in the list
    curr = nxt
    
  if prev_node:
    return prev_node
  else:
    return head
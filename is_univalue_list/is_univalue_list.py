# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def is_univalue_list(head):
  first = head.val
  
  while head:
    if head.val != first:
      return False
    else:
      head = head.next
  
  return True
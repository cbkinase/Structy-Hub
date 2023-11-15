class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
​
def merge_lists(head_1, head_2):
  current1 = head_1
  current2 = head_2
  dummy_head = Node(val=None)
  dummy_head_ref = dummy_head
  
  while current1 and current2:
    if current1.val <= current2.val:
      dummy_head.next = current1
      current1 = current1.next
    else:
      dummy_head.next = current2
      current2 = current2.next
    dummy_head = dummy_head.next
  
  if current1:
    dummy_head.next = current1
  
  if current2:
    dummy_head.next = current2
  
  return dummy_head_ref.next
​
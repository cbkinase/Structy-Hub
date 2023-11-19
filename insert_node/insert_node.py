class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
​
def insert_node(head, value, index):
  current = head
  current_idx = 0
  detached = None
  
  if index == 0:
    new_node = Node(val=value)
    new_node.next = head
    return new_node
  
  while current is not None:
    if current_idx + 1 == index:
      detached = current.next
      new_node = Node(val=value)
      current.next = new_node
      new_node.next = detached
      break
      
    current_idx += 1
    current = current.next
  return head
      
​
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
​
def get_list_vals(head):
  vals = []
  
  while head:
    vals.append(str(head.val))
    head = head.next
    
  vals.reverse()
  return int("".join(vals))
​
def add_lists(head_1, head_2):
  v1 = get_list_vals(head_1)
  v2 = get_list_vals(head_2)
  
  input_sum = str(v1 + v2)[::-1]
  
  head = Node(input_sum[0])
  current = head
  
  for val in input_sum[1:]:
    new_node = Node(val)
    current.next = new_node
    current = current.next
  return head
    
  
  
​
# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def linked_list_values(head):
    values = []
    curr = head
    while curr is not None:
        values.append(curr.val)
        curr = curr.next
    return values
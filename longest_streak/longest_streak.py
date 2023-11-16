# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None
​
def longest_streak(head):
  if head is None:
    return 0
  
  longest_streak = 0
  current_streak = 0
  current_streak_val = head.val
  
  while head:
    if head.val == current_streak_val:
      current_streak += 1
      if current_streak > longest_streak:
        longest_streak = current_streak
    else:
        current_streak = 1
        current_streak_val = head.val
        
    head = head.next
  
  return longest_streak
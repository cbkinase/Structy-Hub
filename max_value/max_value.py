import math
def max_value(nums):
  highest = -math.inf
  
  for num in nums:
    if num > highest:
      highest = num
      
  return highest
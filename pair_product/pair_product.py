def pair_product(numbers, target_product):
    prev = {}
  
    for idx, num in enumerate(numbers):
        counterpart = int(target_product / num)
        
        if counterpart in prev:
            return prev[counterpart], idx
        else:
            prev[num] = idx
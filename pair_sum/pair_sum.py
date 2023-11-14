def pair_sum(numbers, target_sum):
    pass
    pairs = {}
    
    for idx, num in enumerate(numbers):
        complement = target_sum - num
        
        if complement in pairs:
            return pairs[complement], idx
        else:
            pairs[num] = idx
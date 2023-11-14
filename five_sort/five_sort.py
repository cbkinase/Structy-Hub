def five_sort(nums):
    end_ptr = len(nums) - 1
    curr_ptr = 0
    while curr_ptr <= end_ptr:
        if nums[end_ptr] == 5:
            end_ptr -= 1
        elif nums[curr_ptr] == 5:
            nums[curr_ptr], nums[end_ptr] = nums[end_ptr], nums[curr_ptr]
            curr_ptr += 1
        else:
            curr_ptr += 1
    return nums
  
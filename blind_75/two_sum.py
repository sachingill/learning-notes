def two_sum(nums, target):
    # The array are ordered, so we can use inplace method to implement it
    sorted_nums = list(enumerate(nums))
    
    # Sort based on the values
    
    # Sort based on the values
    sorted_nums.sort(key=lambda x: x[1])
    print(sorted_nums)
    left = 0
    right = len(nums) - 1
    while left < right:
        current_sum = sorted_nums[left][1] + sorted_nums[right][1]
        if current_sum == target:
            return [sorted_nums[left][0], sorted_nums[right][0]]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return []

def two_sum_space(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
    return []

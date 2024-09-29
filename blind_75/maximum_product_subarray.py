def max_product(nums: list[int]) -> int:
    if not nums:
        raise ValueError("Input array is empty")
    max_so_far = min_so_far = result = nums[0]
    for num in nums[1:]:
        temp_max = max(num, max_so_far * num, min_so_far * num)
        min_so_far = min(num, max_so_far * num, min_so_far * num)
        max_so_far = temp_max
        result = max(result, max_so_far)
       
    return result
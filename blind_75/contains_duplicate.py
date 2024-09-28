from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    # Sort the list in ascending order
    nums = sorted(nums)

    i = 0;
    while i < len(nums)-1:
        if(nums[i] == nums[i+1]):
            return True
        i +=1
    return False

    
    
def conatains_duplicate_mem(nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


    
    # The rest of the function logic will go here
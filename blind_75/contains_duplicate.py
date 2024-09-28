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

    
    



    
    # The rest of the function logic will go here
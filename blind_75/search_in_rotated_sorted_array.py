def search(nums: list[int], target: int) -> int:
    if not nums:
       return -1
    if len(nums) <=1:
      return 0 if nums[0] == target else -1
    left = 0
    right = len(nums) -1
    
    while (left <= right):
        mid = (left + right) //2
        if (nums[mid] == target):
            return mid;
       
        if nums[left] <= nums[mid]:
           if nums[left] <= target < nums[mid]:
              right =  mid -1
           else:
              left = mid+1
        else:
           if nums[mid] < target <= nums[right]:
              left = mid + 1
           else:
              right = mid - 1
    return -1


    
    



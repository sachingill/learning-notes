def find_min(nums: list[int]) -> int:
  if not nums:
    raise ValueError(" Invalide Array list object.")
  if len(nums) <= 1:
    return nums[0]
  left = 0;
  right = len(nums) -1
 
  while (left < right):
    mid = (left + right)//2
    if mid < len(nums) - 1 and (nums[mid] > nums[mid+1]):
      return nums[mid+1]
    elif (nums[mid] > nums[right]):
      left = mid  + 1
    else:
      right = mid

  return nums[left]

  
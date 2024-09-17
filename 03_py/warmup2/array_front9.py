def array_front9(nums):
  valueAt = 0
  for i in range(min(len(nums), 4)):
    if nums[i] == 9:
      return True
  return False

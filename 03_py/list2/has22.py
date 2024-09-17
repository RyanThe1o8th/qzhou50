def has22(nums):
  hasTwo = False
  for i in range(len(nums)):
    if nums[i] == 2:
      if hasTwo:
        return True
      else:
        hasTwo = True
    else:
      hasTwo = False
  return False

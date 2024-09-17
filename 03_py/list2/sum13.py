def sum13(nums):
  if len(nums) == 0:
    return 0
  returnable = 0
  for i in range(len(nums)):
    if nums[i] != 13:
      if i != 0:
        if nums[i - 1] != 13:
          returnable = returnable + nums[i]
      else:
        returnable = returnable + nums[i]
  return returnable

def count_evens(nums):
  returnable = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      returnable = returnable + 1
  return returnable

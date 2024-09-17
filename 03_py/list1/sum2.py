def sum2(nums):
  returnable = 0
  for i in range(min(len(nums),2)):
    returnable = returnable + nums[i]
  return returnable

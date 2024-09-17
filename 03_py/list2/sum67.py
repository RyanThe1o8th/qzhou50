def sum67(nums):
  returnable = 0
  hasSixed = False
  for i in range(len(nums)):
    if hasSixed:
      if nums[i] == 7:
        hasSixed = False
    else:
      if nums[i] == 6:
        hasSixed = True
      else:
        returnable = returnable + nums[i]
  return returnable

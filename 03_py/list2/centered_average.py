def centered_average(nums):
  min1 = nums[0]
  max1 = nums[0]
  sumofall = 0
  for i in range(len(nums)):
    min1 = min(min1, nums[i])
    max1 = max(max1, nums[i])
    sumofall = sumofall + nums[i]
  return (sumofall - min1 - max1)/(len(nums)-2)

#
# LeetCode
#
# Problem - 368
# URL - https://leetcode.com/problems/largest-divisible-subset/description/
#

class Solution:
  def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
    nums.sort()

    dynamicP = {}
    ans = [nums[0]]
    for i in range(len(nums)):
      dynamicP[i] = [nums[i]]

      for j in range(i):
        if (
          nums[i] % nums[j] == 0 and 
          len(dynamicP[j]) + 1 > len(dynamicP[i])
        ):
          dynamicP[i] = dynamicP[j] + [nums[i]]

          if len(ans) < len(dynamicP[i]):
            ans = dynamicP[i]

    return ans

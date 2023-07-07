#
# LeetCode
#
# Problem - 209
# URL - https://leetcode.com/problems/minimum-size-subarray-sum/description/
#

class Solution:
  def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    ans = 0

    if sum(nums) < target:
      return ans
    
    ans = len(nums)
    currentSum = 0
    leftIndex = 0
    for i in range(len(nums)):
      currentSum += nums[i]

      while currentSum >= target:
        ans = min(ans, i - leftIndex + 1)
        currentSum -= nums[leftIndex]
        leftIndex += 1

    return ans

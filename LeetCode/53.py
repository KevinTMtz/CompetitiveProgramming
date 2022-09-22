#
# LeetCode
#
# Problem - 53
# URL - https://leetcode.com/problems/maximum-subarray/
#

class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    currentSum = float('-inf')
    maxSum = float('-inf')

    for num in nums:
      currentSum = max(currentSum + num, num)
      maxSum = max(maxSum, currentSum)
    
    return maxSum
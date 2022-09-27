#
# LeetCode
#
# Problem - 268
# URL - https://leetcode.com/problems/missing-number/
#

class Solution:
  def missingNumber(self, nums: List[int]) -> int:
    ans = len(nums)
    
    for i in range(0, len(nums)):
      ans = (ans ^ i) ^ nums[i]
      
    return ans

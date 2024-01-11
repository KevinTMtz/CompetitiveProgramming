#
# LeetCode
#
# Problem - 55
# URL - https://leetcode.com/problems/jump-game/description/
#

class Solution:
  def canJump(self, nums: List[int]) -> bool:
    dp = dict()

    return self.canJumpHelper(nums, 0, dp)

  def canJumpHelper(self, nums: List[int], index: int, dp: dict) -> bool:
    if index in dp:
      return dp[index]

    if index >= len(nums) - 1:
      dp[index] = True
      return dp[index]
    
    for i in range(nums[index], 0, -1):
      if self.canJumpHelper(nums, index + i, dp):
        dp[index] = True
        return dp[index]

    dp[index] = False
    return dp[index]
  
class EfficientSolution:
  def canJump(self, nums: List[int]) -> bool:
    max_range = 0

    for i in range(len(nums)):
      if (max_range < i):
        return False

      max_range = max(max_range, i + nums[i])

    return max_range >= len(nums) - 1
    
    
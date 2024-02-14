#
# LeetCode
#
# Problem - 494
# URL - https://leetcode.com/problems/target-sum/
#

class Solution:
  def findTargetSumWays(self, nums: List[int], target: int) -> int:
    dp = dict()

    return self.findTargetSumWaysHelper(nums, 0, target, 0, dp)

  def findTargetSumWaysHelper(self, nums: List[int], current: 0, target: int, i: int, dp: dict) -> int:
    if i >= len(nums) and current == target:
      return 1
    elif i >= len(nums):
      return 0

    if i in dp and current in dp[i]:
      return dp[i][current]

    if not i in dp:
      dp[i] = dict()

    dp[i][current] = (
      self.findTargetSumWaysHelper(nums, current + nums[i], target, i+1, dp) +
      self.findTargetSumWaysHelper(nums, current - nums[i], target, i+1, dp)
    )

    return dp[i][current]

#
# LeetCode
#
# Problem - 746
# URL - https://leetcode.com/problems/min-cost-climbing-stairs/submissions/
#

class Solution:
  def minCostClimbingStairs(self, cost: List[int]) -> int:
    dp = dict()

    return min(
      self.minCostClimbingStairsHelper(cost, 0, dp),
      self.minCostClimbingStairsHelper(cost, 1, dp)
    )
  
  def minCostClimbingStairsHelper(self, cost: List[int], index: int, dp: dict) -> int:
    if index >= len(cost):
      return 0

    if not index in dp:
      dp[index] = min(
        self.minCostClimbingStairsHelper(cost, index + 1, dp) + cost[index],
        self.minCostClimbingStairsHelper(cost, index + 2, dp) + cost[index]
      )

    return dp[index]

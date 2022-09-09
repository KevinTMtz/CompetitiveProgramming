#
# LeetCode
#
# Problem - 122
# URL - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
#

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    profit = 0

    for i in range(len(prices) - 1):
      if prices[i] < prices[i+1]:
        profit += prices[i+1] - prices[i]

    return profit

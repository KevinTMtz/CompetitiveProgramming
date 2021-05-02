#
# LeetCode
#
# Problem - 121
# URL - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    minPrice = float('inf')
    maxProfit = 0

    for price in prices:
      if (price < minPrice):
        minPrice = price
      else:
        maxProfit = max(maxProfit, price - minPrice)

    return maxProfit

#
# LeetCode
#
# Problem - 1672
# URL - https://leetcode.com/problems/richest-customer-wealth/
#

class Solution:
  def maximumWealth(self, accounts: List[List[int]]) -> int:
    maxWealth = 0

    for account in accounts:
      accountSum = sum(account)

      maxWealth = maxWealth if maxWealth > accountSum else accountSum

    return maxWealth

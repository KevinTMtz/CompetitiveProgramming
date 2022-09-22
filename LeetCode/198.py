#
# LeetCode
#
# Problem - 198
# URL - https://leetcode.com/problems/house-robber/
#

class Solution:
  def rob(self, nums: List[int]) -> int:
    robbed = 0
    notRobbed = 0
    
    for money in nums:
      robbed, notRobbed = notRobbed + money, max(robbed, notRobbed)
    
    return max(robbed, notRobbed)

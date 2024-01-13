#
# LeetCode
#
# Problem - 213
# URL - https://leetcode.com/problems/house-robber-ii/submissions/1144693427/
#

class Solution:
  def rob(self, nums: List[int]) -> int:
    if len(nums) <= 3:
      return max(nums)

    ans_1, robbed, not_robbed = 0, 0, 0
    for i in range(len(nums) - 1):
      robbed, not_robbed = not_robbed + nums[i], max(robbed, not_robbed)
    ans_1 = max(robbed, not_robbed)

    robbed, not_robbed = 0, 0
    for i in range(1, len(nums)):
      robbed, not_robbed = not_robbed + nums[i], max(robbed, not_robbed)

    return max(ans_1, robbed, not_robbed)

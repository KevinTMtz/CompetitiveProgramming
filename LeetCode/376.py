#
# LeetCode
#
# Problem - 376
# URL - https://leetcode.com/problems/wiggle-subsequence/description/
#

class Solution:
  def wiggleMaxLength(self, nums: List[int]) -> int:
    ans = len(nums)

    if ans < 2:
      return ans

    lastDiff = 0
    for i in range(1, len(nums)):
      newDiff = nums[i] - nums[i - 1]

      if newDiff == 0 or lastDiff < 0 > newDiff or lastDiff > 0 < newDiff:
        ans -= 1
      else:
        lastDiff = newDiff

    return ans

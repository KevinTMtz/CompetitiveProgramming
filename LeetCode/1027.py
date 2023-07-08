#
# LeetCode
#
# Problem - 1027
# URL - https://leetcode.com/problems/longest-arithmetic-subsequence/description/
#

class Solution:
  def longestArithSeqLength(self, nums: List[int]) -> int:
    dynamicP = {}
    ans = 2

    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        difference = nums[j] - nums[i]
        dynamicP[(j, difference)] = dynamicP.get((i, difference), 1) + 1
        ans = max(ans, dynamicP[(j, difference)])

    return ans

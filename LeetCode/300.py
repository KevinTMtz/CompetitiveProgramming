#
# LeetCode
#
# Problem - 300
# URL - https://leetcode.com/problems/longest-increasing-subsequence/
#

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    if len(nums) == 0:
      return 0

    memoizationList = []
    for n in nums:
      pos = bisect.bisect_left(memoizationList, n)
      if pos == len(memoizationList):
        memoizationList.append(n)
      else:
        memoizationList[pos] = n

    return len(memoizationList)

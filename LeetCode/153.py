#
# LeetCode
#
# Problem - 153
# URL - https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
#

class Solution:
  def findMin(self, nums: List[int]) -> int:
    minNum = float('inf')

    for i in nums:
      minNum = min(minNum, i)

    return minNum

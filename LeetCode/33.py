#
# LeetCode
#
# Problem - 33
# URL - https://leetcode.com/problems/search-in-rotated-sorted-array/
#

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    if target in nums:
      return nums.index(target)
    else:
      return -1

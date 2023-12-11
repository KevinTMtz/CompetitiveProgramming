#
# LeetCode
#
# Problem - 704
# URL - https://leetcode.com/problems/binary-search/
#

class Solution:
  def search(self, nums: List[int], target: int) -> int:
    l = 0
    r = len(nums) - 1

    while l <= r:
      m = (l + r) // 2
      num = nums[m]

      if num == target:
        return m
      elif num > target:
        r = m - 1
      elif num < target:
        l = m + 1

    return -1

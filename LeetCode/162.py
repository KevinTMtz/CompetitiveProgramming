#
# LeetCode
#
# Problem - 162
# URL - https://leetcode.com/problems/find-peak-element/description/
#

class Solution:
  def findPeakElement(self, nums: List[int]) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
      m = (l + r) // 2

      if (
        (m == len(nums) - 1 or nums[m] > nums[m + 1])
        and (m == 0 or nums[m] > nums[m - 1])
      ):
        return m
      elif nums[m] < nums[m + 1]:
        l = m + 1
      elif nums[m] < nums[m - 1]:
        r = m - 1

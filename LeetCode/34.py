#
# LeetCode
#
# Problem - 34
# URL - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
#

class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    indexes = [-1, -1]

    l = 0
    r = len(nums) - 1
    while l <= r:
      index = (l+r)//2

      if nums[index] == target and indexes[0] != 1:
        indexes[0] = index
        break

      elif nums[index] < target:
        l = index + 1

      elif nums[index] > target:
        r = index - 1

      index = int((r-l)/2)+l

    if indexes[0] != -1:
      indexes[1] = indexes[0]
      temp = indexes[0]
      while (temp-1 >= 0 and nums[temp-1] == target):
        temp -= 1
      indexes[0] = temp

      temp = indexes[1]
      while (temp+1 < len(nums) and nums[temp+1] == target):
        temp += 1
      indexes[1] = temp

    return indexes

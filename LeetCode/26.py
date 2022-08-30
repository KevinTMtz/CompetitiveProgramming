#
# LeetCode
#
# Problem - 26
# URL - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
#

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    numCheckPoint = nums[0]

    count = len(nums)
    for i, num in enumerate(range(1, len(nums))):
      if num == numCheckPoint:
        count -= 1
      else:
        numCheckPoint = num

    for i in range(count):
      nums[i] = i+1

    return count

#
# LeetCode
#
# Problem - 283
# URL - https://leetcode.com/problems/move-zeroes/
#

class Solution:
  def moveZeroes(self, nums: List[int]) -> None:
    lastNum = None
    for i in range(len(nums)):
      if nums[i] == 0:
        for j in range(lastNum if lastNum else i+1, len(nums)):
          if nums[j] != 0:
            lastNum = j+1
            nums[j], nums[i] = nums[i], nums[j]
            break

          if j == len(nums) - 1:
            return

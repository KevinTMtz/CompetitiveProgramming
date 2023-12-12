#
# LeetCode
#
# Problem - 167
# URL - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
#

class Solution:
  def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    while l < r:
      currentSum = numbers[l] + numbers[r]

      if currentSum == target:
        return [l+1, r+1]
      elif currentSum < target:
        l += 1
      elif currentSum > target:
        r -= 1

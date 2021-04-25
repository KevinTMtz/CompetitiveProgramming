#
# LeetCode
#
# Problem - 1
# URL - https://leetcode.com/problems/two-sum/
#

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    complement = {target - nums[0]}

    for i in range(1, len(nums)):
      if (nums[i] in complement):
        return [nums.index(target - nums[i]), i]

      complement.add(target - nums[i])

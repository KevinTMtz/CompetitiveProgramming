#
# LeetCode
#
# Problem - 136
# URL - https://leetcode.com/problems/single-number/
#

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    return reduce(lambda xorValue, num: xorValue ^ num, nums)

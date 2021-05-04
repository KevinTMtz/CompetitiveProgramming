#
# LeetCode
#
# Problem - 179
# URL - https://leetcode.com/problems/largest-number/
#

class LargerNumKey(str):
  def __lt__(x, y):
    return x+y > y+x


class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    nums = list(map(str, nums))
    nums = sorted(nums, key=LargerNumKey)

    if (nums[0] == '0'):
      return "0"

    ans = ""
    for element in nums:
      ans += element
    return ans

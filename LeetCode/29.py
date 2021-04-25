#
# LeetCode
#
# Problem - 29
# URL - https://leetcode.com/problems/divide-two-integers/
#

class Solution:
  def divide(self, dividend: int, divisor: int) -> int:
    if dividend == -2147483648 and divisor == -1:
      return 2147483647
    elif dividend == -2147483648 and divisor == 1:
      return -2147483648
    elif dividend // divisor >= 0:
      return dividend // divisor
    else:
      if (dividend / divisor) == int(dividend / divisor):
        return dividend // divisor
      return dividend // divisor + 1

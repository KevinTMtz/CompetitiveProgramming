#
# LeetCode
#
# Problem - 7
# URL - https://leetcode.com/problems/reverse-integer/
#

class Solution:
  def reverse(self, x: int) -> int:
    ans = 0

    negative = False
    if x < 0:
      negative = True
      x *= -1

    while x > 0:
      difference = x % 10

      ans = ans * 10 + difference
      x = (x - difference) / 10

    return 0 if ans > 2 ** 31 else int(ans) * (-1 if negative else 1)

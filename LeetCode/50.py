#
# LeetCode
#
# Problem - 50
# URL - https://leetcode.com/problems/powx-n/
#

class Solution:
  def myPow(self, x: float, n: int) -> float:
    if n == 0:
      return 1

    temp = self.myPow(x, abs(n) // 2)

    ans = 0
    if n % 2 == 0:
      ans = temp * temp
    else:
      ans = x * temp * temp

    if n > 0:
      return ans
    else:
      return 1 / ans

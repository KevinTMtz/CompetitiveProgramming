#
# LeetCode
#
# Problem - 509
# URL - https://leetcode.com/problems/fibonacci-number/description/
#

class Solution:
  def fib(self, n: int) -> int:
    first = 0
    second = 1

    if n == 0:
      return first
    elif n == 1:
      return second

    for i in range(n - 1):
      first, second = second, first + second

    return second

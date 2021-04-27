#
# LeetCode
#
# Problem - 69
# URL - https://leetcode.com/problems/sqrtx/
#

class Solution:
  def mySqrt(self, x: int) -> int:
    l = 1
    r = x
    while(l != r):
      temp = (l + r) // 2
      if (temp**2 == x):
        return temp
      elif (temp**2 > x):
        r = temp
      elif (temp**2 < x):
        if ((temp+1)**2 > x):
          return temp
        l = temp

    return 1

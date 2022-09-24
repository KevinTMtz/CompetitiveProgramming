#
# LeetCode
#
# Problem - 326
# URL - https://leetcode.com/problems/power-of-three/
#

class Solution:
  def isPowerOfThree(self, n: int) -> bool:
    if not n > 0:
      return False
    
    i = math.log10(n) / math.log10(3)
    
    return i % 1 == 0

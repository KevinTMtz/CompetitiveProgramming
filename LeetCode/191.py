#
# LeetCode
#
# Problem - 191
# URL - https://leetcode.com/problems/number-of-1-bits/
#

class Solution:
  def hammingWeight(self, n: int) -> int:
    count = 0
    
    for i in range(32):
      if n & (1 << i):
        count += 1
      
    return count

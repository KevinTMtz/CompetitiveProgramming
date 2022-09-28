#
# LeetCode
#
# Problem - 190
# URL - https://leetcode.com/problems/reverse-bits/
#

class Solution:
  def reverseBits(self, n: int) -> int:
    ans = 0
    
    for i in range(32):
      ans = (ans << 1) + ((n >> i) & 1)
      
    return ans

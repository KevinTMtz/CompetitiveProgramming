#
# LeetCode
#
# Problem - 70
# URL - https://leetcode.com/problems/climbing-stairs/
#

class Solution:
  memo = dict()
  
  def climbStairs(self, n: int) -> int:
    if n == 2:
      return 2
    elif n == 1:
      return 1
    
    if not n in self.memo:
      self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
      
    return self.memo[n]
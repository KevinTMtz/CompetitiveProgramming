#
# LeetCode
#
# Problem - 338
# URL - https://leetcode.com/problems/counting-bits/
#

class Solution:
  def countBits(self, n: int) -> List[int]:
    memo = {0: 0, 1: 1}
    
    ans = []
    
    lastPowerOfTwo = 1
    for i in range(n + 1):
      if i == 0 or i == 1:
        memo[i] = i
      
      elif i >= lastPowerOfTwo * 2:
        lastPowerOfTwo = lastPowerOfTwo * 2
        
        memo[i] = 1
        
      else:
        memo[i] = memo.get(i - lastPowerOfTwo) + 1
      
      ans.append(memo.get(i))
    
    return ans
        
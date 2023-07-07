#
# LeetCode
#
# Problem - 334
# URL - https://leetcode.com/problems/increasing-triplet-subsequence/
#

class Solution:
  def increasingTriplet(self, nums: List[int]) -> bool:
    first, second = inf, inf
    
    for current in nums:
      if second < current:
        return True
      if current <= first:
        first = current    
      else:
        second = current 
            
    return  False

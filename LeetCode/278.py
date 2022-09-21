#
# LeetCode
#
# Problem - 278
# URL - https://leetcode.com/problems/first-bad-version/
#

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
  def firstBadVersion(self, n: int) -> int:
    minL = 1
    maxL = n
    
    while True:
      if minL >= maxL:
        return minL
      
      middle = (minL + maxL) // 2
      
      if isBadVersion(middle):
        maxL = middle
      else:
        minL = middle + 1

#
# LeetCode
#
# Problem - 1326
# URL - https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/
#

class Solution:
  def minTaps(self, n: int, ranges: List[int]) -> int:
    ranges = [(i - r, i + r) for i, r in enumerate(ranges)]
    ranges.sort()
    
    ans = 0
    rightEnd = 0
    i = 0
    while i <= n and rightEnd < n:
      newRightEnd = rightEnd
      while i <= n and ranges[i][0] <= rightEnd:
        newRightEnd = max(newRightEnd, ranges[i][1])
        i += 1

      if newRightEnd == rightEnd:
        return -1

      rightEnd = newRightEnd
      ans += 1
    
    return ans

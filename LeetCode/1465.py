#
# LeetCode
#
# Problem - 1465
# URL - https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
#

class Solution:
  def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
    horizontalCuts = sorted(horizontalCuts)
    verticalCuts = sorted(verticalCuts)

    maxW = max(verticalCuts[0], w-verticalCuts[-1])
    maxH = max(horizontalCuts[0], h-horizontalCuts[-1])

    for i in range(0, len(verticalCuts)-1):
      maxW = max(maxW, verticalCuts[i+1]-verticalCuts[i])

    for i in range(0, len(horizontalCuts)-1):
      maxH = max(maxH, horizontalCuts[i+1]-horizontalCuts[i])

    return maxW * maxH % (10**9 + 7)

#
# LeetCode
#
# Problem - 1578
# URL - https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/
#

class Solution:
  def minCost(self, colors: str, neededTime: List[int]) -> int:
    totalTime = 0

    repeatedCount = 1
    totalCurrentTime = neededTime[0]
    currentMax = neededTime[0]
    for i in range(1, len(neededTime)):
      if colors[i-1] == colors[i]:
        repeatedCount += 1
        totalCurrentTime += neededTime[i]
        currentMax = max(currentMax, neededTime[i])
      else:
        if repeatedCount > 1:
          totalTime += totalCurrentTime - currentMax

        repeatedCount = 1
        totalCurrentTime = neededTime[i]
        currentMax = neededTime[i]

    if repeatedCount > 1:
      totalTime += totalCurrentTime - currentMax

    return totalTime

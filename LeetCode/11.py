#
# LeetCode
#
# Problem - 11
# URL - https://leetcode.com/problems/container-with-most-water/
#

class Solution:
  def maxArea(self, height: List[int]) -> int:
    l = 0
    r = len(height) - 1

    maxArea = 0
    while l != r:
      maxArea = max(maxArea, (r - l) * min(height[l], height[r]))

      if height[l] <= height[r]:
        l += 1
      else:
        r -= 1

    return maxArea

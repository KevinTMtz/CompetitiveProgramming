#
# LeetCode
#
# Problem - 739
# URL - https://leetcode.com/problems/daily-temperatures/submissions/
#

class Solution:
  def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    ans = [0] * len(temperatures)

    stack = []
    for i in range(len(temperatures) - 1, -1, -1):
      while stack and stack[-1][0] <= temperatures[i]:
        stack.pop()

      if stack:
        ans[i] = stack[-1][1] - i

      stack.append((temperatures[i], i))

    return ans

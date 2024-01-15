#
# LeetCode
#
# Problem - 62
# URL - https://leetcode.com/problems/unique-paths/submissions/1146617922/
#

class Solution:
  def uniquePaths(self, m: int, n: int) -> int:
    return self.uniquePathsHelper(m, n, (0, 0), None, dict())

  def uniquePathsHelper(self, m: int, n:int, coor: (int, int), direction: string, dp: dict) -> int:
    if m == 1 or n == 1:
      return 1

    if coor in dp:
      return dp[coor]

    x, y = coor
    if x == n - 1 and y == m - 1:
      return 0

    ans = 0
    if x < n - 1:
      ans += self.uniquePathsHelper(m, n, (x + 1, y), 'r', dp) + (direction != 'r' and not y == m - 1)
    if y < m - 1:
      ans += self.uniquePathsHelper(m, n, (x, y + 1), 'd', dp) + (direction != 'd' and not x == n - 1)

    dp[coor] = ans
    return dp[coor]

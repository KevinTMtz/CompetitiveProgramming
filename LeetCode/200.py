#
# LeetCode
#
# Problem - 200
# URL - https://leetcode.com/problems/number-of-islands/
#

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    if not grid:
      return 0

    xLen = len(grid[0])
    yLen = len(grid)

    islandsCount = 0
    queue = []
    for i in range(yLen):
      for k in range(xLen):
        if(grid[i][k] == '1'):
          queue.append((i, k))
          islandsCount += 1

          while (queue):
            y, x = queue.pop()

            grid[y][x] = '2'

            if (y > 0 and grid[y-1][x] == '1'):
              queue.append((y-1, x))
            if (y+1 < yLen and grid[y+1][x] == '1'):
              queue.append((y+1, x))
            if (x > 0 and grid[y][x-1] == '1'):
              queue.append((y, x-1))
            if (x+1 < xLen and grid[y][x+1] == '1'):
              queue.append((y, x+1))

    return islandsCount

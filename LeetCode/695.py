#
# LeetCode
#
# Problem - 695
# URL - https://leetcode.com/problems/max-area-of-island/description/
#

class Solution:
  def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    visited = dict()

    max_area = 0
    for y in range(len(grid)):
      for x in range(len(grid[0])):
        if not visited.get((x,y), False) and grid[y][x] == 1:
          max_area = max(max_area, self.maxAreaOfIslandHelper(grid, visited, (x, y)))

    return max_area

  def maxAreaOfIslandHelper(self, grid: List[List[int]], visited: dict, coor: (int, int)) -> int:
    visited[coor] = True

    island_area = 1

    x_coors = [coor[0]-1, coor[0]+1]
    for x_coor in x_coors:
      y_coor = coor[1]
      if (
        x_coor >= 0 and x_coor < len(grid[0])
        and grid[y_coor][x_coor] == 1
        and not visited.get((x_coor, y_coor), False)
      ):
        island_area += self.maxAreaOfIslandHelper(grid, visited, (x_coor, y_coor))

    y_coors = [coor[1]-1, coor[1]+1]
    for y_coor in y_coors:
      x_coor = coor[0]
      if (
        y_coor >= 0 and y_coor < len(grid)
        and grid[y_coor][x_coor] == 1
        and not visited.get((x_coor, y_coor), False)
      ):
        island_area += self.maxAreaOfIslandHelper(grid, visited, (x_coor, y_coor))

    return island_area
    
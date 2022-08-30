#
# LeetCode
#
# Problem - 1232
# URL - https://leetcode.com/problems/check-if-it-is-a-straight-line/
#

class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    if (len(coordinates) < 3):
      return True

    for i in range(len(coordinates) - 2):
      coor1 = coordinates[i]
      coor2 = coordinates[i+1]
      coor3 = coordinates[i+2]

      area = (
          coor1[0]*(coor2[1]-coor3[1]) +
          coor2[0]*(coor3[1]-coor1[1]) +
          coor3[0]*(coor1[1]-coor2[1])
      )

      if area != 0:
        return False

    return True

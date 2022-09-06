#
# LeetCode
#
# Problem - 48
# URL - https://leetcode.com/problems/rotate-image/
#

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    for i in range(len(matrix)):
      for j in range(i+1, len(matrix)):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

      matrix[i].reverse()

#
# LeetCode
#
# Problem - 54
# URL - https://leetcode.com/problems/spiral-matrix/
#


class Solution:
  def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    if (not matrix or not matrix[0]):
      return []

    indexV1 = 0
    indexV2 = len(matrix)
    indexH1 = 0
    indexH2 = len(matrix[0])

    ansList = []

    n = len(matrix) * len(matrix[0])

    while n > 0:
      for i in range(indexH1, indexH2):
        ansList.append(matrix[indexV1][i])
        n -= 1

      for i in range(indexV1+1, indexV2):
        ansList.append(matrix[i][indexH2-1])
        n -= 1

      if (indexV2 - indexV1 > 1):
        for i in range(indexH2-2, indexH1, -1):
          ansList.append(matrix[indexV2-1][i])
          n -= 1

      if (indexH2 - indexH1 > 1):
        for i in range(indexV2-1, indexV1, -1):
          ansList.append(matrix[i][indexH1])
          n -= 1

      indexV1 += 1
      indexV2 -= 1
      indexH1 += 1
      indexH2 -= 1

    return ansList
